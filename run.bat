pip install -r requirements.txt
cd COVID-19-Vaccine-Slot-Finder
:loop
python covid-vaccine-finder.py --age <age> --pincode <pincode> --days <no.of.days> --email <email_id>
PING localhost -n 600 >NUL
goto loop
