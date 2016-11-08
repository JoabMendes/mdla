import json


def frequency_percentage(support):
    total_sequences = 3201
    frequency = str(int(support * 100 / total_sequences))
    return frequency


with open('dictionary.json') as data_file:
    dictionary = json.load(data_file)


#Read the relev
result = open('gap_4/relevant_output.txt')

result_content = result.readlines()

humanized = open('gap_4/humanized_output.csv', "w+")

for result_line in result_content:
    result_line_array = result_line.split(" ")
    i = 0
    while i < (len(result_line_array)-1): #Last element is the number of support, it should be not be search on the dictionary
        if result_line_array[i] in dictionary:
            ev_label = dictionary[result_line_array[i]]
            result_line_array[i] = ev_label
        if result_line_array[i] == "-1":
           result_line_array[i] = ","
        i+=1
    support = result_line_array[-1]
    result_line_array[-1] = result_line_array[-1].rstrip() + " " + frequency_percentage(int(support)) + "%"

    human_line = ''.join(result_line_array)
    humanized.write(human_line+"\n")

humanized.close()
result.close()
data_file.close()
