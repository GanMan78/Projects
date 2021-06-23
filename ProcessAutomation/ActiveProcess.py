
import psutil
from sys import *

def ProcessDisplay():
    print("List of running proccesses")
    
    Data=[]
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs=['pid','name','username'])
        Data.append(value)
    return Data

def main():
    count=0
    line=80*'*'
    print(line)
    print("--------------------Current Active Processes-----------------")
    print(line)
    print("Script title : "+argv[0])
    
    print(arr)
    for element in arr:
        print(element)
        count=count+1
    
    print("Number of current running process :",count)

if __name__=="__main__":
    main()