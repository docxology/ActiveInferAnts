import os
from nbconvert import PythonExporter, MarkdownExporter
import nbformat
from collections import defaultdict

def convert_notebook(notebook_path: str, output_format: str = 'script') -> str:
    """
    Converts a Jupyter Notebook to either a Python script or a Markdown file and returns the output path.
    
    Args:
        notebook_path (str): The path to the Jupyter Notebook.
        output_format (str): The format to convert the notebook into ('script' or 'markdown').
        
    Returns:
        str: The path to the converted notebook.
    """
    # Define the output path based on the desired format
    output_path = notebook_path.replace(".ipynb", ".py" if output_format == 'script' else ".md")
    exporter = PythonExporter() if output_format == 'script' else MarkdownExporter()

    # Load the notebook object
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        nb_node = nbformat.read(nb_file, as_version=4)
    
    # Export the notebook object to the desired format
    output_content, _ = exporter.from_notebook_node(nb_node)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(output_content)
    
    return output_path

def convert_notebooks_in_directory(directory: str, output_format: str = 'script') -> None:
    """
    Converts all Jupyter Notebooks within a specified directory and its subdirectories into Python scripts or Markdown files,
    and prints a summary of conversions per repository.
    
    Args:
        directory (str): The root directory to search for Jupyter Notebooks.
        output_format (str): The format to convert the notebooks into ('script' or 'markdown').
    """
    conversion_summary = defaultdict(int)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_path = os.path.join(root, file)
                output_path = convert_notebook(notebook_path, output_format)
                repo_name = root.split(os.sep)[-1]  # Assuming the immediate parent directory is the repo name
                conversion_summary[repo_name] += 1
                print(f"Converted {notebook_path} to {output_path}.")
        
        if root.split(os.sep)[-1] in conversion_summary:  # Check if the current directory is a repo with conversions
            repo_name = root.split(os.sep)[-1]
            print(f"Finished converting notebooks in {repo_name}. Total: {conversion_summary[repo_name]} notebook(s).")
    
    print("\nOverall Conversion Summary per Repository:")
    for repo, count in conversion_summary.items():
        print(f"{repo}: {count} notebook(s) converted.")

if __name__ == "__main__":
    target_directory = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    output_format = input("Enter the output format ('script' for Python scripts or 'markdown' for Markdown files, default is 'script'): ").strip() or "script"
    convert_notebooks_in_directory(target_directory, output_format)

