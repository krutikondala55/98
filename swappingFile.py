def swapFileData():

    filename=input("Enter the file name:")
    
    file1 =open(filename,'r')

    file2 = open(filename,'r')
    
    file1 = open(filename,'w')
    
    file2 = open(filename,'w')
    

swapFileData()