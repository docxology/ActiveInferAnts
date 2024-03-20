import os
import subprocess
from collections import defaultdict

def clone_repo(git_url: str, target_dir: str) -> None:
    """
    Clones a single GitHub repository into the specified target directory.
    
    Parameters:
    git_url (str): The GitHub repository URL to clone.
    target_dir (str): The directory to clone the repository into.
    """
    repo_name = git_url.split('/')[-1]  # Extracts repo name from URL
    full_path = os.path.join(target_dir, repo_name)
    clone_command = ["git", "clone", git_url, full_path]
    
    try:
        subprocess.run(clone_command, check=True, capture_output=True)
        print(f"Successfully cloned {git_url} into {full_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {git_url}. Error: {e.stderr.decode()}", file=sys.stderr)

def list_repos(directory: str) -> None:
    """
    Lists all cloned repositories in the specified directory.
    
    Parameters:
    directory (str): The directory containing the cloned repositories.
    """
    repos = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    print("Cloned Repositories:")
    for repo in repos:
        print(f"- {repo}")

def repo_summary(directory: str) -> None:
    """
    Provides a summary of the repositories, including the number of files and total size.
    
    Parameters:
    directory (str): The directory containing the cloned repositories.
    """
    repos = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    summary = defaultdict(lambda: {"file_count": 0, "total_size": 0})
    for repo in repos:
        repo_path = os.path.join(directory, repo)
        for root, _, files in os.walk(repo_path):
            summary[repo]["file_count"] += len(files)
            for file in files:
                file_path = os.path.join(root, file)
                summary[repo]["total_size"] += os.path.getsize(file_path)
    
    print("Repository Summary:")
    for repo, info in summary.items():
        size_mb = info["total_size"] / (1024 * 1024)
        print(f"- {repo}: {info['file_count']} files, {size_mb:.2f} MB")
