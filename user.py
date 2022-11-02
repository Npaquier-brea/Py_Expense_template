from PyInquirer import prompt
import csv

user_questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'Yo, what\'s your name young blood ?',
    }
]

def add_user():
    infos = prompt(user_questions)
    filename = "users.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        tmp_data = [infos['name']]
        csvwriter.writerow(tmp_data)
    print("User Added !")
    return True