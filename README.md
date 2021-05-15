# COVID-19-Vaccine-Slot-Finder

## Getting Started

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



# Sample Output:

> python covid-vaccine-finder.py --age 45 --pincode 560037 --days 1

+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
|    Date    |         Center        |  Vaccine   | Capacity | Price |                             Address                              |      Slots      |
+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
| 15-05-2021 | Doddanekkundi UPHC P3 | COVISHIELD |    10    |  Free |       NEAR RAM TEMPLE VIBHUTIPURA EXTENSION DODDANEKKUNDI        | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 15-05-2021 |  Marathahalli UPHC P3 | COVISHIELD |    12    |  Free | PHC MARATHALLI ANANAD NAGAR 2ND CROSS MARATHALLI BANGLORE 560037 | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 15-05-2021 |  Vibuthipura UPHC P3  | COVISHIELD |    25    |  Free |  Annasandrapalya Main Rd, Ramesh Nagar, Vibhutipura, Bengaluru,  | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
| 15-05-2021 |    YAMLURU UPHC P3    | COVISHIELD |    6     |  Free |             Kempapura MAIN ROAD,Bellandur, Bengaluru             | 10:00AM-11:00AM |
|            |                       |            |          |       |                                                                  | 11:00AM-12:00PM |
|            |                       |            |          |       |                                                                  | 12:00PM-01:00PM |
|            |                       |            |          |       |                                                                  | 01:00PM-04:00PM |
|            |                       |            |          |       |                                                                  |                 |
+------------+-----------------------+------------+----------+-------+------------------------------------------------------------------+-----------------+
 

