sandwich_orders = ['french dip', 'pastrami', 'egg salad', 'pastrami', 
                    'dagwood', 'caprese', 'pastrami']

finished_sandwiches = []
past = print("\nPastrami is over")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    completed_sandwich = sandwich_orders.pop()
    
    print("I made your: "+ completed_sandwich.title() + " sandwich!")
    finished_sandwiches.append(completed_sandwich)
    

print("\nFinished sandwiches are: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
