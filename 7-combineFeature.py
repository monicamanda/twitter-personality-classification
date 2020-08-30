import csv
import pandas as pd
from sklearn.preprocessing import StandardScaler 

label = {}
with open('dataset/label-result.csv', 'r') as file:
    i = 0
    for row in file:
        if i == 0:
            i += 1
            continue
        row = row.split(',')
        last = row[len(row)-1].split('\n')
        label[row[0]] = last[0]

emotion = {}
header = ''
with open('dataset/emosent-result.csv', 'r') as file:
    i = 0
    for row in file:
        if i == 0:
            header = row.split('\n')[0]
            header += ',Following,Followers,Retweet,Favorite,Label\n'
            i += 1
            continue
        row = row.split(',')
        last = row[len(row)-1].split('\n')
        row[len(row)-1] = last[0]
        emotion[row[0]] = row[1:]

count = 0
socials = dict()
with open('dataset/crawl-social.csv', 'r') as social:
    for target_list in social:
        if count == 0:
            count += 1
            continue
        temp = target_list.split(',')
        temp[len(temp) - 1] = temp[len(temp) - 1].split('\n')[0]
        
        socials[temp[0]] = {
            'Following': temp[1],
            'Followers': temp[2],
            'Retweet': temp[3],
            'Favorite': temp[4]
        }

matches = {}
count = 0
with open('dataset/final-feature.csv', 'w') as file:
    file.write(header)
    for target_list in emotion:
        if target_list in label:
            if target_list in socials:
                emotion[target_list].append(label[target_list])
                emotion[target_list].insert(0, target_list)
                emotion[target_list][len(emotion[target_list])-1] = socials[target_list]['Following'] + ',' + socials[target_list]['Followers'] + ',' + socials[target_list]['Retweet'] + ',' + socials[target_list]['Favorite'] + ',' + emotion[target_list][len(emotion[target_list])-1] + '\n'
                file.write(','.join(emotion[target_list]))
                count += 1

print("\n- writing to 'dataset/final-feature.csv' complete.")
