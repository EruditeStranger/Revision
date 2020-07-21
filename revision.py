file = input("Enter file name: ")

f = open(file)

xyz = list()
for line in f:
    line = line.rstrip()
    words = line.split()
    xyz.append(words)
dictionary_of_count = dict()
for abc in xyz:
    for k in abc:
        dictionary_of_count[k] = dictionary_of_count.get(k,0) + 1

rev = list()
for word,count in dictionary_of_count.items():
    newtup = (count,word)
    rev.append(newtup)

rev = sorted(rev,reverse=True)
print(rev)
