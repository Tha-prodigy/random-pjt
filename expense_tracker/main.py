import json, datetime

def menu():
    while True:
        print('\n============== EXPENSE TRACKER ==============\n')

        print('1. Add an expense \n2. View expenses \n3. Show total spending \n4. Filter by category \n5. Edit expense \n6. Delete expense \n7. Exit \n')

        choice = input('Choose an option: ')
        if choice == '1':
            categories = []
            
            category = input('Input category: ')
            
            for dict in user_data:
                categories.append( list(dict.keys())[0])
                
                
            if category in categories:
                
                print('-'*40)
                print(f'category {category} already exists')
                option = input('Would you like to add an entry to it ? y/n: ')
                if option == 'y':
                    amount, description, time = request_input()

                    add_expense_entry(category, amount, description, time)
                
                
            else:
                # print(list(dict.keys())[0]) 
                                    
                amount, description, time = request_input()
                
                add_expense(category, amount, description, time)
                   
                               

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            show_total_spending()

        elif choice == '4':
            filter_by_cat()
            
        elif choice == '5':
            edit_expense()
        elif choice== '6':
            delete_expense()

        elif choice=='7':
            return


def load_data():
    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

user_data = load_data()
print(user_data)

def add_expense(category, amount, description, date):
    expense = {}
    
    expense_data = []
    expense_data.append({'amount': amount, 'description': description, 'date/time': str(date)})
    expense[category] = expense_data
    user_data.append(expense)

    dump_data(user_data)
    

def request_input():
    try:
        amount = int(input('Enter amount: '))
    except:
        print('invalid amount entry')
        return
    
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
    expense = {}
    
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
    else:
        return False


def view_expenses():
    if not empty_entry():
    
        for diction in user_data:
            category = list(diction.keys())[0]
            category_val = list(diction.values())[0]
            print(f'\n====================== category: {category} =====================\n')
            for val in category_val:
                print(f"- Amount: ${val["amount"]}\n- Description: {val["description"]}\n- Date/time: {val["date/time"]} ")
                print('-'*40)       
                
                
    else:
        print("There's no entry at the moment")

        

def show_total_spending():
    if not empty_entry():
        print("-"*40)
        print(' '*15, 'TOTAL SPENDING: ')
        total = 0
        for dict in user_data:
            val_list = list(dict.values())[0]
            for val in val_list:
                total += int(val['amount'])
                
            
        print(f'- ${total}')

def view_all_categories():
    num = 1

    if not empty_entry():
        
        print('-'*40)
        print(' '*15, 'Categories: ')
        for dict in user_data:
            cat = list(dict.keys())[0]
            print(f'{num}. {cat}')
            num +=1

    else:
        print("There's no entry at the moment")
        return

            
def view_category_entry(category):
    num = 1
   
    cat_val = []
    for dic in user_data:
        if category == list(dic.keys())[0]:
            print(f'---------------------- {category} entry ----------------------\n')
            print("   "+format("Amount", '<10') + '| ' + format("Description", '<20') + '| ' + format("Time of entry", '<10') )
        
            entries = dic[category] 
            for val in entries:
                print(f"{num}. {val['amount']:<10}| {val['description']:<20}| {val['date/time']:<10}")
                num+=1
            cat_val = list(dic.values())[0]
            
            return cat_val
        else:
            continue
    print('\nThe categgory you entered does not exists...')
    return cat_val
                   
        

def filter_by_cat():
    view_all_categories()

    category = input('\nSelect a category: ')
    print('\n')
    for dic in user_data:
        if category == list(dic.keys())[0]:
            print(f'\n--------------- {category} ------------------')
            for val in list(dic.values())[0]:
                print(f'- Amount: ${val['amount']}')
                print(f'- Description: {val['description']}')
                print(f'- Date/time: {val['date/time']}')
                print('--------------------------------------------')
            return
        else:
            print('The category you entered does not exist')
            return
        
def edit_expense():
    view_all_categories()
    category = input('\nSelect a category: ')
    entries  = view_category_entry(category)
    try:
        entry_index = int(input("\nChoose an entry by it's numbering: "))
    except:
        print('invalid entry')
        return
    field = input("input the category field you'd like to modify: ")
    new_entry = input('Enter your new entry: ')
    # entries = []
    
    print(entries)
        
    # print(entries)
    if entry_index >0 and entry_index <= len(entries): 
        entries[entry_index-1][field] = new_entry
        dump_data(user_data)
        # print('new entry: ',entries)
        
        print('Entry has been successfully edited')
        return
    else:
        print('You selected a non existent entry')
        return


def delete_expense():

    option = input("select delete format\n1. By category\n2. By category entry\nchoice: ")
    if option == '1':
        view_all_categories()

        try:
            entry_index = int(input("\nChoose the category of expense you'd like to delete by it's numbering: "))
        except:
            print('invalid entry')
            return
        if entry_index >0 and entry_index <= len(user_data): 
        
            exp = user_data.pop(entry_index-1)
            print(f"\nCategory {list(exp.keys())[0]} has been succesfully deleted")
            dump_data(user_data)

        else:
            print('You selected a non existent entry')
            return

    elif option == '2':
        view_all_categories()

        category = input('\n Choose a category among the above: ')

        cat_entry = view_category_entry(category)
        if cat_entry != []:
            try:
                entry_index = int(input("\nChoose an entry by it's numbering: "))
            except:
                print('invalid entry')
                return
            if entry_index >0 and entry_index <= len(cat_entry):
                val = cat_entry.pop(entry_index-1) 
                print('Entry deletion succesfull')
                dump_data(user_data)
    
    

menu()









