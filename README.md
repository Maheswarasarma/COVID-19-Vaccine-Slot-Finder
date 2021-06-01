# COVID-19-Vaccine-Slot-Finder

Note: - Due to privacy issues in linux systems requests are getting blocked <br><br>
however, script is working fine in Windows platform

## Getting Started

## Pre-requisites

We Highly Recommended to use `Anaconda`  https://www.anaconda.com/products/individual


## Setting up Environment

1. Download source code `git clone https://github.com/Maheswarasarma/COVID-19-Vaccine-Slot-Finder.git`
2. change directory `cd COVID-19-Vaccine-Slot-Finder`
3. Go to anaconda prompt and execute  `pip install -r requirements.txt`

After above steps, execute `run.bat` for continuous monitoring of available slots <br><br>
Make sure to edit run.bat (add your age/pincode/district/dose/email/weeks) before running it <br>
Keep only options as per your preference (please find list of optional arguments below)


## Update

Added `run.bat` to execute script every 10 min <br>

Things to be done before running batch file: edit batch file to contain age/pincode/email properly<br><br>

## Running the script
1. `python covid-vaccine-finder.py --age <age> --district <district> --weeks <no.of.weeks> --dose <1|2> --email <email>` for district based search
2. `python covid-vaccine-finder.py --age <age> --pincode <pincode> --weeks <no.of.weeks> --dose <1|2> --email <email>` for pincode based search


## New Feature - Telegram messaging
This feature will send sms to telegram chat when slots are available <br><br>
set env variables `telegram_token and telegram_chat_id`

Example:<br/>

In Windows <br><br>
`set telegram_token=1234567890:AABcDdEeFfgGhHhzHQRxYufubSdjfXO9Y678`
<br/>
`set telegram_chat_id=@TelegramBot`

(or) we can set these environment variables globally, refer https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/ <br>

(or) we can pass telegram tokens as arguments
-token <token> -chat <chat_id> <br>

## Telegram Token/ID generation <br/>
Follow below link on how to generate telegram token/ID <br/>
https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token


After above steps add your bot to Newly created group/channel as admin.
Use that group/channel Id as telegram_chat_id <br>

## Usage
Vaccine Slot Availability Finder

`usage: covid-vaccine-finder.py -a AGE -p PINCODE [-e EMAIL] [-weeks WEEKS] [-v] [-version] [-h]`
```
required arguments:
  -a <AGE>,             --age          <AGE>        Enter required age to get vaccine availability
  -p <PINCODE>,         --pincode      <PINCODE>    Enter area pincode
  
optional arguments:
  -e     <EMAIL>,        --email        <EMAIL>      Enter email to receive alert
  -weeks <WEEKS>,        --weeks        <WEEKS>      Enter no. of weeks to search
  -dose  <DOSE>,         --dose         <DOSE>       Enter dose1/dose2 preference: eg: -dose 1 (or) -dose 2 
  -v,                    --verbose                   Print out the progress
  -version               --version                   Print the version of the script
  -h,                    -help, --help               Show this help message and exit
  -district <DISTRICT>,  --district     <DISTRICT>   Enter district name eg: Jagtial, Rangareddy
```

## Sample output from terminal

```
> python covid-vaccine-finder.py --age 46 -district Jagtial -weeks 1

 Available slots:

+------------+---------------------+---------+----------+--------+--------+-------+-----------------+---------+-----------------+
|    Date    |        Center       | Vaccine | Capacity | Dose 1 | Dose 2 | Price |     Address     | Pincode |      Slots      |
+------------+---------------------+---------+----------+--------+--------+-------+-----------------+---------+-----------------+
| 31-05-2021 | Allamayyagutta UPHC | COVAXIN |    10    |   0    |   10   |  Free | Allamaiah Gutta |  505326 | 10:00AM-11:00AM |
|            |                     |         |          |        |        |       |                 |         | 11:00AM-12:00PM |
|            |                     |         |          |        |        |       |                 |         | 12:00PM-01:00PM |
|            |                     |         |          |        |        |       |                 |         | 01:00PM-04:00PM |
|            |                     |         |          |        |        |       |                 |         |                 |
| 31-05-2021 | Allamayyagutta UPHC | COVAXIN |    10    |   0    |   10   |  Free | Allamaiah Gutta |  505326 | 10:00AM-11:00AM |
|            |                     |         |          |        |        |       |                 |         | 11:00AM-12:00PM |
|            |                     |         |          |        |        |       |                 |         | 12:00PM-01:00PM |
|            |                     |         |          |        |        |       |                 |         | 01:00PM-04:00PM |
|            |                     |         |          |        |        |       |                 |         |                 |
+------------+---------------------+---------+----------+--------+--------+-------+-----------------+---------+-----------------+
```


## Sample Email output

![image](https://user-images.githubusercontent.com/25954119/119632213-3ad8ec80-be2e-11eb-855e-b7ffe7306c08.png)




## Sample Telegram chat

![image](https://user-images.githubusercontent.com/25954119/119632361-5c39d880-be2e-11eb-9cc0-40a912607e66.png)



 ## Development
 
 Want to contribute? Please feel free to raise pull request 😇
