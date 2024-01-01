n = 1
for i in range (0,n):
    Your_mail = input("Enter your gmail : ")
domain=()
users=()
for i in range(0,len(Your_mail)):
    if(Your_mail[i]=='@'):
        domain = Your_mail[i:]
        username = Your_mail[:i]
        i+=1
print("username:-",username)
print("domain:-",domain)