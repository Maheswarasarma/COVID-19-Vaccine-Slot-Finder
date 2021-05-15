# COVID-19-Vaccine-Slot-Finder

## Getting Started

## Pre-requisites

Recommended python version `Python 3.0+`

## Setting up Environment

1. Create virtual env using `virtualenv env --python python3`
2. source the new env using `source env/bin/activate`


## Installation

Upon successful completion of setup, run the following command in your terminal  `pip install -r requirements.txt`


## Optional Feature - Telegram messaging
set env variables `telegram_token and telegram_chat_id`

Example:<br/>

In Linux Bash-shell <br/>
`export telegram_token=1234567890:AABcDdEeFfgGhHhzHQRxYufubSdjfXO9Y678`
<br/>
 `export telegram_chat_id=@TelegramBot`
 
In Linux C-shell <br/>
`setenv telegram_token 1234567890:AABcDdEeFfgGhHhzHQRxYufubSdjfXO9Y678`
<br/>
`setenv telegram_chat_id @TelegramBot`

In Windows <br/>
`set telegram_token=1234567890:AABcDdEeFfgGhHhzHQRxYufubSdjfXO9Y678`
<br/>
`set telegram_chat_id=@TelegramBot`


## Telegram Token/ID generation <br/>
Follow below link on how to generate telegram token/ID <br/>
https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token

## Usage
Vaccine Slot Availability Finder

`usage: covid-vaccine-finder.py -a AGE -p PINCODE [-e EMAIL] [-d DAYS] [-v] [-version] [-h]`
```
required arguments:
  -a AGE,     --age     AGE      Enter required age to get vaccine availability
  -p PINCODE, --pincode PINCODE  Enter area pincode

optional arguments:
  -e EMAIL, --email   EMAIL   Enter email to receive alert
  -d DAYS,  --days    DAYS    Enter no. of days to search
  -v,       --verbose         print out the progress
  -version  --version         print the version of the script
  -h,       -help, --help     Show this help message and exit
```

## Sample output from terminal

```
> python covid-vaccine-finder.py --age 45 --pincode 560037 --days 1

+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
|    Date    |         Center        |  Vaccine   | Capacity | Price |                             Address                              |      Slots      |
+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
| 10-05-2021 | Doddanekkundi UPHC P3 | COVISHIELD |    10    |  Free |       NEAR RAM TEMPLE VIBHUTIPURA EXTENSION DODDANEKKUNDI        | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 10-05-2021 |  Marathahalli UPHC P3 | COVISHIELD |    12    |  Free | PHC MARATHALLI ANANAD NAGAR 2ND CROSS MARATHALLI BANGLORE 560037 | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 10-05-2021 |  Vibuthipura UPHC P3  | COVISHIELD |    25    |  Free |  Annasandrapalya Main Rd, Ramesh Nagar, Vibhutipura, Bengaluru,  | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 10-05-2021 |    YAMLURU UPHC P3    | COVISHIELD |    6     |  Free |             Kempapura MAIN ROAD,Bellandur, Bengaluru             | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
```


## Sample Email output

![image](https://user-images.githubusercontent.com/25954119/118352449-1ef85f80-b57f-11eb-9926-4fcd5ac34004.png)


## Sample Telegram chat

![image](https://user-images.githubusercontent.com/25954119/118352467-3e8f8800-b57f-11eb-9e47-fbc21b1c1858.png)

 
