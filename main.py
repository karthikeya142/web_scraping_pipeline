import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())  # Print the HTML content for debugging

    table = soup.find('table')

    if table is None:
        print("No table found on the webpage.")
        return []

    headers = [header.text for header in table.find_all('th')]
    data = []
    for row in table.find_all('tr')[1:]:
        values = [col.text for col in row.find_all('td')]
        if values:
            data.append(dict(zip(headers, values)))

    return data


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'  # Use a sample URL with a known table structure
    scraped_data = fetch_data(url)
    print(scraped_data)
