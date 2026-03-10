from users import users

tickets = []

def login():
    print("=== Login ===")
    username = input("Benutzername: ")
    password = input("Passwort: ")

    if username in users and users[username]["password"] == password:
        print("Login erfolgreich!\n")
        return username
    else:
        print("Falsche Login-Daten\n")
        return None


def create_ticket(user):
    title = input("Titel des Tickets: ")
    description = input("Beschreibung: ")

    ticket = {
        "user": user,
        "title": title,
        "description": description,
        "status": "offen"
    }

    tickets.append(ticket)
    print("Ticket erstellt!\n")


def show_tickets():
    print("\n=== Alle Tickets ===")

    if not tickets:
        print("Keine Tickets vorhanden\n")
        return

    for i, ticket in enumerate(tickets):
        print(f"\nTicket #{i+1}")
        print("User:", ticket["user"])
        print("Titel:", ticket["title"])
        print("Beschreibung:", ticket["description"])
        print("Status:", ticket["status"])


def main():
    user = None

    while not user:
        user = login()

    while True:
        print("\n=== Menü ===")
        print("1 - Ticket erstellen")
        print("2 - Tickets anzeigen")
        print("3 - Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            create_ticket(user)

        elif choice == "2":
            show_tickets()

        elif choice == "3":
            print("Programm beendet")
            break

        else:
            print("Ungültige Auswahl")


if __name__ == "__main__":
    main()
