import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python script.py <database1.csv> <sequence1.csv>")
        sys.exit(1)
    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # TODO: Read database file into a variable
    database_data = []
    with open(database_filename) as database_file:
        database_reader = csv.DictReader(database_file)
        for row in database_reader:
            database_data.append(row)
    # print(database_data)

    # TODO: Read DNA sequence file into a variable
    with open(sequence_filename, encoding="utf-8") as sequence_file:
        sequence_reader = sequence_file.read()
    # print(sequence_reader)

    # TODO: Find longest match of each STR in DNA sequence
    # Stripping the 'name' field
    STR = database_reader.fieldnames[1:]
    # Storing values and keys in a dictionary
    STR_data = {}
    # Iterating over all the STR's
    for data in STR:
        STR_data[data] = longest_match(sequence_reader, data)
    # print(STR_data)

    # TODO: Check database for matching profiles
    for person in database_data:
        match = True
        for information in STR:
            if int(person[information]) != STR_data[information]:
                match = False
                break
        if match == True:
            print(person['name'])
    print("No Match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # if sequence_length[i] == subsequence_length[i]:
        # If a match, move substring to next potential match in sequence
        # count += 1
        # return 1 + longest_match(sequence[i-1], subsequence[i-1])
        # Continue moving substring and checking for matches until out of consecutive matches
        # else:
        #     return max(longest_match(sequence[i], subsequence[i-1]), longest_match(sequence[i-1], subsequence[i]))

        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
