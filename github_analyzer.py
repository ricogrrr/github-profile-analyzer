import requests
import matplotlib.pyplot as plt

GITHUB_USERNAME = "ricogrrr"  # Change this to any GitHub username

def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def analyze_languages(repos):
    language_count = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1
    return language_count

def plot_languages(language_data):
    if not language_data:
        print("No language data available")
        return
    
    plt.figure(figsize=(8, 5))
    plt.bar(language_data.keys(), language_data.values(), color="skyblue")
    plt.xlabel("Programming Languages")
    plt.ylabel("Number of Repositories")
    plt.title("GitHub Repositories by Language")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    user_data = get_github_data(GITHUB_USERNAME)
    if user_data:
        print(f"GitHub Profile: {user_data['name']} (@{user_data['login']})")
        print(f"Public Repos: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']} | Following: {user_data['following']}")

        repos = get_repos(GITHUB_USERNAME)
        language_stats = analyze_languages(repos)
        plot_languages(language_stats)
