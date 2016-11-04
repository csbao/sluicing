#!/usr/bin/python

import sys
import json
import pdb

f = sys.argv[1]
fd = open(f)
content = fd.readlines()

for l in content[1:20]:
    # l = fd.readline()
    obj = json.loads(l)
    out = json.dumps(obj, indent=2)
    # pdb.set_trace()
    print (out)

fd.close()