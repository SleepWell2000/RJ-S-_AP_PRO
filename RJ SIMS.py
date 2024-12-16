import csv
import os

# Constants
DATA_FILE = "sim_cards.csv"
sim_cards = []  # Global list to store sim cards

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_sim_number(sim_number):
    """Validate SIM card number format"""
    if not sim_number:
        return False
    return (len(sim_number) == 11 and 
            sim_number.isdigit() and 
            sim_number.startswith("09"))

def validate_balance(balance):
    """Validate balance amount"""
    try:
        amount = float(balance)
        return amount >= 0
    except ValueError:
        return False

def load_data():
    """Load SIM card data from CSV file"""
    global sim_cards
    sim_cards = []
    
    if not os.path.exists(DATA_FILE):
        return
        
    try:
        with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(key in row for key in ["sim_number", "balance", "owner"]):
                    sim_cards.append({
                        "sim_number": row["sim_number"],
                        "balance": row["balance"],
                        "owner": row["owner"]
                    })
    except Exception:
        sim_cards = []

def save_data():
    """Save SIM card data to CSV file"""
    global sim_cards
    if not sim_cards:
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        return
    
    try:
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["sim_number", "balance", "owner"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sim in sim_cards:
                writer.writerow({
                    "sim_number": sim["sim_number"],
                    "balance": str(sim["balance"]),
                    "owner": sim["owner"]
                })
    except Exception as e:
        print(f"Error saving data: {e}")
        raise  # Re-raise the exception for the test to catch

# Menu options
def menu():
    clear_screen()
    print("=== RJ'S SIM Card Management System ===")
    print("1. Add SIM Card")
    print("2. View All SIM Cards")
    print("3. Search SIM Card")
    print("4. Update SIM Card")
    print("5. Delete SIM Card")
    print("6. Export Data")
    print("7. Exit")
    choice = input("Choose an option: ")
    return choice

# Reusable function for user input with validation
def get_input(prompt, valid_condition_func, error_message):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'back' or user_input == '00':
            return 'back'
        if valid_condition_func(user_input):
            return user_input
        print(error_message)

# Add SIM card
def add_sim_card():
    while True:
        clear_screen()  # Clear screen before adding a SIM card
        print("=== Add SIM Card ===")
        print("(Type 'back' or '00' to return to menu)")

        sim_number = get_input("Enter SIM Number: ", 
                             lambda x: validate_sim_number(x) and not any(sim['sim_number'] == x for sim in sim_cards), 
                             "Error: SIM Number must be 11 digits, start with '09', and be unique!")
        if sim_number == 'back':
            return

        balance = get_input("Enter Balance: ",
                          validate_balance, 
                          "Error: Balance must be a non-negative number!")
        if balance == 'back':
            return

        owner = get_input("Enter Owner Name: ", 
                         lambda x: all(c.isalpha() or c.isspace() or c in "-'" for c in x), 
                         "Error: Owner Name must contain only letters, spaces, and optionally hyphens/apostrophes!")
        if owner == 'back':
            return

        sim_cards.append({
            "sim_number": sim_number,
            "balance": balance,
            "owner": owner
        })
        save_data()
        print("SIM card added successfully!")
        input("Press Enter to continue...")
        return

# View all SIM cards
def view_sim_cards():
    while True:
        clear_screen()  # Clear screen before viewing SIM cards
        print("=== SIM Cards ===")
        if not sim_cards:
            print("No SIM cards found!")
        else:
            print("{:<5} {:<15} {:<10} {:<20}".format("No.", "SIM Number", "Balance", "Owner"))
            print("-" * 50)
            for i, sim in enumerate(sim_cards, 1):
                print("{:<5} {:<15} {:<10} {:<20}".format(
                    i, 
                    sim['sim_number'], 
                    sim['balance'], 
                    sim['owner']
                ))

        print("\nType 'back' or '00' to return to menu")
        choice = input("Press Enter to continue...")
        if choice.lower() == 'back' or choice == '00':
            return

# Search SIM card
def search_sim_card():
    while True:
        clear_screen()  # Clear screen before searching
        print("=== Search SIM Card ===")
        print("(Type 'back' or '00' to return to menu)")

        search_term = input("Enter SIM number or owner name to search: ")
        if search_term.lower() == 'back' or search_term == '00':
            return

        results = []
        for sim in sim_cards:
            if (search_term.lower() in sim['sim_number'].lower() or 
                search_term.lower() in sim['owner'].lower()):
                results.append(sim)

        if results:
            print("\nSearch Results:")
            print("{:<5} {:<15} {:<10} {:<20}".format("No.", "SIM Number", "Balance", "Owner"))
            print("-" * 50)
            for i, sim in enumerate(results, 1):
                print("{:<5} {:<15} {:<10} {:<20}".format(
                    i, 
                    sim['sim_number'], 
                    sim['balance'], 
                    sim['owner']
                ))
        else:
            print("\nNo matching records found!")

        input("\nPress Enter to continue...")

# Update SIM card
def update_sim_card():
    while True:
        clear_screen()  # Clear screen before updating SIM card
        print("=== Update SIM Card ===")
        print("(Type 'back' or '00' to return to menu)")

        sim_number = input("Enter SIM number to update: ")
        if sim_number.lower() == 'back' or sim_number == '00':
            return

        for sim in sim_cards:
            if sim['sim_number'] == sim_number:
                print("\nCurrent Details:")
                print(f"SIM Number: {sim['sim_number']}")
                print(f"Balance: {sim['balance']}")
                print(f"Owner: {sim['owner']}")

                new_balance = get_input("\nEnter new balance (or press Enter to skip): ",
                                      lambda x: not x or validate_balance(x),
                                      "Error: Balance must be a non-negative number!")
                if new_balance == 'back':
                    return

                new_owner = get_input("Enter new owner name (or press Enter to skip): ",
                                    lambda x: not x or all(c.isalpha() or c.isspace() or c in "-'" for c in x),
                                    "Error: Owner name must contain only letters, spaces, and optionally hyphens/apostrophes!")
                if new_owner == 'back':
                    return

                if new_balance:
                    sim['balance'] = new_balance
                if new_owner:
                    sim['owner'] = new_owner

                save_data()
                print("\nSIM card updated successfully!")
                input("Press Enter to continue...")
                return

        print("\nSIM card not found!")
        input("Press Enter to continue...")

# Delete SIM card
def delete_sim_card():
    while True:
        clear_screen()  # Clear screen before deleting SIM card
        print("=== Delete SIM Card ===")
        print("(Type 'back' or '00' to return to menu)")

        sim_number = input("Enter SIM number to delete: ")
        if sim_number.lower() == 'back' or sim_number == '00':
            return

        for i, sim in enumerate(sim_cards):
            if sim['sim_number'] == sim_number:
                print("\nFound SIM card:")
                print(f"SIM Number: {sim['sim_number']}")
                print(f"Balance: {sim['balance']}")
                print(f"Owner: {sim['owner']}")

                confirm = input("\nAre you sure you want to delete this SIM card? (y/n): ")
                if confirm.lower() == 'y':
                    sim_cards.pop(i)
                    save_data()
                    print("\nSIM card deleted successfully!")
                else:
                    print("\nDeletion cancelled!")
                input("Press Enter to continue...")
                return

        print("\nSIM card not found!")
        input("Press Enter to continue...")

# Export data
def export_data():
    while True:
        clear_screen()  # Clear screen before exporting data
        print("=== Export Data ===")
        print("(Type 'back' or '00' to return to menu)")

        if not sim_cards:
            print("No data to export!")
            input("Press Enter to continue...")
            return

        filename = input("Enter filename for export (without extension): ")
        if filename.lower() == 'back' or filename == '00':
            return

        try:
            export_file = f"{filename}.csv"
            with open(export_file, mode='w', newline='') as file:
                fieldnames = ["sim_number", "balance", "owner"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(sim_cards)
            print(f"\nData exported successfully to {export_file}")
        except Exception as e:
            print(f"\nError exporting data: {e}")

        input("Press Enter to continue...")
        return

# Main program loop
def main():
    load_data()
    while True:
        choice = menu()
        if choice == '1':
            add_sim_card()
        elif choice == '2':
            view_sim_cards()
        elif choice == '3':
            search_sim_card()
        elif choice == '4':
            update_sim_card()
        elif choice == '5':
            delete_sim_card()
        elif choice == '6':
            export_data()
        elif choice == '7':
            print("Thank you for using the system!")
            break
        else:
            input("Invalid choice! Press Enter to continue...")

if __name__ == "__main__":
    main()
