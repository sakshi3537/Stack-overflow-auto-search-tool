import subprocess
import requests
import webbrowser

def getError(cmd):
    args=cmd.split()
    proc=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=proc.communicate()
    return out,err

def makeRequest(error):
    response=requests.get("https://api.stackexchange.com/" + "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    return response.json()

def openUrls(response):
    count=0
    url=[]
    for x in response['items']:
        if x['is_answered']:
            url.append(x['link'])
            count+=1
        if count==3 or count==len(response['items']):
            break
    
    for x in url:
        webbrowser.open(x)

out,err=getError("python <file_path>")
errorTypeAndMessege=err.decode('utf-8').strip().split("\n")[-1]

if errorTypeAndMessege:
    response=makeRequest(errorTypeAndMessege)
    openUrls(response)
else:
    print("No errors found")