import pandas as pd
import tldextract

# Read the CSV file (assuming the URLs are in the first column)
df = pd.read_csv('urls.csv', header=None)

# Initialize empty lists for domain and subdomain
domains = []
subdomains = []

# Extract domain and subdomain using tldextract
for url in df[0]:
    extracted = tldextract.extract(url)
    if extracted.subdomain:
        subdomains.append(url)
        domains.append(None)
    else:
        subdomains.append(None)
        domains.append(url)

# Create new DataFrame with domain and subdomain columns
result_df = pd.DataFrame({'Domain': domains, 'Subdomain': subdomains})

# Save the results to a new CSV file
result_df.to_csv('output_domains_subdomains.csv', index=False)

print("Separation complete! Results saved to 'output_domains_subdomains.csv'.")
