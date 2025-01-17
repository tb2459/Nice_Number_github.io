import requests
from bs4 import BeautifulSoup

# URL of the ESPN NFL scoreboard page
url = "https://www.espn.com/nfl/scoreboard/_/week/3/year/2024/seasontype/2"

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the webpage content
response = requests.get(url, headers=headers)

# Print the status code and response content for debugging
print(f"Status Code: {response.status_code}")
print(response.content[:500])  # Print the first 500 characters of the response content
json_data = response.json()
print(json_data)


if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract relevant data
# This example assumes you want to extract game scores and team names
games = soup.find_all('article', class_='scoreboard')

for game in games:
    teams = game.find_all('span', class_='sb-team-short')
    scores = game.find_all('span', class_='sb-team-score')
    
    if len(teams) == 2 and len(scores) == 2:
        team1 = teams[0].text
        team2 = teams[1].text
        score1 = scores[0].text
        score2 = scores[1].text
        print(f"{team1} {score1} - {team2} {score2}")

# Note: The actual class names and structure may vary, so you may need to inspect the webpage
# and adjust the selectors accordingly.