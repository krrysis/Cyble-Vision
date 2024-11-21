import csv
from collections import defaultdict

def process_urls(input_file, output_file):
    """
    Processes a CSV file containing URLs and outputs a CSV file with unique domains/subdomains and their counts.

    Args:
        input_file: Path to the input CSV file.
        output_file: Path to the output CSV file.
    """

    domain_counts = defaultdict(lambda: defaultdict(int))

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url = row[0].strip()  # Remove leading/trailing whitespace

            if url:  # Skip empty URLs
                if "://" in url:  # Check if protocol exists
                    domain = url.split("://")[1].split("/")[0]
                else:
                    domain = url.split("/")[0]

                subdomains = domain.split(".")
                top_level_domain = subdomains[-1]

                for subdomain in subdomains:
                    domain_counts[top_level_domain][subdomain] += 1

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain Name", "Subdomains", "Count"])
        for domain, subdomain_counts in domain_counts.items():
            for subdomain, count in subdomain_counts.items():
                writer.writerow([domain, subdomain, count])

if __name__ == "__main__":
    input_file = "input.csv"  # Replace with your input file path
    output_file = "output.csv"  # Replace with your desired output file path
    process_urls(input_file, output_file)
    print(f"Results written to {output_file}")