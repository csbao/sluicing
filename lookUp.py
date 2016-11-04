#!/usr/bin/python

from nltk.tree import ParentedTree

def prettyS(obj):
    tree = ParentedTree.fromstring(obj["tree"])
    # print(tree)
    return tree.pprint()

def prettify(li):
    out = ""
    # for i in li:
    #     print(i["tree"])
    res = map(prettyS, li)
    print(res)
    return '\n\n'.join(res)

if __name__ == '__main__':
    import sys
    
    args = sys.argv
    
    f = args[-1]
    lookin = "allSluices.jsons"
    
    import json
    
    fd = open(lookin, "r")
    for l in fd:
        # if '"line": ' + str(f) in l:
            obj = json.loads(l)
            ls = []
            ls.append(obj["before"][-1])
            ls.append(obj["match"]["sentence"])
            ls.append(obj["after"][0])
            prettify(ls)
            # print (prettify(ls))
            print ("hello")