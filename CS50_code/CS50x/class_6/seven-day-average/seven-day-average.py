import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines() #splitlines method turns strings into lists splitting using line breaks
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state == "":
            #print('No state entered.')
            break
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    #for i in reader:
        #{'date': '2020-07-12', 'state': 'Arkansas', 'fips': '05', 'cases': '28367', 'deaths': '321'}
            #date   state   fips   cases    deaths

    #We'll use a dict to store data in the form of {'state':[seven-day-data]} for each state and a 7 day period
    new_cases = {}
    prev_cases_dic = {}

    for reg in reader:
        state = reg['state']
        #print(state)

        #finitializing dics
        if new_cases == {}:
            new_cases = {(state): [int(reg['cases'])]}
            prev_cases_dic = {(state): int(reg['cases'])} #considered to record cumulative data as int (not as list)

        #states with rpevious cases
        elif state in list(new_cases):
            #control only 14 cases for each state
            if len(new_cases[state]) == 14:
                prev_cases_list = new_cases[state][1:]
            else:
                prev_cases_list = new_cases[state]

            #calculates cases for new day by substracting previous cumulative data for the state
            new_case = int(reg['cases']) - prev_cases_dic[state] #int(prev_cases_dic[state])
            prev_cases_list.append(new_case)
            new_cases[state] = prev_cases_list
            prev_cases_dic[state] = int(reg['cases']) #updates cumulative data for last date
        else: #current state not yet in new_cases dict => add a new element/state to the dic
            new_cases[state] = [int(reg['cases'])]
            prev_cases_dic[state] = int(reg['cases'])

    #print(new_cases)
    return(new_cases)


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    for state in states:
        #for i in new_cases[state][0:7]
        fst_avg = sum(new_cases[state][0:7]) / 7
        scnd_avg = sum(new_cases[state][7:14]) / 7

        try:
            inc = scnd_avg / fst_avg
        except ZeroDivisionError:
            print("Can't calculate increase for this state")

        if inc < 0:
            print(state, " had a 7-day average of", round(scnd_avg,0) , " and a decrease of ", "{0:.0%}".format(inc), '.' )
        elif inc > 0:
            print(state, " had a 7-day average of", round(scnd_avg,0) , " and an increase of ", "{0:.0%}".format(inc), '.' )
        else:
            print(state, " had a 7-day average of", round(scnd_avg,0), '.' )

main()
