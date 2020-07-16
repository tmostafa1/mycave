from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
#print(*[(list(c)) for k, c in groupby(input())]) #c returns how many times each key and k is the key




#key_funct=lambda x: (count+=1 for x in s if s[x]==s[x+1])
#for k, g in itertools.groupby(s, key_funct):
 #   print(k, list(g))