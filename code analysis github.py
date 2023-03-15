import pandas
import requests
import urllib.request
import re
import webbrowser

df = pandas.read_csv('mosl.csv', usecols=[0])
list2 = [row[0] for row in df.values]
#print(list2)
html_url=[]
for i in range(len(list2)):
    api_url = list2[i]
    response = requests.get(api_url)
    data = response.json()
    html_url.append(data["html_url"])
    #print(data["html_url"])

print("list is: \n")
print(html_url)
