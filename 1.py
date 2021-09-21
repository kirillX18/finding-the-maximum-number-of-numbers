M = [0,0,0,0,0,0,0,0,0,0]
s = ' '
k = 0
a = 0
print('Введите строку')
s = input(str(s))
for i in s:
    if i == '1':
        M[0] = M[0] + 1
    if i == '2':
        M[1] = M[1] + 1
    if i == '3':
        M[2] = M[2] + 1
    if i == '4':
        M[3] = M[3] + 1
    if i == '5':
        M[4] = M[4] + 1
    if i == '6':
        M[5] = M[5] + 1
    if i == '7':
        M[6] = M[6] + 1
    if i == '8':
        M[7] = M[7] + 1
    if i == '9':
        M[8] = M[8] + 1
    if i == '10':
        M[9] = M[9] + 1
a = max(M)        
for f in M:
    k += 1
    if a == f:
        print(k,a)
        
    
    
    
        
    
    


