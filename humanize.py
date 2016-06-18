

dic = open('dictionary.json')

#Read dictionay file
brute_content = dic.readlines()

#Create dictionay on memory
dictionary = {}

for line in brute_content:
    a = line.split("=")
    dictionary[a[0].replace("'", "")] = a[1].replace("\n", "")

#print dictionary

#Read the relev
result = open('relevant_results_50.txt')

result_content = result.readlines()


humanized = open('humanized_results_50.csv', "w+")

for result_line in result_content:
    result_line_array = result_line.split()
    i = 0
    while i < (len(result_line_array)-1): #Last element is the number of support, it should be not be search on the dictionary
        print result_line_array[i] in dictionary
        if result_line_array[i] in dictionary:
            ev_label = dictionary[result_line_array[i]]
            print ev_label
            result_line_array[i] = ev_label
        if result_line_array[i] == "-1":
           result_line_array[i] = ","
        i+=1

        print result_line_array
    human_line = ' '.join(result_line_array)
    humanized.write(human_line+"\n")
