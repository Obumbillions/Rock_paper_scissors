import random
options = ['R', 'P', 'S']
options_value = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}

print("Welcome.\nTo play, please enter R for rock, P for paper, S for scissors")

while True:
    player_choice = input(" ")
    while player_choice not in options:
        print("Invalid option. Please select between R, P, and S")
        player_choice = input(" ")
        continue

    CPU_choice = random.choice(options)
    print("Player(%s): CPU (%s)" % (options_value[player_choice], options_value[CPU_choice]))
    

    if player_choice == CPU_choice:
        print("Game tie. Please select between R, P, and S")
        continue
    elif player_choice == 'R' and CPU_choice == 'S' or player_choice == 'P' and CPU_choice == 'R' or player_choice == 'S' and CPU_choice == 'P':
        print("Winner: Player\nGame over")
        break
    else:
        print("Winner: CPU\nGame over")
        break