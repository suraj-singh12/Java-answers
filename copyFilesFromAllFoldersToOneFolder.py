import os

from distutils.dir_util import copy_tree

def main():
    subDir = next(os.walk('.'))[1]
    subDir.remove('.git')
    subDir.remove('AllLectureNotes')
    dest_dir = 'AllLectureNotes\\'
    dest_dir = os.path.abspath(dest_dir)
    print(dest_dir)

    for source_dir in subDir:
        source_dir = os.path.abspath(source_dir)
        print('--------', source_dir, '--------')
        copy_tree(source_dir, dest_dir)

if __name__ == "__main__":
    main()