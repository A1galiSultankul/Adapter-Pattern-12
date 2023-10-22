from abc import ABC, abstractmethod

class BookingSystem(ABC):
    @abstractmethod
    def bookTicket(self, name, date, showTime, tickets):
        pass

    @abstractmethod
    def deleteTicket(self, name, date):
        pass

    @abstractmethod
    def buyTicket(self, name, date, showTime, tickets):
        pass

class ConcertShow:
    def reserveTT(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} on {date} at {showTime}, let's quickly buy a ticket to the concert")

    def buyTT(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the show on {date} at {showTime} are booked.")

class ConcertShowAdapter(BookingSystem):
    def __init__(self, concertShow):
        self.concertShow = concertShow
        self.purchasedTickets = []

    def bookTicket(self, name, date, showTime, tickets):
        try:
            if not isinstance(tickets, int) or tickets <= 0:
                raise ValueError("Invalid ticket quantity. Please provide a valid positive integer.")

            self.concertShow.reserveTT(name, date, showTime, tickets)
            self.purchasedTickets.append((name, date, showTime, tickets))
            print(f"Booking completed for {name} on {date} at {showTime} for {tickets} tickets.")

        except ValueError as e:
            print(f"Error in booking: {e}")

    def deleteTicket(self, name, date):
        try:
            raise NotImplementedError("Deletion not supported by the concert")
        except NotImplementedError as e:
            print(f"Error in deleting ticket: {e}")

    def buyTicket(self, name, date, showTime, tickets):
        try:
            if not isinstance(tickets, int) or tickets <= 0:
                raise ValueError("Invalid ticket quantity. Please provide a valid positive integer.")

            self.concertShow.buyTT(name, date, showTime, tickets)
            self.purchasedTickets.append((name, date, showTime, tickets))
            print(f"Purchase completed for {name} on {date} at {showTime} for {tickets} tickets.")

        except ValueError as e:
            print(f"Error in buying ticket: {e}")

    def viewPurchasedTickets(self):
        if self.purchasedTickets:
            print("Purchased Tickets:")
            for ticket in self.purchasedTickets:
                print(f"Name: {ticket[0]}, Date: {ticket[1]}, Show Time: {ticket[2]}, Tickets: {ticket[3]}")
        else:
            print("No purchased tickets.")

class Configuration:
    showTimes = ["6pm", "8pm", "10pm", "12pm"]

if __name__ == '__main__':
    adapter = ConcertShowAdapter(ConcertShow())

    while True:
        print("\n1. Book a ticket \n2. Delete a ticket \n3. Buy a ticket \n4. View Purchased Tickets\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':

            name = input("Enter your name: ")
            showDate = input("Enter the date (YYYY-MM-DD): ")
            print("Available show times:", Configuration.showTimes)
            showTime = input("Choose the show time: ")
            tickets = int(input("Enter the number of tickets: "))
            adapter.bookTicket(name, showDate, showTime, tickets)

        elif choice == '2':
            name = input("Enter your name: ")
            showDate = input("Enter the date to delete (YYYY-MM-DD): ")
            adapter.deleteTicket(name, showDate)

        elif choice == '3':
            name = input("Enter your name: ")
            showDate = input("Enter the date (YYYY-MM-DD): ")
            print("Available show times:", Configuration.showTimes)
            showTime = input("Choose the show time: ")
            tickets = int(input("Enter the number of tickets: "))
            adapter.buyTicket(name, showDate, showTime, tickets)
        elif choice == '4':
            adapter.viewPurchasedTickets()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")  #
