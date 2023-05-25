import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Optional
import re



class Quine:
    """
    A class to represent a Quine.

    This version of Quine works with Markdown files. It can optionally print the content of the Markdown files or just the headings and subheadings.
    It can also optionally take in a path for a configuration `yml` file to be printed at the top of the output file.

    ...

    Attributes
    ----------
    base_directory : str
        the base directory to start from
    excluded_directories : set
        a set of directories to be excluded
    included_extensions : set
        a set of file extensions to be included
    print_content : bool
        if True, print the content of the markdown files
    config_path : str
        optional path to a configuration yml file

    Methods
    -------
    write_to_file(root_directory:str, file_name:str, output_file:object):
        Writes the content of the file to the output markdown file.
    generate_quine():
        Walks through the base directory and its subdirectories, excluding certain directories and file types,
        and writes the markdown source code or headings/subheadings to a Markdown file.
    """

    def __init__(self, base_directory: str, excluded_directories: List[str], included_extensions: List[str], print_content: bool, config_path: Optional[str] = None):
        self.base_directory = base_directory
        self.excluded_directories = excluded_directories
        self.included_extensions = included_extensions
        self.print_content = print_content
        self.config_path = config_path

    def write_to_file(self, root_directory: str, file_name: str, output_file: object) -> None:
        """
        Writes the content of the file to the output markdown file.

        Parameters
        ----------
        root_directory : str
            The root directory.
        file_name : str
            The file name.
        output_file : object
            The output file object.
        """
        output_file.write(f"## {file_name}\n\n")
        with open(os.path.join(root_directory, file_name), "r", encoding='utf-8', errors='ignore') as file:
            file_content = file.read()
            if self.print_content:
                output_file.write(file_content)
                print(file_content)  # Print the file content to the terminal
            else:
                headings = re.findall(r"#{1,6}\s(.*?)\n", file_content)
                for heading in headings:
                    output_file.write(f"- {heading}\n")
                print(headings)

    def generate_quine(self) -> None:
        """
        Walks through the base directory and its subdirectories, excluding certain directories and file types,
        and writes the markdown source code or headings/subheadings to a Markdown file.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"quine_{current_time}.md"
        output_dir = Path().cwd() / "output"  # Output directory
        output_dir.mkdir(parents=True, exist_ok=True)  # Create the output directory if it doesn't exist
        file_path = output_dir / file_name  # Output file path
        with open(file_path, "w", encoding='utf-8', errors='ignore') as output_file:
            if self.config_path:
                with open(self.config_path, "r") as config_file:
                    output_file.write(config_file.read())
                    output_file.write("\n---\n\n")
            for root_directory, directories, files in os.walk(self.base_directory):
                directories[:] = [directory for directory in directories if directory not in self.excluded_directories]
                if root_directory != ".":
                    output_file.write(f"# {os.path.relpath(root_directory, '../docs')}\n\n")
                for file_name in files:
                    if any(file_name.endswith(extension) for extension in self.included_extensions):
                        self.write_to_file(root_directory, file_name, output_file)


if __name__ == "__main__":
    base_directory_in = r"C:\Users\jonma\github_repos\freemocap_organization\documentation\docs"
    quine = Quine(
        base_directory=base_directory_in,

        # exclude irrelevant directories
        excluded_directories=["__pycache__",
                              ".git",
                              "utilities",
                              ],

        # Include markdown files
        included_extensions=[".md"],

        # Whether to print the content of the markdown files
        print_content=False,

        # Optional path to a configuration yml file
        config_path=r"C:\Users\jonma\github_repos\freemocap_organization\documentation\mkdocs.yml"
    )
    quine.generate_quine()
