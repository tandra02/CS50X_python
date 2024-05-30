from cs50 import get_float


def calculate_quarters(cents):
    quarters = 0
    while cents >= 25: # Cents can't be less than 25
        quarters += 1
        cents -= 25 # Subtract from the cent
    return quarters


def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        dimes += 1
        cents -= 10
    return dimes


def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        nickels += 1
        cents -= 5
    return nickels


def calculate_pennies(cents):
    pennies = 0
    while cents >= 1:
        pennies += 1
        cents -= 1
    return pennies


def main():
    while True:
        change = get_float("Change: ")
        if change > -1: # Changes can't be negative
            break
    cents = round(change * 100)

    quarters = calculate_quarters(cents)
    cents_after_quarters = cents - quarters * 25

    dimes = calculate_dimes(cents_after_quarters)
    cents_after_dimes = cents_after_quarters - dimes * 10

    nickels = calculate_nickels(cents_after_dimes)
    cents_after_nickels = cents_after_dimes - nickels * 5

    pennies = calculate_pennies(cents_after_nickels)

    total_coins = quarters + dimes + nickels + pennies
    print("Total coins:", total_coins)


if __name__ == "__main__":
    main()
