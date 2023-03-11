import pandas

list_size=['X'*1000+'S', 'M', 'X'*1000+'L']
#print('XXL' in 'XXXL')
n=input()
n=int(n)

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
            print('Yes')

        else:
            print('No')
        




############################q2
# n=input()
# errorCodes=[]
# for i in range(int(n)):

#     file=input()
#     filespl=file.split(' ')
#     print(filespl)
#     allValid = True
#     isValid=filespl[1]
#     isValid=isValid.capitalize()


#     #print(isValid)

   

#     #allValid = record.isValid
#     if isValid =='True':
#         allValid=True

#     else:
#         errorCodes.append (filespl[2])
#         allValid=False
            

#     if allValid=='True':
#         print ("Yes")
#     else:
#         print( "No")
#         print(errorCodes)


##############q3


