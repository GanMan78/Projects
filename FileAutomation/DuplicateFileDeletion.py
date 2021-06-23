
from sys import*
import os
import hashlib
import time

File_path=""
def CalculateChecksum(path,blocksize=1024):
    fd=open(path,'rb')
    hobj=hashlib.md5()
    
    buffer=fd.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer=fd.read(blocksize)
        
    fd.close()
    return hobj.hexdigest()

def DirectoryTraversal(path,FolderName="Logs"):
    global File_Path
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    File_Path=os.path.join(FolderName,"File_Log%s.txt"%(time.ctime()))    # os.path.join(FolderName,"File_Log%s.log"%(time.ctime())) 
    File_Path=(File_Path.replace(" ","_").replace(":","_"))
    fd=open(File_Path,"w")
    
    print("Checking files..")
    time.sleep(2)
    print("Contents of the directory are")
    fd.write("Contents of the directory are : \n")
    
    duplicate={}        # Directory to hold checksum and filename
    for Folder, Subfolder, Filename in os.walk(path):
        print("Directory name is : "+Folder)
        fd.write("Directory name is : "+Folder+"\n")
        for sub in Subfolder:
            fd.write("Subfolder of "+Folder+" is "+sub+"\n")
        for file in Filename:
            fd.write("File name is : "+file+"\n")
            actualpath=os.path.join(Folder,file)
            hash=CalculateChecksum(actualpath)
            
            if hash in duplicate:       # that checksum is already present
                duplicate[hash].append(actualpath)
            else:       #there is no such checksum
                duplicate[hash]=[actualpath]
            
    return duplicate

def DisplayDuplicate(duplicate):
    fd=open(File_Path,"a")
    output=list(filter(lambda x:len(x)>1,duplicate.values()))
    
    if(len(output)>0):
        print("There are duplicate files")
        fd.write("There are duplicate files \n")
    else:
        print("There are no duplicate files")
        fd.write("There are no duplicate files \n")
        print("Closing the application..")
        print("Check log file for more details")
        return
    
    fd.write("List of duplicate files are : \n")
    icnt=0
    for result in output:
        icnt=0
        for path in result:
            icnt+=1
            if icnt>=2:
                print("Deleting duplicate file..")
                time.sleep(2)
                fd.write("%s\n"%path)
                os.remove(path)
        
    print("Number of duplicate files deleted:",icnt)
    fd.write("Number of duplicate files deleted: "+str(icnt)+"\n")
    print("Process completed..")
    time.sleep(3)
    print("Check log file for more details!!")
def main():
    line=80*'*'
    print(line)
    print("-----------------Duplicate File Deletion Script----------------")
    print("---------------------Author: Ganesh M Mane---------------------")
    print(line)
    print("Script is running...")
    time.sleep(5)
    
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