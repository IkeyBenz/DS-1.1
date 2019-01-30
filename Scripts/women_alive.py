import csv

reader = csv.reader(open('../Datasets/titanic.csv', 'r'), 'excel')

# Index of sex: 4
# Index of survival: 1

def check_women_survival():
    count = 0
    for row in reader:
        if row[4] == 'female' and row[1] == '1':
            count += 1
    return count

print('Women who survived:', check_women_survival())