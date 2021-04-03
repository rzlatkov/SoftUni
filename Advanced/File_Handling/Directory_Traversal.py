# Directory Traversal

import os

USER = os.getlogin()
USED_PATH = '/home/rzlatkov/Softuni/Advanced/File_Handling/'  # first level traverse only
ROOT_PATH = './'  # traverse everything
REPORT_PATH_WINDOWS = f'C:\\Users\\{USER}\\Desktop\\report.txt'     # for Win users
REPORT_PATH_LINUX = f'/home/{USER}/Desktop/report.txt'  # I am coding on a Linux (Manjaro)


def traverse(path):
    dictionary_of_files = {}
    path = os.walk(path)
    for _,_, files in path:
        for f in files:
            extension = f[f.index('.'):]
            if not extension in dictionary_of_files:
                dictionary_of_files[extension] = []
            dictionary_of_files[extension].append(f)
    return dictionary_of_files


def sort_extensions(dictionary_of_files):
    return dict(sorted(dictionary_of_files.items(), key=lambda x: x[0]))


def sort_filenames(dictionary_list_values):
    return sorted(dictionary_list_values, key=lambda x: x)


def write_to_report(result, report_path):
    with open(report_path, 'w') as writer:
        for ext, fnames in result.items():
            writer.write(ext + '\n')
            sorted_fnames = sort_filenames(fnames)
            for f in sorted_fnames:
                writer.write(f"- - - {f}\n")


files = traverse(USED_PATH)
sorted_ext = sort_extensions(files)
write_to_report(sorted_ext, REPORT_PATH_LINUX)
