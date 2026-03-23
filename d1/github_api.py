import requests

username = "Dotmebhanu"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()


for repo in repos:
    print(f"{repo['name']} — Stars: {repo['stargazers_count']}")