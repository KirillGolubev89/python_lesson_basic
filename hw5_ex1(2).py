import os

path_dir =[('dir_' + str(i + 1)) for  i in range(9)]

for i in path_dir:
    os.rmdir(i)
