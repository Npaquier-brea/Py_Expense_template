from PyInquirer import prompt
import csv


users = []
users_checkbox = []

with open('users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        users.append(row[0])
        users_checkbox.append({'name': row[0]})
        
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
        'choices':users,
    },
    {
        "type":"checkbox",
        "name":"users_involved",
        "message":"New Expense - Users Involved: ",
        "choices":users_checkbox,
    },
]

def calculate_balance(amount, nb_users, users, spender):
    balance = []
    amount_spender = amount / nb_users * (nb_users - 1)
    amount_users_involved =  0 - amount / nb_users
    balance.append({'name': spender,'balance': str(amount_spender)})
    for user in users:
        balance.append({'name': user,'balance': str(amount_users_involved), 'spender': spender})
    return balance
    
def new_expense(*args):
    infos = prompt(expense_questions)
    filename1 = "expense_report.csv"
    filename2 = "balance.csv"
    with open(filename1, 'a') as csvfile:
        tmp_data = [infos['amount'], infos['label'], infos['spender']]
        csvwriter = csv.writer(csvfile)
        for user_involved in infos['users_involved']:
            tmp_data.append(user_involved)
        csvwriter.writerow(tmp_data)
        csvfile.close()
    with open(filename2, 'a') as csvfile:
        #infos['users_involved'].remove(infos['spender'])
        csvwriter = csv.writer(csvfile)
        balance = calculate_balance(int(infos['amount']), len(infos['users_involved']), infos['users_involved'], infos['spender'])
        for elm in balance:
            csvwriter.writerow([elm['name'], elm['balance']])
        csvfile.close()
    print("Expense Added !")
    return True


