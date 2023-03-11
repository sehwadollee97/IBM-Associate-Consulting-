
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


#############q3