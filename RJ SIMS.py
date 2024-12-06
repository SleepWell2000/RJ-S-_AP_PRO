import os
import json

# File for persistent data storage
DATA_FILE = "sim_cards.json"

# In-memory database to store SIM card details
sim_cards = []

# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load data from file
def load_data():
    global sim_cards
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            sim_cards = json.load(file)

# Save data to file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(sim_cards, file, indent=4)

# Menu options
def menu():
    clear_console()
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

# Add SIM card
def add_sim_card():
    clear_console()
    print("=== Add SIM Card ===")
    sim_number = input("Enter SIM Number: ")
    if any(sim['sim_number'] == sim_number for sim in sim_cards):
        print("Error: SIM Number already exists!")
        input("Press Enter to continue...")
        return
    try:
        balance = float(input("Enter Balance: "))
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        owner = input("Enter Owner Name: ")
        sim_cards.append({
            "sim_number": sim_number,
            "balance": balance,
            "owner": owner
        })
        save_data()
        print("SIM card added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")

# View all SIM cards
def view_sim_cards():
    clear_console()
    print("=== SIM Cards ===")
    if not sim_cards:
        print("No SIM cards found!")
    else:
        print("{:<5} {:<15} {:<10} {:<20}".format("No.", "SIM Number", "Balance", "Owner"))
        print("-" * 50)
        for idx, sim in enumerate(sim_cards, start=1):
            print("{:<5} {:<15} {:<10.2f} {:<20}".format(idx, sim['sim_number'], sim['balance'], sim['owner']))
    input("Press Enter to continue...")

# Search SIM card
def search_sim_card():
    clear_console()
    print("=== Search SIM Card ===")
    search_term = input("Enter SIM Number or Owner Name to Search: ").lower()
    results = [sim for sim in sim_cards if search_term in sim['sim_number'] or search_term in sim['owner'].lower()]
    if not results:
        print("No matching SIM cards found!")
    else:
        print("{:<5} {:<15} {:<10} {:<20}".format("No.", "SIM Number", "Balance", "Owner"))
        print("-" * 50)
        for idx, sim in enumerate(results, start=1):
            print("{:<5} {:<15} {:<10.2f} {:<20}".format(idx, sim['sim_number'], sim['balance'], sim['owner']))
    input("Press Enter to continue...")

# Update SIM card
def update_sim_card():
    clear_console()
    print("=== Update SIM Card ===")
    sim_number = input("Enter SIM Number to Update: ")
    for sim in sim_cards:
        if sim['sim_number'] == sim_number:
            print("Current Details:")
            print(f"SIM Number: {sim['sim_number']}, Balance: {sim['balance']}, Owner: {sim['owner']}")
            try:
                sim['balance'] = float(input("Enter New Balance: "))
                sim['owner'] = input("Enter New Owner Name: ")
                save_data()
                print("SIM card updated successfully!")
            except ValueError:
                print("Error: Invalid input for balance!")
            input("Press Enter to continue...")
            return
    print("SIM card not found!")
    input("Press Enter to continue...")

# Delete SIM card
def delete_sim_card():
    clear_console()
    print("=== Delete SIM Card ===")
    sim_number = input("Enter SIM Number to Delete: ")
    for sim in sim_cards:
        if sim['sim_number'] == sim_number:
            sim_cards.remove(sim)
            save_data()
            print("SIM card deleted successfully!")
            input("Press Enter to continue...")
            return
    print("SIM card not found!")
    input("Press Enter to continue...")

# Export data to a file
def export_data():
    clear_console()
    print("=== Export Data ===")
    file_name = input("Enter file name to export (e.g., sim_cards.json): ")
    with open(file_name, "w") as file:
        json.dump(sim_cards, file, indent=4)
    print(f"Data exported to {file_name} successfully!")
    input("Press Enter to continue...")

# Main application loop
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
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")

# Entry point of the program
if __name__ == "__main__":
    main()
