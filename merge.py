import json
import sys
def merge(a, b, key):  #i have done asking for the key
    merge = {}
    for item in a+b:
        if item[key] in merge:
          merge[item[key]].update(item)
        else:
          merge[item[key]] = item
    return [val for (_, val) in merge.items()]
    

with open(sys.argv[1],'r') as a:
    with open(sys.argv[2],'r') as b:
        f1=json.load(a)
        f2=json.load(b)
with open(sys.argv[3], 'w') as f:
          json.dump(merge(f1 ,f2, "id"),f,sort_keys=True)
