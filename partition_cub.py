# partition_cub.py
# Dan Popp
# 12/06/21
#
# File to partition the CUB-200 dataset
import os
import shutil

from tqdm import tqdm

DATA_DIR = '/home/poppfd/data/CUB-200-2011/CUB_200_2011'


def create_dir(path):
    """
    Creates the directory if it doesn't already exist
    """
    if not os.path.isdir(path):
        os.mkdir(path)


def main():
    dataset_dir = os.path.join(DATA_DIR, 'dataset_dir')
    create_dir(dataset_dir)
    test_dir = os.path.join(dataset_dir, 'test')
    train_dir = os.path.join(dataset_dir, 'train')
    create_dir(test_dir)
    create_dir(train_dir)

    # Load image ID dict
    image_dict = {}
    image_id_file = os.path.join(DATA_DIR, 'images.txt')
    with open(image_id_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            tokens = line.split(' ')
            id = int(tokens[0])
            filename = tokens[1]
            image_dict[id] = filename

    # Create Class Directories
    class_file = os.path.join(DATA_DIR, 'classes.txt')
    class_dict = {}
    with open(class_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            tokens = line.split(' ')
            class_dict[int(tokens[0])] = tokens[1]
            path = os.path.join(test_dir, tokens[1])
            create_dir(path)
            path = os.path.join(train_dir, tokens[1])
            create_dir(path)

    # Create test and train split
    split_file = os.path.join(DATA_DIR, 'train_test_split.txt')
    raw_images = os.path.join(DATA_DIR, 'images')
    train_split_dict = {}
    with open(split_file, 'r') as file:
        lines = file.readlines()
        for line in tqdm(lines):
            line = line.strip()
            tokens = line.split(' ')
            image_id = int(tokens[0])
            train_split_dict[image_id] = int(tokens[1]) == 1

    # Load class label file
    class_file = os.path.join(DATA_DIR, 'image_class_labels.txt')
    image_class_dict = {}
    with open(class_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            tokens = line.split(' ')
            id = int(tokens[0])
            class_id = int(tokens[1])
            image_class_dict[id] = class_id

    # Copy the files over properly
    for image_id in tqdm(image_dict):
        filename = os.path.join(raw_images, image_dict[image_id])
        is_train = train_split_dict[image_id]
        class_id = image_class_dict[image_id]
        class_name = class_dict[class_id]
        out_dir = train_dir if is_train else test_dir
        out_dir = os.path.join(out_dir, class_name)
        shutil.copy(filename, out_dir)


if __name__ == '__main__':
    main()
