mytext="mwembe tayari kenyayyyy"
mynum=len(mytext)
newtext=[""]
final=""
for i in mytext:
    x=int(mynum)-1
    newtext.append(mytext[x])
    mynum=mynum-1
    
for k in range(len(newtext)):
    
    final=final + newtext[k]

print(final)