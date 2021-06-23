
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
    
    for Folder, Subfolder, Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:
            print("Subfolder of "+Folder+" is "+sub)
        for file in Filename:
            print("File name is : "+file)
            
            actualpath=os.path.join(Folder,file)
            print('Access time  :', time.ctime(os.path.getatime(actualpath)))
            print('Modified time:', time.ctime(os.path.getmtime(actualpath)))
            print('Change time  :', time.ctime(os.path.getctime(actualpath)))
            print('Size         :', os.path.getsize(actualpath))
            hash=CalculateChecksum(actualpath)
            print("\n")
            #print(hash)
            #print(file+"\t"+time.ctime(os.path.getatime(actualpath))+"\t"+str(os.path.getsize(actualpath)))

def main():
    line=80*'*'
    print(line)
    print("----------------Directory Traversal Script-----------------")
    print("------------------Author: Ganesh M. Mane------------------")
    print(line)
    
    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
        
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("It is a Directory cleaner script")
        exit()
        
    if (argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide the absolute path of target directory")

    DirectoryTraversal(argv[1])

if __name__=="__main__":
    main()