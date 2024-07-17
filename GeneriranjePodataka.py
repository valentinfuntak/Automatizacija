import os
import random
import string

# Rječnik za mjesec na hrvatskom jeziku
mjeseci_hr = {
    1: 'siječanj',
    2: 'veljača',
    3: 'ožujak',
    4: 'travanj',
    5: 'svibanj',
    6: 'lipanj',
    7: 'srpanj',
    8: 'kolovoz',
    9: 'rujan',
    10: 'listopad',
    11: 'studeni',
    12: 'prosinac'
}

# METODE
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_first_name():
    return generate_random_string(random.randint(5, 10))

def generate_last_name():
    return generate_random_string(random.randint(5, 10))

def generate_date_of_birth():
    year = random.randint(1970, 2003)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assume every month has 28 days for simplicity
    month_hr_name = mjeseci_hr[month]
    return day, month_hr_name, year  # Vraćamo trojku (dan, mjesec, godina)

def generate_gender():
    genders = ['Muškarac', 'Žena']  # Promijenjeni nazivi spolova na hrvatski
    return random.choice(genders)

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_email(first_name, last_name):
    domains = ['example.com', 'test.com', 'mail.com']  # Dodajte više domena po potrebi
    domain = random.choice(domains)
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"


def get_last_index(file_path):
    if not os.path.exists(file_path):
        return 0  # Ako datoteka ne postoji, počinjemo s indeksom 0
    else:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                # Tražimo zadnji redak koji sadrži "Account X:", gdje je X broj
                for line in reversed(lines):
                    if line.startswith("Account "):
                        last_index = int(line.split()[1].strip(':'))
                        return last_index
                # Ako nije pronađen niti jedan važeći indeks, vraćamo 0
                return 0
            else:
                return 0  # Ako datoteka postoji, ali nema računa, počinjemo s indeksom 0

def save_data_to_file(index, first_name, last_name, date_of_birth, gender, password, email, file_path):
    confirm_password = password  # Postavljamo confirm_password na istu vrijednost kao i password
    with open(file_path, 'a') as file:
        file.write(f"=========================================\n")
        file.write(f"Account {index}:\n")
        file.write(f"=========================================\n")
        file.write(f"First Name: {first_name}\n")
        file.write(f"Last Name: {last_name}\n")
        file.write(f"Date of Birth: {date_of_birth}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Confirm Password: {confirm_password}\n")
        file.write(f"Email: {email}\n\n")
        
# MAIN FUNKCIJA
if __name__ == "__main__":
    directory = 'podaci'
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, r'C:\Users\valen\Desktop\Selenium_Automatization\Podaci\generated_accounts.txt')

    num_accounts = 1  # Broj računa koje želimo generirati

    # Dobivanje posljednjeg indeksa iz datoteke
    last_index = get_last_index(file_path)

    # Set za pohranu već generiranih podataka
    existing_data = set()

    # Generiranje novih računa s nastavljanjem od zadnjeg indeksa + 1
    for i in range(last_index + 1, last_index + 1 + num_accounts):
        while True:
            first_name = generate_first_name()
            last_name = generate_last_name()
            date_of_birth = generate_date_of_birth()
            gender = generate_gender()
            email = generate_email(first_name, last_name)
            password = generate_password()

            # Provjera jedinstvenosti podataka
            data_set = (first_name, last_name, date_of_birth, gender, password)
            if data_set not in existing_data:
                existing_data.add(data_set)
                break

        # Spremanje novog računa u datoteku
        save_data_to_file(i, first_name, last_name, date_of_birth, gender, password, email, file_path)
    print(f"Generated {num_accounts} accounts saved to {file_path}")

