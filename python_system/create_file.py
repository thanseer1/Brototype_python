#!/usr/bin/env python3

import os
import sys

filname=sys.argv[1]

if not os.path.exists(filname):
    with open(filname,"w") as f:
        f.write("create new file")
else:
    print("file exit")  
sys.exit(1)          