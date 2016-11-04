import json
import sys
import pdb

args = sys.argv
fin = args[-1]

F = open(fin, "r")
print fin
for l in F:
	try:
		j = json.loads(l)
		file = j["metadata"]["file"]
		line = j["metadata"]["line"]
		sent = j["match"]["sentence"]["string"]
		V = j["match"]["govV"]["string"]
		sluice = j["match"]["sluice"]["string"]
		if "%s %s" % ("n't", V) in sent or "%s %s" % ("not", V) in sent:
		    neg = "Neg"
		else:
		    neg = "No"
		
		print "%s\t%s\t%s\t%s\t%s %s" % (V, sluice, neg, sent, file, line)
	except:
		pass
