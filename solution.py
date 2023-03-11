# import pandas

# ##########q1
list_size=['X'*1000+'S', 'M', 'X'*1000+'L']
#print('XXL' in 'XXXL')
n=input()
n=int(n)
list_true=[]
if n>=1 and n<=1000:
    o=input()
    print(o) 
    numbers_str = o.split(' ')
    numbers = [str(x) for x in numbers_str]
    print(numbers)

    for i in range(len(numbers)):
        if numbers[i] in list_size[0] or numbers[i] in list_size[1] or numbers[i] in list_size[2] :
            #print(numbers[i])
            #continue
            list_true.append(True)

        else:
            list_true.append(False)
            #print('No')
        
if False in list_true:
    print('No')
else:
    print('Yes')

# ###################################q1################

