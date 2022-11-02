from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user
import csv

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "New User":
        add_user()
        ask_option()
    if (option['main_options']) == "Show Status":
        with open('balance.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if len(row) >= 3:
                    if float(row[1]) >= 0:
                        print(row[0] + " owes nothing")
                    else:
                        print(row[0] + " owes " + str(round(-float(row[1]),2)) + "€ to " + row[2])
                else:
                    print(row[0] + " owes nothing")
        ask_option()

def main():
    ask_option()

main()