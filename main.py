import webbrowser

# List of URLs to open
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.github.com",
    # Add more URLs as needed
]

# Function to open URLs
def open_urls(url_list):
    for url in url_list:
        webbrowser.open(url)

# Main function
def main():
    open_urls(urls)

if __name__ == "__main__":
    main()
