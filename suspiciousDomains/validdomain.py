import csv
import socket

def telnet_domains(file_path):
    with open(file_path, 'r') as f, open('output.csv', 'w', newline='') as out_file:
        reader = csv.reader(f)
        writer = csv.writer(out_file)
        for row in reader:
            domain = row[0]
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((domain, 443))
                if result == 0:
                    print(f"{domain}, Successful")
                    writer.writerow([domain, 'Successful'])
                else:
                    print(f"{domain}, Failed")
                    writer.writerow([domain, 'Failed'])
                sock.close()
            except socket.gaierror:
                writer.writerow([domain, 'Invalid domain name'])
            except socket.timeout:
                writer.writerow([domain, 'Connection timed out'])

if __name__ == '__main__':
    file_path = 'domains.csv'
    telnet_domains(file_path)
