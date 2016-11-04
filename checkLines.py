import json

fname = 'July07_15_lines'

fh = open(fname)

lines = []
for l in fh:
    j = json.loads(l)
    import pdb; pdb.set_trace()
    lines.append(str(j["metadata"]["line"]))

fh.close()

print (sorted(lines))
