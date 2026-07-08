import datetime

num = 0
dictInfos = {'Name':[],'Day':[],'Month':[],'Year':[]}
def DateNameInfo(name = 'none', day = 'none', month = 'none', year = 'none'):
    dictInfos['Name'].append(name)
    dictInfos['Day'].append(day)
    dictInfos['Month'].append(month)
    dictInfos['Year'].append(year)

def usergatheringinfo():
    global num
    while True:
        name = input("Enter person Name: ")
        day = input("Enter person Day: ")
        month = input("Enter person Month: ")
        year = input("Enter person Year: ")
        num = num + 1
        DateNameInfo(name, day, month, year)
        cont = input("Want to continue? [y/n]: ")
        if cont == 'n':
            break
        elif cont != 'y':
            while cont != 'y' and cont != 'n':
                cont = input("Invalid input, Want to continue? [y/n]: ")
            if cont == 'n':
                break

def CheckDateValidity():
    global num
    filtered_dictInfos = {'Name': [], 'Day': [], 'Month': [], 'Year': []}

    for i in range(0, num):
        day = int(dictInfos['Day'][i])
        month = int(dictInfos['Month'][i])
        year = int(dictInfos['Year'][i])
        if 1 <= day <= 31 and 1 <= month <= 12 and int(datetime.datetime.now().strftime('%Y')) - 100 <= year <= int(datetime.datetime.now().strftime('%Y')):
            filtered_dictInfos['Name'].append(dictInfos['Name'][i])
            filtered_dictInfos['Day'].append(day)
            filtered_dictInfos['Month'].append(month)
            filtered_dictInfos['Year'].append(year)
        else:
            print("Invalid Date for {} name".format(dictInfos['Name'][i]))
    dictInfos.update(filtered_dictInfos)

def calculateage(i):
    global dictInfos
    age = int(datetime.datetime.now().strftime('%Y')) - int(dictInfos['Year'][i])
    if int(datetime.datetime.now().strftime('%m'))  < int(dictInfos['Month'][i]):
        return age - 1
    elif int(datetime.datetime.now().strftime('%m')) == int(dictInfos['Month'][i]):
        if int(datetime.datetime.now().strftime('%d')) <= int(dictInfos['Day'][i]):
            return age - 1
        else:
            return age
    else:
        return age

def printdates():
    global dictInfos
    global sortedages
    sorted_dictInfos = {'Name': [], 'Day': [], 'Month': [], 'Year': []}
    if len(dictInfos['Name']) == 1:
        date = datetime.date(dictInfos['Year'][0], dictInfos['Month'][0], dictInfos['Day'][0])
        print('there is no oldest or youngest person')
        print('{} is {} years old and hes/she was born on {}'.format(dictInfos['Name'][0], calculateage(0), date.strftime('%A')))
        print('Total People: {}'.format(len(dictInfos['Name'])))
    elif len(dictInfos['Name']) > 1:
        sortedages = []
        templist = []
        for i in range(0, len(dictInfos['Name'])):
            sortedages.append(calculateage(i))
            templist.append(calculateage(i))
        for i in range(0, len(dictInfos['Name'])):
            maxage = max(templist)
            tempmaxage = templist.index(maxage)
            supporttemplist = templist.copy()
            templist = sortedages.copy()
            maxage_index = templist.index(maxage)
            templist = supporttemplist.copy()
            sorted_dictInfos['Name'].append(dictInfos['Name'][maxage_index])
            sorted_dictInfos['Day'].append(dictInfos['Day'][maxage_index])
            sorted_dictInfos['Month'].append(dictInfos['Month'][maxage_index])
            sorted_dictInfos['Year'].append(dictInfos['Year'][maxage_index])
            del templist[tempmaxage]
        sortedages.sort(reverse=True)
        dictInfos.update(sorted_dictInfos)
        for i in range(0, len(dictInfos['Name'])):
            date = datetime.date(dictInfos['Year'][i], dictInfos['Month'][i], dictInfos['Day'][i])
            print('{} is {} years old and hes/she was born on {}'.format(dictInfos['Name'][i], sortedages[i], date.strftime('%A')))
        print('The oldest one is {}'.format(dictInfos['Name'][0]))
        print('The youngest one is {}'.format(dictInfos['Name'][-1]))
        print('Total People: {}'.format(len(dictInfos['Name'])))

def filewrite():
    global dictInfos
    global sortedages
    file = open('data.txt', 'w')
    for i in range(0, len(dictInfos['Name'])):
        file.write("{} is {} years old".format(dictInfos['Name'][i], sortedages[i]) + '\n')
    file.close()

def fileread():
    global dictInfos
    file = open('data.txt', 'r')
    print(file.read())
    file.close()


try:
    usergatheringinfo()
    CheckDateValidity()
    assert len(dictInfos['Name']) != 0
    printdates()
except AssertionError:
    print("No valid data found, program terminated")
except ValueError:
    print("incorrect user data type input, program terminated")
else:
    filewrite()
    fileread()
finally:
    print("End of program")
