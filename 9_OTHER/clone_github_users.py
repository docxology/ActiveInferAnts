import subprocess
import sys
import os
import requests
from typing import Union, List, Dict

def clone_repo(git_url: str, target_dir: str) -> None:
    """
    Clones a single GitHub repository into the specified target directory.
    
    Parameters:
    - git_url (str): The GitHub repository URL to clone.
    - target_dir (str): The directory to clone the repository into.
    """
    repo_name = git_url.split('/')[-1]  # Extracts repo name from URL
    full_path = os.path.join(target_dir, repo_name)
    clone_command = ["git", "clone", git_url, full_path]
    
    try:
        subprocess.run(clone_command, check=True, capture_output=True)
        print(f"Successfully cloned {git_url} into {full_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {git_url}. Error: {e.stderr.decode()}", file=sys.stderr)

def get_user_repos(username: str) -> List[str]:
    """
    Fetches all public repository URLs of a given GitHub user.
    
    Parameters:
    - username (str): The GitHub username to fetch repositories for.
    
    Returns:
    List[str]: A list of repository clone URLs.
    """
    repos_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repos_url)
    repos = response.json()
    return [repo['clone_url'] for repo in repos]

def clone_user_repos(username: str, target_dir: str) -> None:
    """
    Clones all public repositories of a given GitHub user into the specified target directory.
    
    Parameters:
    - username (str): The GitHub username whose repositories to clone.
    - target_dir (str): The directory to clone the repositories into.
    """
    repo_urls = get_user_repos(username)
    for git_url in repo_urls:
        clone_repo(git_url, target_dir)
if __name__ == "__main__":
    users_to_clone = {
        "ActiveInference": ["infer-actively", "ago109", "daphnedemekas", "conorheins", "ChampiB", "zfountas", "alec-tschantz", "schwartenbeckph", "tejparr", "biaslab", "rssmith33"],
        # More Active Inference: "HMCL-UNIST", "AP6YC", fabio-deep", "BerenMillidge", "fgregoretti", "cpezzato", "edluyuan","djcrw", "spm", "wmkouw", "tomekkorbak"
        # "ActiveInferenceInstitute" -- for bringing in examples, educational materials, transcripts, etc. 
        "Synergetics": ["4dsolutions"],
        # "Ants": ["Social-Insect-Genomics", "cdanielcadena", "cooplab", "johnssproul", "pbfrandsen", "PeterMulhair", "fohebert", "guillemylla", "guo-cheng"],
        #"Agents": ["Anthropic", "OpenAI", "Significant-Gravitas", "yoheinakajima", "TransformerOptimus", "Paitesanshi", "kyrolabs", "lafmdp", "Jenqyang", "e2b-dev", "OpenBMB"]
    }\
    
    target_dir = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    
    for category, usernames in users_to_clone.items():
        print(f"Cloning {category} repositories...")
        for username in usernames:
            user_target_dir = os.path.join(target_dir, category, username)
            if not os.path.exists(user_target_dir):
                os.makedirs(user_target_dir)
            clone_user_repos(username, user_target_dir)
