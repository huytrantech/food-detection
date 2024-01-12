from utils import split_datasets

split_datasets(source_dir="datasets", percent=0.025)
split_datasets(source_dir="datasets", percent=0.025,type_dataset="test")
split_datasets(source_dir="datasets", percent=0.025,type_dataset="valid")