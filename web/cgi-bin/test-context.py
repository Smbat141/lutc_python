#!/usr/bin/python3

import languages2common                      # from my dir
f = open('test-context-output.txt', 'w')     # in .. server dir
f.write(languages2common.inputkey)
f.close()
print('context-type: text/html\n\nDone.\n')
import pathlib, os

print(pathlib.Path(__file__).parent.resolve())
print(os.getcwd())


