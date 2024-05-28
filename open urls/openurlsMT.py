import csv
import webbrowser
import time
import threading

def open_url(url):
    try:
        # Add "https://" if the URL doesn't have a scheme
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        webbrowser.open_new(url)
        print(f"Opened URL: {url}")
    except Exception as e:
        print(f"Error opening URL {url}: {e}")

if __name__ == "__main__":
    with open('urls.csv', 'r') as f:
        reader = csv.reader(f)
        urls = list(reader)

    if not urls:
        print("No URLs found in the CSV file.")
        exit()

    print(f"Found {len(urls)} URLs in the CSV file.")

    threads = []
    for url in urls:
        thread = threading.Thread(target=open_url, args=(url[0],))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All URLs opened successfully!")
