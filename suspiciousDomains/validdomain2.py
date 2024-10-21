import csv
import requests

def check_domains(file_path):
    with open(file_path, 'r') as f, open('output.csv', 'w', newline='') as out_file:
        reader = csv.reader(f)
        writer = csv.writer(out_file)
        for row in reader:
            domain = row[0]
            try:
                response = requests.get(f"http://{domain}", timeout=5)
                if response.status_code == 200:
                    print(f"{domain}, Successful")
                    writer.writerow([domain, 'Successful'])
                else:
                    print(f"{domain}, Responded with status code {response.status_code}")
                    writer.writerow([domain, f"Responded with status code {response.status_code}"])
            except requests.exceptions.RequestException:
                writer.writerow([domain, 'Failed'])

if __name__ == '__main__':
    file_path = 'domains.csv'
    check_domains(file_path)
