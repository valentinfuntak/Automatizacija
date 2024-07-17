import os
import time
from clicknium import clicknium as cc

# Uvoz funkcije za parsiranje datuma rođenja i rječnika s mjesecima na hrvatskom
from GeneriranjePodataka import generate_date_of_birth as datum
from GeneriranjePodataka import mjeseci_hr

# METODE
def read_data_from_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return []

    with open(file_path, 'r') as file:
        accounts = []
        account = {}
        for line in file:
            if line.startswith("Account"):
                if account:
                    accounts.append(account)
                account = {}
                account['index'] = int(line.split()[1].strip(':'))
            elif line.startswith("First Name:"):
                account['first_name'] = line.split(":", 1)[1].strip()
            elif line.startswith("Last Name:"):
                account['last_name'] = line.split(":", 1)[1].strip()
            elif line.startswith("Date of Birth:"):
                account['date_of_birth'] = line.split(":", 1)[1].strip()
            elif line.startswith("Gender:"):
                account['gender'] = line.split(":", 1)[1].strip()
            elif line.startswith("Password:"):
                account['password'] = line.split(":", 1)[1].strip()
            elif line.startswith("Confirm Password:"):
                account['confirm_password'] = line.split(":", 1)[1].strip()
        if account:
            accounts.append(account)

    return accounts


def RegistracijaGoogle():
    directory = 'podaci'
    file_path = os.path.join(directory, r'C:\Users\valen\Desktop\Selenium_Automatization\Podaci\generated_accounts.txt')

    # Čitanje podataka iz datoteke
    accounts = read_data_from_file(file_path)
    if not accounts:
        print("No accounts found in file.")
        return

    cc.config.set_license('idC+m5GXnIGXlqad0MjQw8fAwtDe0KGRmpefk6SXgNDI0MDQ3tChmYfQyNCil4CBnZyTntKigJ2Ul4GBm52ck57Q3tCkk56blpOGl7SAnZ/QyNDAwsDG38LE38DApsPByMLFyMPC3MLCysrGy8qo0N7QpJOem5aThpemndDI0MDCwMbfwsXfwMCmw8HIwsXIw8LcwsLKysbLy6jQ3tC0l5OGh4CXgdDIqYnQvJOfl9DI0L+Tir6dkZOGnYC+m5+bhpfQ3tCkk56Hl9DI0MPKxsbExcbGwsXBxcLLx8fDxMPH0I+vjw==.hn2r9awfekKJpsauAEhL4Q/eAYqNkHY15A+HM2dlb5NtYahobqgMKRa89hJw9bR6Njc+fW9pmNeGvavK0bjILFMEOe/+MY5m7anvfsNY81jkG5GY+6+8Rwvh1tXO/ooi8q83Ibz+x2yJwLHpn8vr5vwpzcxAmXsa8mOCLIjeL4s=')
    tab = cc.edge.open("https://accounts.google.com/lifecycle/steps/signup/name?continue=https://myaccount.google.com?utm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&ddm=0&dsh=S1308871146:1719147752392253&flowEntry=SignUp&flowName=GlifWebSignIn&TL=AC3PFD5EaCfapUT5_Pqimy9-jpLyPW6n70xE8hiiustLhjOLBAY-A3eJfEMPtMEr")

    for account in accounts:
        first_name = account['first_name']
        last_name = account['last_name']
        date_of_birth = account['date_of_birth']
        gender = account['gender']
        lozinka = account['password']
        potvrda = account.get('confirm_password', 'default_password')

        
        
        # Parsiranje datuma rođenja
        day, month, year = datum()

        ime = tab.find_element_by_xpath('//*[@id="firstName"]')
        ime.set_text(first_name)

        prezime = tab.find_element_by_xpath('//*[@id="lastName"]')
        prezime.set_text(last_name)

        gumb = tab.find_element_by_xpath('//*[@id="collectNameNext"]/div/button/div[3]')
        gumb.click()

        # Adding wait time to ensure elements are loaded
        time.sleep(2)

        dan = tab.find_element_by_xpath('//*[@id="day"]')
        dan.set_text(str(day))
        
        godina = tab.find_element_by_xpath('//*[@id="year"]')
        godina.set_text(str(year))
        
        mjesec = tab.find_element_by_xpath('//*[@id="month"]')
        mjesec.select_item(month)
            
        spol = tab.find_element_by_xpath('//*[@id="gender"]')
        spol.select_item('Muškarac')
        
        a1 = tab.find_element_by_xpath('//*[@id="birthdaygenderNext"]/div/button/div[3]').click()
        
        opcija = tab.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[2]/div/div[1]/div/div[3]/div').click()

        #email = account['email'] 
        #email_input = tab.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
        #email_input.set_text(email)
        
        a2 = tab.find_element_by_xpath('//*[@id="next"]/div/button').click()
        
        lozinka = tab.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').set_text(str(lozinka))
        potvrda = tab.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').set_text(str(potvrda))
        prikazi = tab.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/input').click()
        
        a3 = tab.find_element_by_xpath('//*[@id="createpasswordNext"]/div/button/span').click()
        
        telefon = tab.find_element_by_xpath('//*[@id="phoneNumberId"]').set_text("0955807648")
        a4 = tab.find_element_by_xpath('//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/span').click()
        
        
# MAIN FUNKCIJA
if __name__ == "__main__":
    RegistracijaGoogle()