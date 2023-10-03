import csv
import webbrowser
import time
i=1
with open('urls.csv', 'r') as f:
    reader = csv.reader(f)
    urls = list(reader)

for url in urls:
    webbrowser.open_new(url[0])
    print(i)
    i+=1
    time.sleep(2)