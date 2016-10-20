import copy

def sort_list(lista):
    new_list = []
    for i in lista:
        if len(new_list) == 0:
            new_list.append(i)
        else:
            index = len(new_list)-1
            while len(i) < len(new_list[index]):
                index-=1
            new_list.insert(index+1, i)
    return new_list

ori_results = open('vgen_output.txt')

brute_content = ori_results.readlines()

matrix_content = []

for b in brute_content:
    matrix_content.append(b.split())

sorted_matrix_content = sort_list(matrix_content)

array_final = []

for i in sorted_matrix_content:
    array_final.append(' '.join(i))

sorted_result = open('vgen_sorted_output.txt', 'w+')

for i in array_final:
    sorted_result.write(i+"\n")

sorted_result.close()
