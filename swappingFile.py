def swapFileData():
    file1Name=input('What is the name of the first file? ')
    file2Name=input('What is the name of the second file? ')

    file1=open(file1Name,'r')
    file2=open(file2Name,'r')
    file1Data=file1.read()
    file2Data=file2.read()

    a=open(file1Name,'w')
    a.write(file2Data)

    b=open(file2Name,'w')
    b.write(file1Data)

    print('You are the most tricky person in the world!!!')

swapFileData()