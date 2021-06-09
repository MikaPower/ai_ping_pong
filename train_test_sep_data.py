import os
import pandas as pd
import random
from shutil import copyfile


def create_test_and_train_sets():
    path = 'datasets/createML/slow_&_fast_backup_with_cut_movements/classes/'
    train_path = 'datasets/createML/slow_&_fast_dataset_with_cut_movements_separated/train/'
    test_path = 'datasets/createML/slow_&_fast_dataset_with_cut_movements_separated/test/'
    mov_dir = os.listdir(path)
    for mov in mov_dir:
        files = os.listdir(path + mov)
        random.shuffle(files)
        to_remove = int(len(files) * 0.20)
        test = files[0:to_remove]
        train = files[to_remove:]
        for file in train:
            copyfile(path+mov+'/'+file,  train_path+mov+'/'+file)
        for file in test:
            copyfile(path+mov+'/'+file,  test_path+mov+'/'+file)



if __name__ == "__main__":
    create_test_and_train_sets()
