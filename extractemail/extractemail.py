import re

# Define the input and output file paths
input_file_path = "data.txt"
output_file_path = "emails.txt"

# Regular expression pattern to match email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Read the input file and extract email addresses
with open(input_file_path, "r") as in_file:
    content = in_file.read()
    emails = re.findall(email_pattern, content)

# Write extracted email addresses to the output file
with open(output_file_path, "w") as out_file:
    for email in emails:
        out_file.write(email + "\n")

print(f"Email addresses extracted from {input_file_path} and saved to {output_file_path}.")
