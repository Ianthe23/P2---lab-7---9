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
    
def quicksort_1(arr, key=None):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if (key(x) if key else x) < (key(pivot) if key else pivot)]
        right = [x for x in arr[1:] if (key(x) if key else x) >= (key(pivot) if key else pivot)]
        sorted_arr = quicksort_1(left, key=key) + [pivot] + quicksort_1(right, key=key)

    return sorted_arr

def quicksort_2(arr, key=None, reverse=False, cmp=None):

    sorted = quicksort_1(arr, key=key)
    if reverse:
        sorted.reverse()

    if cmp:
        sorted.sort(cmp=cmp)

    return sorted

def gnomesort(arr, key=None, reverse=False, cmp=None):
    i = 0
    n = len(arr)

    while i < n:
        if i == 0 or (key(arr[i]) if key else arr[i]) >= (key(arr[i - 1]) if key else arr[i - 1]):
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    if reverse:
        arr.reverse()

    if cmp:
        arr.sort(cmp=cmp)

    return arr

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

def test_quicksort():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = quicksort_2(my_list, key=lambda x: x, reverse=True)
    assert sorted_list == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def test_gnomesort():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = gnomesort(my_list, key=lambda x: x, reverse=True)
    assert sorted_list == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def ruleaza_teste():
    test_verificare_float()
    test_validare_data()
    test_quicksort()
    test_gnomesort()

ruleaza_teste()