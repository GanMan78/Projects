
from sys import*
import os
import hashlib
import time

def CalculateChecksum(path,blocksize=1024):
    fd=open(path,'rb')
    hobj=hashlib.md5()
    
    buffer=fd.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer=fd.read(blocksize)
        
    fd.close()
    return hobj.hexdigest()

def DirectoryTraversal(path):
    print("Contents of the directory are")
    
    duplicate={}        # Directory to hold checksum and filename
    for Folder, Subfolder, Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:
            print("Subfolder of "+Folder+" is "+sub)
        for file in Filename:
            print("File name is : "+file)
            actualpath=os.path.join(Folder,file)
            hash=CalculateChecksum(actualpath)
            
            if hash in duplicate:       # that checksum is already present
                duplicate[hash].append(actualpath)
            else:       #there is no such checksum
                duplicate[hash]=[actualpath]
            
    return duplicate

def DisplayDuplicate(duplicate):
    output=list(filter(lambda x:len(x)>1,duplicate.values()))
    
    if(len(output)>0):
        print("There are duplicate files")
    else:
        print("There are no duplicate files")
        return
    
    print("List of duplicate files are : ")
    icnt=0
    for result in output:
        for path in result:
            icnt+=1
            if icnt>=2:
                print("%s"%path)
        icnt=0

def main():
    line=80*'*'
    print(line)
    print("-----------------Duplicate File Search Script----------------")
    print("---------------------Author: Ganesh M Mane---------------------")
    print(line)
    print("Traversing Directories..")
    time.sleep(3)
    
    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
        
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("It is a Directory cleaner script")
        exit()
        
    if (argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide the absolute path of target directory")

    arr={}
    arr=DirectoryTraversal(argv[1])
    DisplayDuplicate(arr)

if __name__=="__main__":
    main()