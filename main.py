#start game
print('game started')
game_is_running = True
#asking number of players
player_number = 0
while (player_number > 6 or player_number < 1):
    player_number = int(input('how many players (1 to 6): '))

#set all balances to starting value
balances = []
for i in range(0,player_number):
    balances.append(1500)
#define a function to display all balances, only prints
def display_balance(input_list):
    for j in range(0,len(input_list)):
        print('')
        print(f'player{j+1} -- {input_list[j]}')
    print('')
#a way to get a valid player, returns the player number
def get_player():
    input_player_number = 0
    while(input_player_number > len(balances) or input_player_number < 1):
        input_player_number = int(input('which player?: '))
    return(input_player_number)
#a way to get a valid amount, returns the amount
def get_amount():
    amount = -1
    while (int(amount) <= int(0)):
        amount = input('valid amount: ')
    return(int(amount))
#main game loop
while(game_is_running):
    display_balance(balances)
    print('')
    print('possible actions are')
    print('t -- make a transaction')
    print('a -- add balance')
    print('s -- subtract balance')
    print('g -- game over')
    print('')
    action = input('write an action: ')   
    match action:
        case 'a':
            op_player = get_player()
            amount = get_amount()
            #-1 cuz arrays start at zero, add the amount
            balances[op_player - 1] += amount    
        case 's':
            op_player = get_player()
            amount = get_amount()
            if amount > balances[op_player - 1]:
                print('not enough')
            else: 
                balances[op_player_giving - 1] -= amount    
        case 't':
            print('from')
            op_player_giving = get_player()
            print('to')
            op_player_taking = get_player()
            amount = get_amount()
            if amount > balances[op_player_giving - 1]:
                print('not enough')
            else: 
                balances[op_player_taking - 1] += amount
                balances[op_player_giving - 1] -= amount
        case 'g':
            game_is_running = False