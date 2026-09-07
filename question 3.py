# Part(i): Student Marks
students={
    "lan":85,
    "Brain":92,
    "Charmaine":78,
    "Danai":95,
    "Skilli":88,
}

for name,mark in students.items():
    print(name, mark)

    highest_marks= 0

    top_student= ""

    for name,mark in students.items():
        if mark > highest_marks:
            highest_marks= mark
            top_student= name

            print("Top student:",top_student)
            print("Highest marks:",highest_marks)

            print()

            # Part (ii): Book Class
            class Book:
             def __init__(self,title,author,price):
                self.title= title
                self.author= author
                self.price= price

                def display_details(self):
                 print("Title:",self.title)
                 print("Price:",self.price)

                book1=Book("To kill a Mockingbird","Harper Lee",14.99)
                book2=Book("1984","George Orwell",12.50)

                book1.display_details()
                book2.display_details()
