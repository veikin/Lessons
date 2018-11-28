users = ['andrei']
current_users = ['vala', 'jhon', 'dima', 'oleg', 'olya']
new_users = ['kate', 'sveta', 'JHON', 'oleg', 'tolik']

if len(users) == 0:
    print("We need to find some users!")

for user in users:
    if user == 'andrei':
        print("Hello " + user.title() + 
                ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + 
                ", thank you for logging in again.")

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Ужe есть пользователь с таким именем")
    else:
        print("Имя доступно")
