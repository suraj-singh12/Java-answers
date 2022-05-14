import os
from distutils.dir_util import copy_tree

def main():
    # get list of all the directories in current working directory
    subDir = next(os.walk('.'))[1]

    # remove unwanted directories
    subDir.remove('.git')
    subDir.remove('AllLectureNotes')

    # destination directory
    dest_dir = 'AllLectureNotes\\'
    dest_dir = os.path.abspath(dest_dir)
    # print(dest_dir)

    for source_dir in subDir:
        source_dir = os.path.abspath(source_dir)
        # copy all files from source->destination dir
        copy_tree(source_dir, dest_dir)
        print('copied directory: ', source_dir)

        # now rename all the files in destination directory 
        # by appending lecture name in front of each file.
        for file in os.listdir(dest_dir):
            old_file = os.path.join(dest_dir, file)
            new_file = os.path.join(dest_dir, source_dir + '_' + file)
            os.rename(old_file, new_file)
        print('success renaming')

if __name__ == "__main__":
    main()