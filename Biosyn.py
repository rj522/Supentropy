import urllib.request
c=str.upper(input(""))
i=0
a=[]
while i<len(c)-2:
    a.append(''.join(sorted((str(c[i]+c[i+1]+c[i+2])))))
    i+=1

txt=str(urllib.request.urlopen("https://en.wikipedia.org/wiki/DNA_codon_table").read())
d=[]
p=[]
for i in a:
    d.append(txt.index(i, txt.index('<th style="text-align:center;"><b>')))
for i in range(0,len(d)):
    p.append(txt.rindex('<th style="text-align:center;"><b>',0,d[i]))
for i in range(0,len(a)):
    if '/' in txt[txt.index('<b>',p[i],d[i]): txt.index('/b',p[i],d[i])]:
        print(txt[txt.index('/',p[i],d[i])+2],end="")
    
for i in range(len(a)):
    print("\n",p[i],d[i],a[i])

    
        
    

