for line in open("./data_train1.txt"):
    line1 = line.strip('\n')
    line2 = line1.split('/',10)
    if len(line2) is 11:
        with open('./data_train.txt', 'a') as f:
            f.writelines(line1 + '\n')

for line in open("./data_test1.txt"):
    line1 = line.strip('\n')
    line2 = line1.split('/',10)
    if len(line2) is 11:
        with open('./data_test.txt', 'a') as f:
            f.writelines(line1 + '\n')
