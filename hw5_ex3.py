# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import os
 
destdir = os.path.abspath('destdir')
if not os.path.exists(destdir):
    os.makedirs(destdir)
 
first_file = sys.argv[0]
dirname,filename = os.path.split(__file__)
content = open(__file__).read()
open(os.path.join(destdir,filename),'w').write(content)
