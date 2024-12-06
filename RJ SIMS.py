import os

# In-memory database to store SIM card details
sim_cards = []

# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu options
def menu():
    clear_console()
    print("=== RJ'S SIM Card Loading System ===")
    print("1. Add SIM Card")
    print("2. View All SIM Cards")
    print("3. Update SIM Card")
    print("4. Delete SIM Card")
    print("5. Exit")
    choice = input("Choose an option: ")
    return choice

# Add SIM card
def add_sim_card():
    clear_console()
    print("=== Add SIM Card ===")
    sim_number = input("Enter SIM Number: ")
    balance = float(input("Enter Balance: "))
    owner = input("Enter Owner Name: ")
    sim_cards.append({
        "sim_number": sim_number,
        "balance": balance,
        "owner": owner
    })
    print("SIM card added successfully!")
    input("Press Enter to continue...")

# View all SIM cards
def view_sim_cards():
    clear_console()
    print("=== SIM Cards ===")
    if not sim_cards:
        print("No SIM cards found!")
    else:
        for idx, sim in enumerate(sim_cards, start=1):
            print(f"{idx}. SIM Number: {sim['sim_number']}, Balance: {sim['balance']}, Owner: {sim['owner']}")
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
            sim['balance'] = float(input("Enter New Balance: "))
            sim['owner'] = input("Enter New Owner Name: ")
            print("SIM card updated successfully!")
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
            print("SIM card deleted successfully!")
            input("Press Enter to continue...")
            return
    print("SIM card not found!")
    input("Press Enter to continue...")

# Main application loop
def main():
    while True:
        choice = menu()
        if choice == '1':
            add_sim_card()
        elif choice == '2':
            view_sim_cards()
        elif choice == '3':
            update_sim_card()
        elif choice == '4':
            delete_sim_card()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")

# Entry point of the program
if __name__ == "__main__":
    main()
