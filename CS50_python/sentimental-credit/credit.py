import re
from cs50 import get_string


def isValidAmex(credit):
    # Matches numbers that start with "34" or "37"
    Amex_pattern = r'^(34|37)'
    if re.match(Amex_pattern, credit):
        return True
    else:
        return False


def isValidMaster(credit):
    # Matches numbers that start with "51-55"
    Master_pattern = r'^[5][1-5]'
    if re.match(Master_pattern, credit):
        return True
    else:
        return False


def isValidVisa(credit):
    # Matches numbers that start with "4"
    Visa_pattern = r'^[4]'
    if re.match(Visa_pattern, credit):
        return True
    else:
        return False


def every_other_digit(credit):  # 378282246310005
    sum = 0
    # Flag value set to FALSE
    isAlternateDigit = False
    # Turning the string value into a int
    credit = int(credit)
    while credit > 0:
        if isAlternateDigit:
            # To get the last digit
            last_digit = credit % 10
            product = multipleAndSum(last_digit)
            sum += product
        else:
            # When flag value is False
            last_digit = credit % 10
            sum += last_digit
        # To get the every other digit, we need to change the flag value
        isAlternateDigit = not isAlternateDigit
        # To move to the next digit
        credit //= 10
    return sum


def multipleAndSum(last_digit):
    multiply = last_digit * 2
    # if the multiplied digit is a two-digit number subtract them with 9
    if multiply > 9:
        return multiply - 9
    else:
        return multiply


def validate_credit_card(credit):
    length = len(credit)
    if length == 15 and isValidAmex(credit):
        return "AMEX"
    elif length == 16 and isValidMaster(credit):
        return "MASTERCARD"
    elif (length == 13 or length == 16) and isValidVisa(credit):
        return "VISA"
    else:
        return "INVALID"


credit = get_string("Number: ")
sum_every_other_digit = every_other_digit(credit)

card_type = validate_credit_card(credit)

if sum_every_other_digit % 10 != 0 or card_type == "INVALID":
    print("INVALID")
else:
    print(card_type)
