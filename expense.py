from PyInquirer import prompt
import csv


users = []
users_checkbox = []

with open('users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    for row in csv_reader:
        users.append(row[0])
        users_checkbox.append({'name': row[0]})
        
print(users)

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        'choices':users
    },
    {
        "type":"checkbox",
        "name":"users_involved",
        "message":"New Expense - Users Involved: ",
        "choices":users_checkbox
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    filename = "expense_report.csv"
    with open(filename, 'a') as csvfile:
        tmp_data = [infos['amount'], infos['label'], infos['spender']]
        csvwriter = csv.writer(csvfile)
        for user_involved in infos['users_involved']:
            tmp_data.append(user_involved)
        csvwriter.writerow(tmp_data)
    print("Expense Added !")
    return True


