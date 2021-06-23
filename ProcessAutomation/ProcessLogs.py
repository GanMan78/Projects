
import os
import time
import psutil
import schedule
from sys import *

def ProcessDisplay(FolderName="LogHistory"):   
    count=0
    Data=[]
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    File_Path=os.path.join(FolderName,"ProcessLog%s.txt"%(time.ctime()))    # os.path.join(FolderName,"Marvellous%s.log"%(time.ctime())) 
    File_Path=(File_Path.replace(" ","").replace(":",""))
    fd=open(File_Path,"w")

    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs=['pid','name','username'])
        Data.append(value)
        count=count+1
    
    for element in Data:
        fd.write("%s\n"% element)
        
    print("Number of current running process :",count)
    return Data

def main():
    count=0
    line=80*'*'
    print(line)
    print("--------------------Current Active Processes-----------------")
    print(line)
    print("Script title : "+argv[0])
        
    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Application_Name Schedule_Time Directory_Name")
        exit()
        
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("Help : It is used to log the running proccesses")
        exit()
    
    schedule.every(int(argv[1])).minutes.do(ProcessDisplay)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()