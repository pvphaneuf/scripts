import fnmatch
import os
import shutil

root_path = '/data/breseq/'
pattern = 'NC*.overview.png'


def create_file_name(file_path):

    new_file_name = file_path.replace('/data/breseq/', '')
    new_file_name = new_file_name.replace('/', '+')
    
    return new_file_name


coverage_file_list = []

for root, dirs, files in os.walk(root_path):
    for filename in fnmatch.filter(files, pattern):
        coverage_file_list.append(os.path.join(root, filename))

copy_location = '/data/breseq/coverage/'

for coverage_file in coverage_file_list:

    shutil.copyfile(coverage_file, copy_location + create_file_name(coverage_file))
