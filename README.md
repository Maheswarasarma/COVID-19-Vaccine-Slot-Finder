# COVID-19-Vaccine-Slot-Finder

Note: - Due to privacy issues in linux systems requests are getting blocked <br>
however, script is working fine in Windows platform

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
  -a <AGE>,             --age          <AGE>        Enter required age to get vaccine availability
  -p <PINCODE>,         --pincode      <PINCODE>    Enter area pincode
  
optional arguments:
  -e <EMAIL>,           --email        <EMAIL>      Enter email to receive alert
  -d <DAYS>,            --days         <DAYS>       Enter no. of days to search
  -v,                   --verbose                   Print out the progress
  -version              --version                   Print the version of the script
  -h,                   -help, --help               Show this help message and exit
  -district <DISTRICT>, --district     <DISTRICT>   Enter district name eg: Jagtial, Rangareddy
```

## Sample output from terminal

```
> python covid-vaccine-finder.py --age 46 -district Jagtial -days 7

+------------+------------------------+------------+----------+--------+--------+-------+----------------------------------------------------------------+-----------------+
|    Date    |         Center         |  Vaccine   | Capacity | Dose 1 | Dose 2 | Price |                            Address                             |      Slots      |
+------------+------------------------+------------+----------+--------+--------+-------+----------------------------------------------------------------+-----------------+
| 19-05-2021 | SAI SANJIVANI HOSPITAL | COVISHIELD |    97    |   0    |   -3   |  Paid | 15, NH 16, Adarsha Nagar, Boyawada, Metpally, Telangana 505325 | 09:00AM-11:00AM |
|            |                        |            |          |        |        |       |                                                                | 11:00AM-01:00PM |
|            |                        |            |          |        |        |       |                                                                | 01:00PM-03:00PM |
|            |                        |            |          |        |        |       |                                                                | 03:00PM-06:00PM |
|            |                        |            |          |        |        |       |                                                                |                 |
| 20-05-2021 | SAI SANJIVANI HOSPITAL | COVISHIELD |    95    |   0    |   0    |  Paid | 15, NH 16, Adarsha Nagar, Boyawada, Metpally, Telangana 505325 | 09:00AM-11:00AM |
|            |                        |            |          |        |        |       |                                                                | 11:00AM-01:00PM |
|            |                        |            |          |        |        |       |                                                                | 01:00PM-03:00PM |
|            |                        |            |          |        |        |       |                                                                | 03:00PM-06:00PM |
|            |                        |            |          |        |        |       |                                                                |                 |
| 22-05-2021 | SAI SANJIVANI HOSPITAL | COVISHIELD |    96    |   0    |   -4   |  Paid | 15, NH 16, Adarsha Nagar, Boyawada, Metpally, Telangana 505325 | 09:00AM-11:00AM |
|            |                        |            |          |        |        |       |                                                                | 11:00AM-01:00PM |
|            |                        |            |          |        |        |       |                                                                | 01:00PM-03:00PM |
|            |                        |            |          |        |        |       |                                                                | 03:00PM-06:00PM |
|            |                        |            |          |        |        |       |                                                                |                 |
+------------+------------------------+------------+----------+--------+--------+-------+----------------------------------------------------------------+-----------------+
```


## Sample Email output

![image](https://user-images.githubusercontent.com/25954119/118475219-9964e300-b729-11eb-9687-6ea62a64d8bf.png)



## Sample Telegram chat

![image](https://user-images.githubusercontent.com/25954119/118475510-f82a5c80-b729-11eb-8dcd-4083ffb95072.png)


 
