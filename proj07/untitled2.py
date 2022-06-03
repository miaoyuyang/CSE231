name = input("Input a name: ")
for i,ch in enumerate(name):
    if ch ==',':
        print(name[i+2].upper()+' '+name[:i].capitalize())
