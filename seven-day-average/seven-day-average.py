import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        # Will check if the user input is empty i.e only pressed enter indicating end of the input
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    for row in reader:
        # Storing values to state variable from the row 'state'
        state = row['state']
        # Storing values to date variable from the row 'date'
        date = row['date']
        # Storing values to cases variable from the row 'cases'
        cases = int(row['cases'])

        if state not in previous_cases:
            # Insert the state, cases as a key, value pair
            previous_cases[state] = cases
            # As this state doesn't exist in previous_cases dictionary, the new cases will not have a record
            new_cases[state] = []
            continue

        new_case = cases - previous_cases[state]
        previous_cases[state] = cases
        if state not in new_cases:
            new_cases[state] = []
        if len(new_cases[state]) >= 14:
            new_cases[state].pop(0)  # Keep only the most recent 14 days
        new_cases[state].append(new_case)
        # previous_cases[state] = cases  # Update previous cases for next iteration

    return new_cases



# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        # Last 7 elements from the states
        recent_week = new_cases[state][7:]
        # First 7 elements from the states
        last_week = new_cases[state][:7]
        avg_recent_week_cases = round(sum(recent_week) / 7)
        avg_last_week_cases = round(sum(last_week) / 7)
        diff_between_cases = avg_recent_week_cases - avg_last_week_cases
        abs_diff_between_cases = abs(diff_between_cases)

        if diff_between_cases > 0:
            # Positive difference means an increase
            msg = 'an increase of'
        else:
            # Negative difference means a decrease
            msg = 'a decrease of'

        try:
            percent = round((abs_diff_between_cases / avg_last_week_cases) * 100, 2)
        except ZeroDivisionError:
            raise ZeroDivisionError

        print(f"{state} had a 7-day average of {abs_diff_between_cases} and {msg} {percent}%.")


main()
