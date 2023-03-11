import pandas
##########q1
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

###################################q1################

############################q2###########################
n=input()
errorCodes=[]
for i in range(int(n)):

    file=input()
    filespl=file.split(' ')
    print(filespl)
    allValid = True
    isValid=filespl[1]
    isValid=isValid.capitalize()


    #print(isValid)

   

    #allValid = record.isValid
    if isValid =='True':
        allValid=True

    else:
        errorCodes.append (filespl[2])
        allValid=False
            

    if allValid=='True':
        print ("Yes")
    else:
        print( "No")
        print(errorCodes)


##############q3


