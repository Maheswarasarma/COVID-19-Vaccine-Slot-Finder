pip install -r requirements.txt
cd COVID-19-Vaccine-Slot-Finder
:loop
python covid-vaccine-finder.py --age <age> --pincode <pincode> --weeks <no.of.weeks> --dose <1|2> --email <email_id> --token <telegram_token> --chat <telegram_chat>
PING localhost -n 600 >NUL
goto loop
