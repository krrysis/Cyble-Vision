import csv
import requests
import webbrowser

black = 0
with open('mosl.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        response = requests.get(url)
        json_data = response.json()
        if 'html_url' in json_data:
            html_url = json_data['html_url']
            webbrowser.open_new_tab(html_url)
            black+=1
            print(black)
            
        else:
            #print(f"No 'html_url' key found in JSON response for URL: {url}")
            pass