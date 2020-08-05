import os

test_list = '/data/Dataset/rec_data/number/train.txt'
save_test_list = '/data/Dataset/rec_data/number/train_list.txt'
with open(test_list, 'r') as f:
    lines = f.readlines()
    for line_index, line in enumerate(lines):
        image_path = line.strip().split(' ')[0]
        # print(image_path)
        ground_truth = image_path.split('.')[0].split('_')[-1]
        # print(image_path,ground_truth)
        write=image_path
        for i in range(len(ground_truth)):
            write = write + " " + ground_truth[i]
        # print(write)
        with open(save_test_list, 'a') as f:
            f.writelines(write+"\n")
