from string import ascii_lowercase

ts = 'a123bc34d8ef34'

cur = []
res = set()

for c in ts:
    if c in ascii_lowercase:
        if cur:
            s = ''.join(cur)
            res.add(int(s))
            cur = []
    else:
        cur.append(c)
else:
    if cur:
        s = ''.join(cur)
        res.add(int(s))

print(res)



