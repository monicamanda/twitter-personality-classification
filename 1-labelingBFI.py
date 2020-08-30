import csv

formBFI = []

with open('dataset/formulir-bfi.csv', mode='r') as file:
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        line = line.replace('"', '')
        line = line.split(',')[2:]
        formBFI.append(line)

usernames = {}

OCEANnumber = {
    'Extraversion': [1, 6, 11, 16, 21, 26, 31, 36],
    'Agreeableness': [2, 7, 12, 17, 22, 27, 32, 37, 42],
    'Conscientiousness': [3, 8, 13, 18, 23, 28, 33, 38, 43],
    'Neuroticism': [4, 9, 14, 19, 24, 29, 34, 39],
    'Openness': [5, 10, 15, 20, 25, 30, 35, 40, 41, 44]
}

R = [6, 21, 31, 2, 12, 27, 37, 8, 18, 23, 43, 9, 24, 34, 35, 41]
for target in formBFI:
    OCEAN = {
        'Extraversion': 0,
        'Agreeableness': 0,
        'Conscientiousness': 0,
        'Neuroticism': 0,
        'Openness': 0
    }
    for col in range(1, 45):
        if col in OCEANnumber['Extraversion']:
            if int(target[col]) > 3:
                if col not in R:
                    OCEAN['Extraversion'] += 1
        if col in OCEANnumber['Agreeableness']:
            if int(target[col]) > 3:
                if col not in R:
                    OCEAN['Agreeableness'] += 1
        if col in OCEANnumber['Conscientiousness']:
            if int(target[col]) > 3:
                if col not in R:
                    OCEAN['Conscientiousness'] += 1
        if col in OCEANnumber['Neuroticism']:
            if int(target[col]) > 3:
                if col not in R:
                    OCEAN['Neuroticism'] += 1
        if col in OCEANnumber['Openness']:
            if int(target[col]) > 3:
                if col not in R:
                    OCEAN['Openness'] += 1

    OCEAN['Extraversion'] /= len(OCEANnumber['Extraversion']) / 10
    OCEAN['Agreeableness'] /= len(OCEANnumber['Agreeableness']) / 10
    OCEAN['Conscientiousness'] /= len(OCEANnumber['Conscientiousness']) / 10
    OCEAN['Neuroticism'] /= len(OCEANnumber['Neuroticism']) / 10
    OCEAN['Openness'] /= len(OCEANnumber['Openness']) / 10

    OCEAN['Extraversion'] = round(OCEAN['Extraversion'], 2)
    OCEAN['Agreeableness'] = round(OCEAN['Agreeableness'], 2)
    OCEAN['Conscientiousness'] = round(OCEAN['Conscientiousness'], 2)
    OCEAN['Neuroticism'] = round(OCEAN['Neuroticism'], 2)
    OCEAN['Openness'] = round(OCEAN['Openness'], 2)

    OCEAN['Extraversion'] = str(OCEAN['Extraversion'])
    OCEAN['Agreeableness'] = str(OCEAN['Agreeableness'])
    OCEAN['Conscientiousness'] = str(OCEAN['Conscientiousness'])
    OCEAN['Neuroticism'] = str(OCEAN['Neuroticism'])
    OCEAN['Openness'] = str(OCEAN['Openness'])
    usernames[target[0]] = OCEAN

with open('dataset/label-result.csv', mode='w') as file:
    file.write(','.join(['username', 'Extraversion', 'Agreeableness',
                         'Conscientiousness', 'Neuroticism', 'Openness', 'Label\n']))
    for username in usernames:
        usernames[username][max(usernames[username],
                                key=usernames[username].get)]
        file.write(','.join([username, usernames[username]['Extraversion'], usernames[username]['Agreeableness'], usernames[username]['Conscientiousness'],
                             usernames[username]['Neuroticism'], usernames[username]['Openness'], max(usernames[username], key=usernames[username].get)])+'\n')

print("\n- writing to 'dataset/label-result.csv' complete.")