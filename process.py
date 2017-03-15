def store_set(input_set, file_name):
    fw = open(file_name, 'w')
    fw.writelines(input_set)
    fw.close()


list = []
with open("dict.txt", 'r') as infile:
    each_article = infile.readlines()
    for each_sentence in each_article:
        each = each_sentence.split("   ")
        list.append(each[1] + "\n")
        store_set(list, "dict0.txt")