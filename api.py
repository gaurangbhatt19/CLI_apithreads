import json
import requests
import sys
from colorama import Fore
import threading
from requests.exceptions import HTTPError
from urllib.parse import unquote

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def arguments():
    data={
        "method":"GET",
        "bodyData":"",
        "url":"",
        "resCode":"200",
        "threads":"1",
        "headers":"",
        "delay":"0",
        "-assertion":""
        }
    arguments=sys.argv
    for i in range(len(arguments)):
        if arguments[i]=="-method":
            data["method"]=arguments[i+1]
        elif arguments[i]=="-bodyData":
            data["bodyData"]=arguments[i+1]
        elif arguments[i]=="-headers":
            data["headers"]=arguments[i+1]
        elif arguments[i]=="-url":
            data["url"]=arguments[i+1]
        elif arguments[i]=="-resCode":
            data["resCode"]=arguments[i+1]
        elif arguments[i]=="-threads":
            data["threads"]=arguments[i+1]
        elif arguments[i]=="-delay":
            data["delay"]=arguments[i+1]
                
    return data

def apiGet(url,headers,body,resCode):
    headersFile=open(headers,"r")
    headersData=json.load(headersFile)

    try:
        res=requests.get(url,headers=headersData)
        if str(res.status_code) == resCode:
            print(bcolors.OKBLUE + "Url: "+url+"\n"+bcolors.OKCYAN+"Response: "+json.dumps(res.json())+"\n"+bcolors.WARNING+"Elapsed Time: "+str(res.elapsed)+"\n"+bcolors.OKGREEN+"Result: "+"Passed")
        else:
            print(bcolors.OKBLUE+ url+" "+bcolors.OKCYAN+ json.dumps(res.json())+" "+bcolors.FAIL+"FAILED")

    except HTTPError:
        print(bcolors.FAIL+ "HTTP Error "+str(HTTPError))
    except Exception as err:
        print(bcolors.FAIL+'Other error occurred: '+str(err))

    
def apiPost(url,body,resCode,headers):
    jsonFile=open(body,"r")
    bodyData=json.load(jsonFile)

    headerFile=open(headers,"r")
    headersData=json.load(headerFile)

    # body=body.replace(r"\r","").replace(r"\n","").replace(r"\t","")
    # body=body.replace("\"","'")
    # bodyData=unquote(body)
    # print(bodyData)

    # headersData=json.load(headers)
    try:
        res= requests.post(url,data=bodyData,headers=headersData)
        if str(res.status_code)==resCode:
            print(bcolors.OKBLUE + "Url: "+url+"\n"+bcolors.OKCYAN+"Response: "+json.dumps(res.json())+bcolors.WARNING+"Elapsed Time: "+str(res.elapsed)+"\n"+bcolors.OKGREEN+"Result: "+"Passed")
        else:
            print(bcolors.OKBLUE+ url+" "+bcolors.OKCYAN+ json.dumps(res.json())+" "+bcolors.FAIL+"FAILED")
    except Exception as err:
        print(bcolors.FAIL+'Other error occurred: '+str(err))

    

def tasks(data):
    if data["method"].lower() == "get":
        apiGet(data["url"],resCode=data["resCode"],body=data["bodyData"],headers=data["headers"])
    if data["method"].lower() == "post":
        apiPost(data["url"],resCode=data["resCode"],body=data["bodyData"],headers=data["headers"])

value=arguments()
for i in range(int(value["threads"])):
    th=threading.Timer(int(value["delay"]),tasks,args=(value,))
    th.start()
    th.join()
    

print(Fore.WHITE)