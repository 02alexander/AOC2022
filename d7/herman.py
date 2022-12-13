s,p={},()
for l in open(0):
 if".."in l:p=p[1:]
 elif"d "in l:s[p:=(l,*p)]=0
 k=p
 while"/"<l<":"and k:s[k]+=int(l.split()[0]);k=k[1:]
v=s.values()
print(sum(t for t in v if t<=1e5),min(t for t in v if t>=max(v)-4e7))