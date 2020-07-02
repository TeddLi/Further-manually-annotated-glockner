import csv

premise = []
hypothsis = []
label = []
label_dict = {'strict_entailment':0, 'Paraphrasing':1}

with open('Manually_annotated_glockner.csv', mode='r') as csv_f:
    employee_writer = reader = csv.reader(csv_f)
    for row in reader:
        premise.append(row[0])
        hypothsis.append(row[1])
        label.append(label_dict[row[2]])

with open('premise.txt','w') as f1:
    for line in premise:
        f1.write(line)
        f1.write('\n')

with open('hypothesis.txt', 'w') as f2:
    for line in hypothsis:
        f2.write(line)
        f2.write('\n')

with open('label.txt', 'w') as f3:
    for line in label:
        f3.write(str(line))
        f3.write('\n')
