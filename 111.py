desk = list(range(1, 10))
def draw_desk(desk):
    for i in range(3):
        print (desk[0+i*3], desk[1+i*3], desk[2+i*3])
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Вводить только числа")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(desk[player_answer-1]) not in "XO"):
                desk[player_answer-1] = player_token
                valid = True
        else:
            print ("Вводить только числа")
def check_win(desk):
    win_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_combination:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            return desk[each[0]]
    return False
def main(desk):
    counter = 0
    win = False
    while not win:
        draw_desk(desk)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(desk)
            if tmp:
                print (tmp, "Победа")
                win = True
                break
        if counter == 9:
            print ("Ничья")
            break
    draw_desk(desk)
main(desk)