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


ori_results = open('sorted_output2.txt')


brute_content = ori_results.readlines()

array_content = []

for b in brute_content:
    array_content.append(b.split())


#organize array sequences by size
#array_content = sort_list(array_content)

#print array_content

i = 0

while i < len(array_content):
    index = i+1
    poped = False
    while index < len(array_content):
        resumed = copy.copy(array_content[i])
        del resumed[-1] # number of support
        del resumed[-1] # #SUP word
        bigger_item = set(array_content[index])
        this_item = set(resumed)
        if this_item.issubset(bigger_item):
            poped = True
            del array_content[i]
            break
        index+=1
    if not poped:
        i+=1

final_content = []

for i in array_content:
    final_content.append(' '.join(i))

output = open('relevant_output.txt2', 'w+')

for i in final_content:
    output.write(i+"\n")

output.close()
