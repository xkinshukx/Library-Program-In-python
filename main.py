from Addbooks import Addbooks
from Issue import Issue
from showbooks import showbooks
from Return import Return

def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Addbooks()
        elif choice == 2:
            showbooks()
        elif choice == 3:
            Issue()
        elif choice == 4:
            Return()
        elif choice == 5:
            print("thank you have a nice greatful day")
            break
        else:
            print("Invalid choice")

library()
