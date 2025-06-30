#!/usr/bin/env python3
"""
Directory Structure Visualizer

A script that visualizes directory structure with colored output.
Directories and files are displayed in different colors for better visual perception.

Usage:
    python hw03.py /path/to/directory

Requirements:
    - colorama library for colored output
    - Python 3.6+

Author: DitriX
"""

import sys
import argparse
from pathlib import Path
from typing import List, Optional, Union, Iterator
from colorama import init, Fore, Back, Style


# Initialize colorama for cross-platform colored output
init(autoreset=True)

def setup_argument_parser() -> argparse.ArgumentParser:
    """
    Set up command line argument parser.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="Visualize directory structure with colored output",
        epilog="Example: python directory_visualizer.py /path/to/directory"
    )
    
    parser.add_argument(
        "directory_path",
        type=str,
        help="Path to the directory to visualize"
    )
    
    return parser


def validate_directory_path(path_str: str) -> Path:
    """
    Validate and convert string path to Path object.
    
    Args:
        path_str (str): String representation of the path
        
    Returns:
        Path: Validated Path object
        
    Raises:
        FileNotFoundError: If path doesn't exist
        NotADirectoryError: If path is not a directory
        PermissionError: If access is denied
    """
    try:
        path: Path = Path(path_str).resolve()
        
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {path}")
        
        # Test if we can access the directory
        try:
            list(path.iterdir())
        except PermissionError:
            raise PermissionError(f"Permission denied to access directory: {path}")
        
        return path
        
    except OSError as e:
        raise OSError(f"Error accessing path '{path_str}': {e}")


def get_directory_contents(directory: Path) -> List[Path]:
    try:
        contents: List[Path] = []
        
        for item in directory.iterdir():
            # Skip hidden files/directories
            if item.name.startswith('.'):
                continue
            contents.append(item)
        
        # Sort: directories first, then files, both alphabetically
        contents.sort(key=lambda x: (x.is_file(), x.name.lower()))
        
        return contents
        
    except PermissionError:
        print(f"{Fore.RED}Permission denied: {directory}")
        return []
    except OSError as e:
        print(f"{Fore.RED}Error reading directory {directory}: {e}")
        return []

def visualize_directory_recursive(
    directory: Path,
    prefix: str = "",
    is_last: bool = True
) -> None:
    """
    Recursively visualize directory structure.
    
    Args:
        directory (Path): Directory to visualize
        prefix (str): Prefix for tree drawing
        is_last (bool): Whether this is the last item in parent
    """
    
    # Get directory name and apply coloring
    dir_name: str = directory.name if directory.name else str(directory)
    colored_name: str = f"{Fore.BLUE}{Style.BRIGHT}📂 {dir_name}{Style.RESET_ALL}"
    
    # Print current directory
    tree_symbol: str = "┗ " if is_last else "┣ "
    print(f"{prefix}{tree_symbol}{colored_name}")
    
    # Prepare prefix for children
    child_prefix: str = prefix + ("   " if is_last else "┃  ")
    
    # Get directory contents
    contents: List[Path] = get_directory_contents(directory)
    
    if not contents:
        return
    
    # Process each item in directory
    for i, item in enumerate(contents):
        is_last_item: bool = (i == len(contents) - 1)
        item_symbol: str = "┗ " if is_last_item else "┣ "
        
        try:
            if item.is_dir():
                # Recursively process subdirectory
                visualize_directory_recursive(
                    item,
                    child_prefix,
                    is_last_item
                )
            else:
                # Process file
                colored_file: str = f"{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}"
                print(f"{child_prefix}{item_symbol}{colored_file}")
                
        except (PermissionError, OSError) as e:
            error_msg: str = f"{Fore.RED}[Error accessing: {item.name}]{Style.RESET_ALL}"
            print(f"{child_prefix}{item_symbol}{error_msg}")

def main() -> None:
    try:
        # Parse command line arguments
        parser: argparse.ArgumentParser = setup_argument_parser()
        args = parser.parse_args()
        
        # Validate directory path
        directory: Path = validate_directory_path(args.directory_path)
        
        # Visualize directory structure
        visualize_directory_recursive(directory)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Operation cancelled by user.{Style.RESET_ALL}")
        sys.exit(1)
        
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError) as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)
        
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main() 