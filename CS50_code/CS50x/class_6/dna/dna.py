import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python tournament.py [csv-file with STR counts] [txt-file with DNA sequence to identify]")
        sys.exit()

    # TODO: Read database file into a variable
    STR_counts = sys.argv[1]
    with open(STR_counts) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ",") #delivers a Dic

        #structure of file: name,AGATC,AATG,TATC
        indiv_dna = []
        for i in csv_reader:
            new_value = {'name': i['name'],'AGATC': int(i['AGATC']),'AATG': int(i['AATG']), 'TATC': int(i['TATC'])}
            indiv_dna.append(new_value)

    #print(indiv_dna)

    # TODO: Read DNA sequence file into a variable
    DNA_seq_file = sys.argv[2]
    with open(DNA_seq_file, 'r') as file:
        dna_seq = file.read().rstrip()

    #print(dna_seq)

    # TODO: Find longest match of each STR in DNA sequence
    subseq_count = {'AGATC': 0,'AATG':0,'TATC':0}

    #print('AGATC: ', longest_match(dna_seq, 'AGATC'))
    #print('AATG: ', longest_match(dna_seq, 'AATG'))
    #print('TATC: ', longest_match(dna_seq, 'TATC'))

    for i in subseq_count:
        #print(sub, ": ", longest_match(dna_seq, sub))
        subseq_count[i] = longest_match(dna_seq, i)

    #print(subseq_count)

    # TODO: Check database for matching profiles
    name = ""
    for people in indiv_dna:
        if (subseq_count['AGATC'] == people['AGATC']) and \
          (subseq_count['AATG'] == people['AATG']) and \
           (subseq_count['TATC'] == people['TATC']) :

            name = people['name']
            print(people['name'])

    if name == "":
        print("No match")

    return name


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
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
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
