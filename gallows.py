from random import choice

WORDS_FILENAME = 'words.txt'
PLAYERS_FILENAME = 'players.txt'

gallows = [['-', '-', '-', '-', '-', '-'],
           [' ', '|', ' ', ' ', '|', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['/', ' ', '\\', ' ', ' ', ' ']]

def draws_gallows(error_nums=0):
    
    def draw():
        str_gallows = ''
        for lst in gallows:
            str_gallows += ''.join(lst) + '\n'
        return str_gallows
    
    match error_nums:
        case 1:
            gallows[2][4] = 'O'
        case 2:
            gallows[3][3] = '/'
        case 3:
            gallows[3][4] = '|'
        case 4:
            gallows[3][5] = '\\'
        case 5:
            gallows[4][3] = '/'
        case 6:
            gallows[4][5] = '\\'
  
    return draw()

def find_all(text:str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result

def get_random_word():
    words = []
    with open(WORDS_FILENAME) as fd:
        words = fd.read().split('\n')
    return choice(words)


def get_player_score(player_name):
    players = []
    try:
        with open(PLAYERS_FILENAME) as fd:
            players = fd.read().split('\n')
    except FileNotFoundError:
        return 0
    
    for rec in players:
        if rec.startswith(player_name):
            return int(rec.split(' ')[1])
    return 0

def write_score(player_name, score):
    players = []
    try:
        with open(PLAYERS_FILENAME) as fd:
            data = fd.read().strip()
            if data:
                players = data.split('\n')
    except FileNotFoundError:
        pass
    
    is_find = False
    
    for i, rec in enumerate(players):
        if rec.startswith(player_name):
            score += int(rec.split(' ')[1])
            players[i] = f"{player_name} {score}"
            is_find = True
    
    if not is_find:
        players.append(f"{player_name} {score}")
    
    with open(PLAYERS_FILENAME, 'w') as fd:
        fd.writelines([player + '\n' for player in players])
    
    
def main():
    player_name = input("Take your name >>>")
    score = get_player_score(player_name)
    print(f'Hello {player_name}, your score {score}')
    word = get_random_word() #choice(["pizza", "lasagna", "banana", "shaurma", "burger", "borsch"])
    answer_word = ["_" for _ in range(len(word))]
    errors_count = 0
    lose = False
    
    def print_state(errors_count=0):
        print(draws_gallows(errors_count))
        print(" ".join(answer_word))

    print_state()
    
    
    while "".join(answer_word) != word:        
        user_input = input("Type your letter >>>").lower()
        
        if user_input in word:
            letter_indexes = find_all(word, user_input)
            for i in letter_indexes:
                answer_word[i] = user_input
            print_state()
        else:
            errors_count += 1
            print_state(errors_count)

        if errors_count >= 6:
            lose = True
            break
    if lose:
        print("Game over \nYou lose!!!")
        write_score(player_name, -5)
    else:
        print("You win!!!")
        
        write_score(player_name, 5)       
        # try:
        #     with open('winner.txt', 'x') as fd:
        #         fd.write(f'{player_name} 5\n')
        # except FileExistsError:
        #     with open('winner.txt', 'a') as fd:
        #         fd.write(f'{player_name} 5\n')
              

if __name__ == "__main__":
    main()
