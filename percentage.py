
natural = open('humanized_results_51.csv')

TOTAL_STUDENTS = 492

brute_content = natural.readlines()

matrix_content = []

for b in brute_content:
    matrix_content.append(b.split())


for i in matrix_content:
    foundin = int(i[-1])
    percentage = (foundin * 100)/TOTAL_STUDENTS
    i.append(", "+str(percentage)+"%")

final = open('aux.txt', 'w+')

for i in matrix_content:
    final.write(' '.join(i)+"\n")

final.close()
natural.close()
