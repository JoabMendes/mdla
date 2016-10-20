import json


with open('dictionary.json') as data_file:
    dictionary = json.load(data_file)


#Read the relev
result = open('spam_relevant_output.txt')

result_content = result.readlines()

humanized = open('humanized/spam_output.csv', "w+")

for result_line in result_content:
    result_line_array = result_line.split(" ")
    print result_line_array
    i = 0
    while i < (len(result_line_array)-1): #Last element is the number of support, it should be not be search on the dictionary
        if result_line_array[i] in dictionary:
            ev_label = dictionary[result_line_array[i]]
            result_line_array[i] = ev_label
        if result_line_array[i] == "-1":
           result_line_array[i] = ","
        i+=1
    print result_line_array

    human_line = ''.join(result_line_array)
    humanized.write(human_line)

humanized.close()
result.close()
data_file.close()
