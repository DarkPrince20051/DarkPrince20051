import phonenumbers
from phonenumbers import geocoder, carrier
from myphone import number

try:
    # Parsiranje broja
    pepnumber = phonenumbers.parse(number)

    # Dobivanje informacija o lokaciji
    location = geocoder.description_for_number(pepnumber, "en")
    print("Lokacija:", location)

    # Dobivanje informacija o operateru
    service_provider = carrier.name_for_number(pepnumber, "en")
    if service_provider:
        print("Operater:", service_provider)
    else:
        print("Operater nije pronađen.")
except phonenumbers.NumberParseException as e:
    print(f"Greška pri parsiranju broja: {e}")
except Exception as e:
    print(f"Došlo je do greške: {e}")
