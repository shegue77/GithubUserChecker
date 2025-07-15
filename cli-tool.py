import requests

def get_github_profile(username):
    print('Getting data...\n')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"User: {data['login']}")
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Public Repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")
        print(f"Bio: {data.get('bio', 'N/A')}")
        print(data)
    else:
        print(f"Failed to fetch profile. Status code: {response.status_code}")

def list_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f"\nRepositories for {username}:")
        for repo in repos:
            print(f"- {repo['name']} (⭐ {repo['stargazers_count']})")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

def main():
    try:
        while True:
            username = input("Enter your GitHub username: ")
            get_github_profile(username)
            list_repositories(username)
            print('\n\n')
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
