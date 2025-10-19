# 用途：随机划分数据集（源文件目录仅包含所有数据的图片和标签，创建一个新的文件夹包含图片和标签，每一项下都有 train ,val,test三个目录）

import random
import shutil
from pathlib import Path

split = {'train': 0.7, 'val': 0.2, 'test': 0.1}
dataset = 'E:/Car_Dataset(in and out)/new_cardata/images/'
dataset_labels = 'E:/Car_Dataset(in and out)/new_cardata/labels/'
new_dataset = 'C:/Users/10038/Desktop/dataset/images/'
new_dataset_labels = 'C:/Users/10038/Desktop/dataset/labels/'
names = []
for data in Path(dataset).iterdir():
    names.append(data.stem)
random.shuffle(names)

train_num = int(split['train'] * len(names))
val_num = int(split['val'] * len(names))
test_num = len(names) - train_num - val_num

print("训练集图片：{}张".format(train_num))
print("验证集图片：{}张".format(val_num))
print("测试集图片：{}张".format(test_num))

for ii in [new_dataset,new_dataset_labels]:
    for iii in ['train/','val/' ,'test/'] :
        path = ii + iii
        if not Path(path).exists():
            Path(path).mkdir(exist_ok = True,parents = True)

i = 0
for name in names:
    data_image = dataset + str(name) + '.jpg'
    data_image_label = dataset_labels + str(name) + '.txt'

    if i < train_num:
        data_new_image = new_dataset + 'train/' + str(name) + '.jpg'
        data_new_label = new_dataset_labels + 'train/' + str(name) + '.txt'
        shutil.move(data_image, data_new_image)
        shutil.move(data_image_label, data_new_label)
    elif i > train_num and i < train_num + val_num:
        data_new_image = new_dataset + 'val/' + str(name) + '.jpg'
        data_new_label = new_dataset_labels + 'val/' + str(name) + '.txt'
        shutil.move(data_image, data_new_image)
        shutil.move(data_image_label, data_new_label)
    else:
        data_new_image = new_dataset + 'test/' + str(name) + '.jpg'
        data_new_label = new_dataset_labels + 'test/' + str(name) + '.txt'
        shutil.move(data_image, data_new_image)
        shutil.move(data_image_label, data_new_label)
    i = i + 1
    print("正在处理第{}张图片".format(i))
