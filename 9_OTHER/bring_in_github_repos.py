import subprocess
import sys

def clone_repo(target_dir=None):
    """
    Clones the pymdp repository into the specified target directory.
    If no target directory is specified, it clones into the current directory.
    
    Parameters:
    target_dir (str, optional): The directory to clone the repository into.
    """
    git_url = "https://github.com/infer-actively/pymdp"
    clone_command = ["git", "clone", git_url]
    if target_dir:
        clone_command.append(target_dir)
    
    try:
        subprocess.run(clone_command, check=True)
        print(f"Successfully cloned {git_url} into {target_dir if target_dir else 'current directory'}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {git_url}. Error: {e}", file=sys.stderr)

# Example usage
if __name__ == "__main__":
    target_dir = input("Enter the target directory (leave blank to clone into the current directory): ")
    clone_repo(target_dir.strip() or None)
