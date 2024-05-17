import random as rd
while True:
    print(' Rock -> Scissor \n Scissor -> Paper \n Paper -> Scissor')
    running = True
    while running:
        print('You Can Choose Between THIS: \n 1 - Rock \n 2 - Paper \n 3 - Scissor')
        choose = input('Choose between 1 and 3: ')
        if choose.isdigit():
            choose = int(choose)
            break
        else:
            print('Please enter a number//')

    while choose > 3 or choose <1:
        choose = int(input('Enter a valid number: '))
    if choose == 1:
        choose_name = 'Rock'
    elif choose == 2:
        choose_name = 'Paper'
    elif choose == 3:
        choose_name = 'Scissor'
    print('Your choice is: ',choose_name)

    comp_choice = rd.randint(1,3)
    while comp_choice == choose_name:
        comp_choice = rd.randint(1,3)
    if comp_choice == 1:
        comp_name1 = 'Rock'
    elif comp_choice == 2:
        comp_name1 = 'Paper'
    elif comp_choice == 3:
        comp_name1 = 'Scissor'
    print('Computer choice is: ',comp_name1)

    if choose == comp_choice:
        print('<-DRAW->')
    if choose == 1 and comp_choice == 2:
        print(f'<{comp_name1} win {choose_name}> \n COMPUTER WINN~~!')
    elif choose == 2 and comp_choice == 1:
        print(f'<{choose_name} win {comp_name1}> \n YOU WINN~~!')
    if choose == 2 and comp_choice == 3:
        print(f'<{comp_name1} win {choose_name}> \n COMPUTER WINN~~!')
    elif choose == 3 and comp_choice == 2:
        print(f'<{choose_name} win {comp_name1}>\n YOU WINN~~!')
    if choose == 3 and comp_choice == 1:
        print(f'<{comp_name1} win {choose_name}> \n COMPUTER WINN~~!')
    elif choose == 1 and comp_choice == 3:
        print(f'<{choose_name} win {comp_name1}> \n, YOU WINN~~!')

    ans = input('Do u want to play again? Y/N :')
    ans = ans.lower()
    if ans == 'y':
        ans == running
    else:
        break
print('Thank you for playing~! ')


