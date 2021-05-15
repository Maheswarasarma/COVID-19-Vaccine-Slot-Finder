# *************************************************************************
# Author      : Maheswara Sarma
# Description : This script will show vaccine availability in India!
# *************************************************************************

import os
import sys
import json
import signal
import smtplib
import requests
import warnings
import datetime
import argparse
import email.message
from io import StringIO
from datetime import date
from functools import partial
from twilio.rest import Client
from prettytable import PrettyTable

# ################### C L A S S E S ####################### #

# global variables
global age, pin, flag, outputs, p_table


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class Operations:
    # base class class constructor
    def __init__(self, o_args):
        self.args = o_args

    # Method to generate table
    def table_dump(self, center, session, p_table):
        global flag
        a_slots = ''
        if 'slots' in session:
            for slot in session["slots"]:
                a_slots = a_slots + slot + "\n"
        if a_slots != '':
            flag = 0
            p_table.add_row([session["date"],
                             center["name"],
                             session["vaccine"],
                             session["available_capacity"],
                             session["available_capacity_dose1"],
                             session["available_capacity_dose2"],
                             center["fee_type"],
                             center["address"],
                             a_slots])

    # Method to generate text msg
    def telegram_dump(self, inp_date, center, session):
        print("Vaccine Available on: {}".format(inp_date))
        print("-" * 50)
        print("Center   : ", center["name"])
        print("Vaccine  : ", session["vaccine"])
        print("Price    : ", center["fee_type"])
        print("Capacity : ", session["available_capacity"])
        print("Dose 1   : ", session["available_capacity_dose1"])
        print("Dose 2   : ", session["available_capacity_dose2"])
        print("Address  : ", center["address"])
        if 'slots' in session:
            print("\nslots  :\n")
            for slot in session["slots"]:
                print(slot)
            print("-" * 50)
            print('\n\n')

    # Method to send telegram msg
    def do_telegram(self, t_data, token, t_id):
        self._telegram_token = token.strip()
        self._telegram_chat_id = t_id.strip()
        alert_text = t_data
        if bool(self._telegram_token and self._telegram_chat_id):
            print("sending telegram ..")
            URL = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(
                self._telegram_token, self._telegram_chat_id, alert_text)
            ro = RestOperations(self.args)
            response = ro.post_operation(
                URL,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
                                           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
                expected_return_code=200)
        else:
            if self.args.verbose:
                print("No telegram tokens found!")

    # Method to send whatsapp msg
    def do_whatsapp(self, d_data, token, w_id):
        os.environ['TWILIO_AUTH_TOKEN'] = token
        os.environ['TWILIO_ACCOUNT_SID'] = w_id
        client = Client()
        self._from_whatsapp_number = 'whatsapp:+91XXXXXXXXXX'
        self._to_whatsapp_number = 'whatsapp:+91XXXXXXXXXX'

        client.messages.create(body=d_data,
                               from_=self._from_whatsapp_number,
                               to=self._to_whatsapp_number)

    # Method to get and process the data
    def process_data(self, p_date_str):
        global outputs
        for inp_date in p_date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={0}&date={1}" \
                .format(self.args.pincode, inp_date)
            ro = RestOperations(self.args)
            response = ro.get_operation(
                URL,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
                                          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
                expected_return_code=200)
            if response:
                for center in response["centers"]:
                    for session in center["sessions"]:
                        if int((session["available_capacity"] > 0
                                or session["available_capacity_dose1"] > 0
                                or session["available_capacity_dose2"] > 0) and
                                int(session["min_age_limit"]) <= int(self.args.age)):
                            if session['date'] == inp_date:
                                self.table_dump(center, session, p_table)
                                with Capturing() as output:
                                    self.telegram_dump(
                                        inp_date, center, session)
                                outputs.append(output)

    # Method to send email
    def send_mail(self, body):
        if self.args.email:
            print("sending email ..")
            sender = self.args.email
            recipients = [self.args.email]
            subject = 'Vaccine Availabilty as on %s' % str(
                date.today()).replace('-', '/')
            email_body = """<html>%s</html>""" % (
                body.get_html_string(format=True))
            try:
                try:
                    import win32com.client as win32
                    outlook = win32.Dispatch('outlook.application')
                    mail = outlook.CreateItem(0)
                    mail.To = ", ".join(recipients)
                    mail.Subject = subject
                    mail.HTMLbody = email_body
                    mail.Send()
                except ModuleNotFoundError:
                    msg = email.message.Message()
                    sender = self.args.email
                    msg['Subject'] = subject
                    msg['From'] = sender
                    msg['To'] = ", ".join(recipients)
                    msg.add_header('Content-Type', 'text/html')
                    msg.set_payload(email_body)
                    s = smtplib.SMTP('localhost')
                    s.sendmail(sender, recipients, msg.as_string())
                    s.quit()
            except ConnectionRefusedError:
                print("Unable to send email due to connection issue")


class RestOperations(Operations):

    def get_operation(self,
                      url,
                      headers,
                      params=None,
                      verify=False,
                      expected_return_code=None):
        """
        Method to perform GET Rest API operation

        :param url: url for the request
        :param header: dict of headers to send with the request
        :param verify: controls whether we verify the server's certificate
        :param expected_return_code: tuple of expected return codes

        :return: returns response from the server if the response status code is
                 in the expected return code

    """
        if args.verbose:
            print(
                'Requested url : %s, headers = %s, params = %s, expected return code = %s' %
                (url, headers, params, expected_return_code))
        try:
            resp = requests.get(url=url,
                                headers=headers,
                                params=params,
                                verify=verify)

            if isinstance(expected_return_code, int):
                expected_return_code = [expected_return_code]
            expected_return_codes = default_return_codes if expected_return_code is None else expected_return_code

            if resp.status_code in expected_return_codes:
                if args.verbose:
                    print(
                        "Check response status code --> \"%s\"" %
                        resp.status_code)
                return resp.json()
            else:
                print("Errored Response content is %s" % resp.content)
                print(resp.status_code)

        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError

        except Exception as err:
            print('Error occured: ', err)
            raise

    def post_operation(self,
                       url,
                       headers,
                       params=None,
                       verify=False,
                       expected_return_code=None):
        """
        Method to perform POST Rest API operation

        :param url: url for the request
        :param header: dict of headers to send with the request
        :param params: to send in the query string for the request
        :param data: any object like to be sent in the body of the request
        :param verify: controls whether we verify the server's certificate
        :param expected_return_code: tuple of expected return codes

        :return: returns response from the server if the response status code is in the expected return code

  """
        global expected_return_codes
        if args.verbose:
            print(
                'Requested url : %s, headers = %s, params = %s, expected return code = %s' %
                (url, headers, params, expected_return_code))
        if isinstance(expected_return_code, int):
            expected_return_code = [expected_return_code]
            expected_return_codes = self.default_return_codes if expected_return_code is None else expected_return_code
        try:
            resp = requests.post(url=url,
                                 headers=headers,
                                 params=params,
                                 verify=verify)

            if resp.status_code in expected_return_codes:
                if args.verbose:
                    print(
                        "Check response status code --> \"%s\"" %
                        resp.status_code)
                return resp
            else:
                print("Errored Response content is %s" % resp.content)
                print(resp.status_code)

        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError

        except Exception as err:
            print('Error occured: ', err)
            raise


# Function to handle signal
def signal_handler(signal, frame):
    print('\n\nCtrl+C received\n', flush=True)
    sys.exit(1)


# ################### B O D Y ####################### #

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)
    currentVersion = "Date: May-16-2021  (version 1.1)"

    if "-version" in str(sys.argv).lower():
        strLine = "***      {0}  -  {1}      ***".format(
            os.path.basename(sys.argv[0]), currentVersion)
        print(
            "*" *
            len(strLine) +
            "\n" +
            strLine +
            "\n" +
            "*" *
            len(strLine),
            flush=True)
        sys.exit(0)

    # telegram settings
    if 'telegram_token' in os.environ:
        telegram_token = os.environ['telegram_token']
    else:
        telegram_token = ''
    if 'telegram_chat_id' in os.environ:
        telegram_chat_id = os.environ['telegram_chat_id']
    else:
        telegram_chat_id = ''

    # whatsapp settings
    if 'TWILIO_AUTH_TOKEN' in os.environ:
        TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    else:
        TWILIO_AUTH_TOKEN = ''
    if 'TWILIO_AUTH_SID' in os.environ:
        TWILIO_AUTH_SID = os.environ['TWILIO_AUTH_SID']
    else:
        TWILIO_AUTH_SID = ''

    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(
        add_help=False, description='Vaccine Finder')
    parser.parse_known_args()

    requiredArgs = parser.add_argument_group('required arguments')
    optionalArgs = parser.add_argument_group('optional arguments')

    requiredArgs.add_argument(
        '-a',
        '--age',
        help='Enter required age to get vaccine availability',
        required=True)
    requiredArgs.add_argument(
        '-p',
        '--pincode',
        help='Enter area pincode',
        required=True)
    optionalArgs.add_argument(
        '-e',
        '--email',
        help='Enter email to receive alert',
        required=False)
    optionalArgs.add_argument(
        '-d',
        '--days',
        help='Enter no. of days to search',
        required=False)
    optionalArgs.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        default=False,
        help="print out the progress")
    optionalArgs.add_argument(
        "-version",
        action='version',
        version='',
        help="print the version of the script")
    optionalArgs.add_argument(
        "-h",
        "-help",
        "--help",
        action="help",
        help="Show this help message and exit")

    args = parser.parse_args()

    pin = args.pincode
    age = args.age

    if args.email:
        mailto = args.email

    if args.days:
        numdays = args.days
    else:
        numdays = 1

    default_return_codes = [200, 201, 204]
    base = datetime.datetime.today()
    date_list = [
        base +
        datetime.timedelta(
            days=x) for x in range(
            int(numdays))]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    flag = 1
    outputs = []
    p_table = PrettyTable()
    p_table.field_names = [
        "Date",
        "Center",
        "Vaccine",
        "Capacity",
        "Dose 1",
        "Dose 2",
        "Price",
        "Address",
        "Slots"]

    op = Operations(args)
    op.process_data(date_str)

    if flag == 1:
        p_table.add_row(['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    # print table to console
    print(p_table)

    if flag == 0:
        data = ''
        # send a notification message in telegram
        if outputs:
            for out in outputs:
                data += '\n'.join(out)
            op.do_telegram(data, telegram_token, telegram_chat_id)

        # send email if opted
        if args.email:
            op.send_mail(p_table)

# End of script
