#!/usr/bin/env python3
"""
Console Bot Assistant

A simple command-line bot that manages contacts with names and phone numbers.
The bot recognizes commands entered from the keyboard and responds accordingly.

Commands:
    hello - Greet the user
    add [name] [phone] - Add a new contact
    change [name] [phone] - Change existing contact's phone number
    phone [name] - Show phone number for a contact
    all - Show all contacts
    close/exit - Exit the bot
"""

from typing import Dict, List, Tuple


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parse user input into command and arguments.
    
    Args:
        user_input (str): Raw input from user
        
    Returns:
        Tuple[str, List[str]]: Command and list of arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (List[str]): List containing [name, phone]
        contacts (Dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Success message or error message
    """
    if len(args) != 2:
        return "Error: Please provide both name and phone number."
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Change phone number for existing contact.
    
    Args:
        args (List[str]): List containing [name, new_phone]
        contacts (Dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Success message or error message
    """
    if len(args) != 2:
        return "Error: Please provide both name and new phone number."
    
    name, phone = args
    
    if name not in contacts:
        return "Error: Contact not found."
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Show phone number for a specific contact.
    
    Args:
        args (List[str]): List containing [name]
        contacts (Dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Phone number or error message
    """
    if len(args) != 1:
        return "Error: Please provide contact name."
    
    name = args[0]
    
    if name not in contacts:
        return "Error: Contact not found."
    
    return contacts[name]


def show_all(contacts: Dict[str, str]) -> str:
    """
    Show all contacts with their phone numbers.
    
    Args:
        contacts (Dict[str, str]): Dictionary of contacts
        
    Returns:
        str: All contacts formatted as string
    """
    if not contacts:
        return "No contacts found."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)


def main() -> None:
    """
    Main function that manages the command processing loop.
    """
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input: str = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main() 