import json, datetime

def menu():
    while True:
        print('\n============== EXPENSE TRACKER ==============\n')

        print('1. Add an expense \n2. View expenses \n3. Show total spending \n4. Filter by category \n5. Edit expense \n6. Delete expense \n7. Exit \n')

        choice = input('Choose an option: ')
        if choice == '1':

            for dict in user_data:
                category = input('Input category: ')

                if category != list(dict.keys())[0]:
                   amount, description, time = request_input()
                    
                   add_expense(category, amount, description, time)
                   break
                    
                else:
                    print('-'*40)
                    print(f'category {category} already exists')
                    option = input('Would you like to add an entry to it ? y/n: ')
                    if option == 'y':
                        amount, description, time = request_input()

                        add_expense_entry(category, amount, description, time)
                        break

                        

        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_total_spending()

        elif choice == '4':
            filter_by_cat()


def load_data():
    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

user_data = load_data()
# print(user_data)
expense = {}

def add_expense(category, amount, description, date):
    expense_data = []
    expense_data.append({'amount': amount, 'description': description, 'date/time': str(date)})
    expense[category] = expense_data
    user_data.append(expense)

    dump_data(user_data)

def request_input():
    amount = input('Enter amount: ')
    description = input('enter a description: ')
    time_choice = input('would you like to log in the current time or a time of your choosing. y/n? ')
    if time_choice == 'n':
        time = input('Enter date/time(yyyy-mm-dd HH:MM): ')
    elif time_choice == 'y':
        time = datetime.datetime.now()
    else:
        print('invalid input')

    return amount, description, time

def add_expense_entry(category, amount, description, date):
    for dict in user_data:
        if category == list(dict.keys())[0]:
            expense_data = list(dict.values())[0]
            expense_data.append({'amount': amount, 'description': description, 'date/time': str(date)})
            expense[category] = expense_data
            dump_data(user_data)





       

def dump_data(user_data: list):
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(user_data, file, indent=4)

def empty_entry():
    if len(user_data) == 0:
        return True


def view_expenses():
    if not empty_entry():
    
        for diction in user_data:
            for key, val in diction.items():
                print(f'\n====================== category: {key} =====================\n')
                print(f'amount: {val['amount']}\ndescription: {val['description']}\nDate of entry: {val['date/time']}\n')
    else:
        print("There's no entry at the moment")

        

def show_total_spending():
    if not empty_entry():
        print("-"*40)
        print(' '*15, 'TOTAL SPENDING: ')
        total = 0
        for dict in user_data:
            amount = list(dict.values())[0]['amount']
            total+= int(amount)
        print(f'${total}')

def view_all_categories():
    if not empty_entry:
        print('-'*40)
        print(' '*15, 'Categories: ')
        num = 1
        for dict in user_data:
            cat = list(dict.keys())[0]
            print(f'{num}. {cat}')
            num+=1

def filter_by_cat():
    view_all_categories()

    category = input('\nSelect a category: ')
    print('\n')
    for dict in user_data:
        if category == list(dict.keys())[0]:
            print(f'--------------- {category} ------------------')
            print(f'- Amount: ${dict[category]['amount']}')
            print(f'- Description: ${dict[category]['description']}')
            print(f'- Date/time: ${dict[category]['date/time']}')





            


        



menu()









