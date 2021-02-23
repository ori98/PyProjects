input = [2,4,6,8,9,10,3,12,18]
print(input)

input.append(9999)

temp = []
out = []
rev = []


for inp in input:
    
    
    if inp%2 != 0:
        
        if temp == []:
            out.append(inp)
            continue
        
        temp.reverse()
        rev = temp
        temp = []
        
        for i in rev:
            out.append(i)
        out.append(inp)
        
    
    if inp%2 == 0:

        temp.append(inp)
        
    if inp == 9999 and temp != []:
            temp.reverse()
            rev = temp
            for j in rev:
                out.append(j)
            temp.append(inp)
    
    


out.pop(-1)
print(out)
