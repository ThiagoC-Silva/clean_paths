import os
from .data_paths import folders_list
from .data_paths import file_list


def create_directories(DIRECTORIES):
    directories_list = []
    for folder in folders_list:
        directories_path = os.path.join(DIRECTORIES, folder)
        os.makedirs(directories_path, exist_ok = True)
        directories_list.append(directories_path)
    return directories_list


def create_files(directories_list):
    files_paths_list = []
    for folder, file in zip(directories_list, file_list):
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as file:
            pass
        files_paths_list.append(file_path)
    return files_paths_list