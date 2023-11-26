from datetime import datetime, timedelta
import random
import string
from random import randint

def verificare_float(nr):
    """
        Verificam daca un numar dat nu este intreg (adica sa aiba parte zecimala)
    """
    return isinstance(nr, float) and not nr.is_integer()

def test_verificare_float():
    assert verificare_float(1.2) == True
    assert verificare_float(1) == False
    assert verificare_float(3.14) == True
    assert verificare_float(-2) == False

def validare_data(data):
    """
        Verificam daca o data este introdusa corect
    """
    try:
        datetime_object = datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def test_validare_data():
    assert validare_data("11/12/2023") == True
    assert validare_data("31/04/2002") == False
    assert validare_data("29/02/2004") == True
    assert validare_data("15/05/2010") == True 

def string_generator(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))

def number_string_generator(size):
    return random.randint(1, size)

def data_generator():
    current_date = datetime.now()

    random_day = randint(1, 28)  
    random_month = randint(1, 12)
    random_year = randint(current_date.year - 10, current_date.year + 10)  # +/- 10 years

    random_date = datetime(random_year, random_month, random_day)

    formatted_date = random_date.strftime("%d/%m/%Y")
    return formatted_date

def ruleaza_teste():
    test_verificare_float()
    test_validare_data()

ruleaza_teste()