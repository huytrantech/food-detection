import shutil
import os
import random


def split_datasets(source_dir, type_dataset="train", percent=1.0):
    train_label_source_dir = "{}/{}/{}".format(source_dir,type_dataset,"labels")
    train_image_source_dir = "{}/{}/{}".format(source_dir,type_dataset, "images")

    train_labels_des_dir = "{}/{}2/{}".format(source_dir, type_dataset,"labels")
    train_images_des_dir = "{}/{}2/{}".format(source_dir, type_dataset,"images")

    all_labels_train = os.listdir(train_label_source_dir)

    num_images_train = int(len(all_labels_train) * percent)

    selected_label_train = random.sample(all_labels_train, num_images_train)

    if not os.path.exists(train_labels_des_dir):
        os.makedirs(train_labels_des_dir)

    if not os.path.exists(train_images_des_dir):
        os.makedirs(train_images_des_dir)

    for label in selected_label_train:
        source_path = os.path.join(train_label_source_dir, label)
        destination_path = os.path.join(train_labels_des_dir, label)
        shutil.copyfile(source_path, destination_path)

        image = label.split(".txt")[0] + ".jpg"
        source_path = os.path.join(train_image_source_dir, image)
        destination_path = os.path.join(train_images_des_dir, image)
        shutil.copyfile(source_path, destination_path)


# split_datasets(source_dir="../datasets", percent=0.1)
# split_datasets(source_dir="../datasets", percent=0.1,type_dataset="test")
# split_datasets(source_dir="../datasets", percent=0.1,type_dataset="valid")
