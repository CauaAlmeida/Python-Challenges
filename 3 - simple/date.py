class Dates:
    
    def __init__(self) -> None:
        self.month = int(input("Type the month: "))
        self.day = int(input("Type the day: "))
        self.year = int(input("Type the year: "))
        month = self.month
        day = self.day
        year = self.year
        print("Formatting your date...")
        print(f"Formatted date: {month}/{day}/{year}.")
        self.date = f"{month}/{day}/{year}"
