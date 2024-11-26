import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if len(re.sub(r'\D', '', cleaned_number)) < 10:  
        raise ValueError("Невірний формат: замало цифр для номера телефону.")

    if cleaned_number.startswith('0'):  
        cleaned_number = '+38' + cleaned_number
    elif cleaned_number.startswith('8'):  
        cleaned_number = '+3' + cleaned_number
    elif cleaned_number.startswith('3'):  
        cleaned_number = '+' + cleaned_number

    return cleaned_number

print (normalize_phone("       +380 44 123 4567"))