from datetime import datetime
import matplotlib.pyplot as plt

# This program takes data from a csv file taken from covid19india.org containing daily covid data
# from 1st Feb 21 to 11th Apr 21.
# This takes and displays data for different states

class state(object):
    def __init__(self, code):
        self.code = code
        self.hosp, self.recov = getData(self.code)
    def show(self):
        return show(self)


def getData(code):
    f = open("data.csv", "r")
    next(f) # Skipping the first line containing titles.

    # Dicitionaries for new cases and recoveries to be saved with date as key.
    hosp = {}
    recov = {}

    while True:
        try: # To tackle inconsistencies in data
            data = f.readline().split(",")
        except:
            continue

        try: # To tackle inonsistent patient numbers.
            if int(data[0]) == 548519:
                break
            elif int(data[0]) >= 548519:
                continue
        except:
            continue

        if str(data[8]) == code:
            dateObj = datetime.strptime(str(data[2]).strip(), '%d/%m/%Y')
            if str(data[10]) == "Hospitalized":
                if dateObj in hosp:
                    hosp[dateObj] += int(data[9])
                else:
                    hosp[dateObj] = int(data[9])
            elif str(data[10]) == "Recovered":
                if dateObj in recov:
                    recov[dateObj] += int(data[9])
                else:
                    recov[dateObj] = int(data[9])
            else:
                continue
        
    
    return hosp, recov


def show(state):
    plt.plot(state.hosp.keys(), state.hosp.values(), "-.r", label = "New Cases")
    plt.plot(state.recov.keys(), state.recov.values(), "-.g", label = "Recovery")
    plt.ylabel("Daily number of cases")
    plt.xlabel("Time ->")
    plt.title("New Covid Cases vs Recoveries in " + state.code)
    plt.legend()
    plt.show()

stateCodes = ("BR", "DL", "MH", "UP")
states = []
for code in stateCodes:
    states.append(state(code))

for state in states:
    state.show()

