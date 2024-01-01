class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Checked Out: {'Yes' if self.checked_out else 'No'}")

    def check_out(self):
        if not self.checked_out:
            print(f"Checking out {self.title}")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.checked_out:
            print(f"Checking in {self.title}")
            self.checked_out = False
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")


# Example usage
book1 = Book("The Catcher in the Rye", "B001", "J.D. Salinger")
dvd1 = DVD("Inception", "D001", "Christopher Nolan", 148)

book1.display_info()
book1.check_out()
book1.display_info()
book1.check_in()
book1.display_info()

print("\n")

dvd1.display_info()
dvd1.check_out()
dvd1.display_info()
dvd1.check_in()
dvd1.display_info()
