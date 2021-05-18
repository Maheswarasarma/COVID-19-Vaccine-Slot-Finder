git clone https://github.com/Maheswarasarma/COVID-19-Vaccine-Slot-Finder.git
cd COVID-19-Vaccine-Slot-Finder.git
pip install -r requirements.txt
:loop
python covid-vaccine-finder.py --age <age> --pincode <pincode> --days <no.of.days> --email <email_id>
PING localhost -n 600 >NUL
goto loop
