import csv
import webbrowser

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

    for url in urls:
        if url:
            open_url(url[0])
        else:
            print("Empty URL encountered.")  # Debugging line

    print("All URLs opened successfully!")
