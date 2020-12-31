from flask import Flask
from flask import request,Response,Blueprint
from flask import current_app as app
import json
import pymysql
import os
import threading 
from threading import*
import time
d={}
l=[]
app = Flask(__name__)

@app.route("/", methods = ["POST"])
def main():
    reqBody = request.get_json()
    input = reqBody['input']
    #i = input
    while(1):
        print("Select the operation you want to do:\n")
        print("1-Create\n2-Read\n3-Delete\n4-Show all\n5-Exit\n")
        opt=input
        if(opt==1):
            c = create()
            return(c)
        elif(opt==2):
            r = read()
            return(r)
        elif(opt==3):
            d = delete()
            return(d)
        else:
            print("Invalid Operation\n")
    #print(d)
    t1=Thread(target=(create or read or delete)) 
    t1.start()
    time.sleep(1)
    t2=Thread(target=(create or read or delete))
    t2.start()
    time.sleep(1)

    f=open("garvit.txt",'w')
    strc=str(d)
    f.write(strc)
    f=open("garvit.txt",'r')
    print(f.read())
    f.close()


    app.run(debug=True)

@app.route("/create",methods = ["POST"])
def create():
    reqBody = request.get_json()
    key = reqBody['key']
    value = reqBody['value']
    print("Enter the key value pair to add\n")
    #key,value=map(str,input().split())
    #key=int(key)
    print("Time-To-Live property-------Enter the time in minutes\n")
    ti=reqBody['time']
    ti=ti*60
    if key in d:
        return("Error: this key is Already exists:\n")
    else:
        if len(d)<(1024*1024*1024) and len(value)<=(4*1024):
            if ti==0:
                l=[value,ti]
            else:
                l=[value,time.time()+ti]
            if len(key)<32:
                d[key]=l
                return("Successfully Created\n")
            else:
                return("Error: Invalid Key value\n")
        else:
            return("Error: Memory Limit exceed\n") 

@app.route("/read",methods = ["POST"])
def read():
    print("Enter key to read the pair\n")
    reqBody = request.get_json()
    key = reqBody['key']
    #key = int(key)
    res = {}
    if key not in d:
        return("Error: Key does not Exist\n")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                #res=str(key)+":"+str(b[0])
                res[key] = b[0]
                return(res)
            else:
                return("Error: time to live expired\n")
        else:
            #res=str(key)+":"+str(b[0])
            res[key] = b[0]
            return(res)

@app.route("/delete",methods = ["POST"])
def delete():
    print("Enter the key to delete\n")
    reqBody = request.get_json()
    key = reqBody['key']
    #key = int(key)
    if key not in d:
        return("Error: Key does not Exist\n")
    else:
        del d[key]
        return("Successfully deteled\n")


app.run(debug=True)
