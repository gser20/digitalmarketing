# main.py

from clients import add_client, get_clients
from campaigns import create_campaign, track_campaign_performance, generate_report


def main():
    print("Welcome to the Digital Marketing Business App!")

    while True:
        print("\n1. Add Client")
        print("2. Create Campaign")
        print("3. Track Campaign Performance")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            create_campaign(get_clients())
        elif choice == '3':
            track_campaign_performance()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Thank you for using the Digital Marketing Business App!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()