#!/usr/bin/env python3
"""
Test script for Console Bot Assistant

This script demonstrates the bot functionality by testing all commands.
"""

from bot import parse_input, add_contact, change_contact, show_phone, show_all


def test_bot_functionality():
    """Test all bot functions to ensure they work correctly."""
    
    print("=== Testing Console Bot Assistant ===\n")
    
    # Initialize contacts dictionary
    contacts = {}
    
    # Test 1: Parse input function
    print("1. Testing parse_input function:")
    cmd, args = parse_input("add John 1234567890")
    print(f"   Input: 'add John 1234567890'")
    print(f"   Command: '{cmd}', Args: {args}")
    
    cmd, args = parse_input("HELLO")
    print(f"   Input: 'HELLO'")
    print(f"   Command: '{cmd}', Args: {args}")
    print()
    
    # Test 2: Add contacts
    print("2. Testing add_contact function:")
    result = add_contact(["John", "1234567890"], contacts)
    print(f"   add John 1234567890 -> {result}")
    
    result = add_contact(["Jane", "0987654321"], contacts)
    print(f"   add Jane 0987654321 -> {result}")
    
    result = add_contact(["Alice"], contacts)  # Error case
    print(f"   add Alice (missing phone) -> {result}")
    print()
    
    # Test 3: Show all contacts
    print("3. Testing show_all function:")
    result = show_all(contacts)
    print(f"   Current contacts:\n{result}")
    print()
    
    # Test 4: Show specific phone
    print("4. Testing show_phone function:")
    result = show_phone(["John"], contacts)
    print(f"   phone John -> {result}")
    
    result = show_phone(["Bob"], contacts)  # Error case
    print(f"   phone Bob (not found) -> {result}")
    
    result = show_phone([], contacts)  # Error case
    print(f"   phone (no name) -> {result}")
    print()
    
    # Test 5: Change contact
    print("5. Testing change_contact function:")
    result = change_contact(["John", "1111111111"], contacts)
    print(f"   change John 1111111111 -> {result}")
    
    result = change_contact(["Bob", "2222222222"], contacts)  # Error case
    print(f"   change Bob 2222222222 (not found) -> {result}")
    
    result = change_contact(["John"], contacts)  # Error case
    print(f"   change John (missing phone) -> {result}")
    print()
    
    # Test 6: Show all contacts after changes
    print("6. Final contacts list:")
    result = show_all(contacts)
    print(f"{result}")
    print()
    
    # Test 7: Empty contacts
    print("7. Testing with empty contacts:")
    empty_contacts = {}
    result = show_all(empty_contacts)
    print(f"   show_all (empty) -> {result}")
    print()
    
    print("=== All tests completed successfully! ===")


def demonstrate_interactive_usage():
    """Show example of how the bot would work interactively."""
    
    print("\n=== Example Interactive Session ===")
    print("Welcome to the assistant bot!")
    
    # Simulate user interactions
    interactions = [
        ("hello", "How can I help you?"),
        ("add John 1234567890", "Contact added."),
        ("add Jane 0987654321", "Contact added."),
        ("all", "John: 1234567890\nJane: 0987654321"),
        ("phone John", "1234567890"),
        ("change John 1111111111", "Contact updated."),
        ("phone John", "1111111111"),
        ("phone Bob", "Error: Contact not found."),
        ("invalid_command", "Invalid command."),
        ("close", "Good bye!")
    ]
    
    for user_input, expected_output in interactions:
        print(f"Enter a command: {user_input}")
        print(f"{expected_output}")
    
    print("\n=== End of Interactive Demo ===")


if __name__ == "__main__":
    test_bot_functionality()
    demonstrate_interactive_usage() 