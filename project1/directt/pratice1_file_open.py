file_place = 'learning_feeling.txt'
with open(file_place)as file1:
    lise = []
    lise = file1.readlines()
    print(file1)
    for line in lise:
        print(line.rstrip())
print('--------------------------------------')
for line in lise:
    print(line.replace('Python','C').rstrip())