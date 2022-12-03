
import sys

def outcome_score(their_move, my_move):
    # 0.75 * (2((m-n) % 3 + (-1 ^ ((m -n) % 3))) + -1 ^ ((m -n) % 3) + abs(-1 ^ ((m -n) % 3)) )
    # 0 They win
    # 3 draw
    # 6 I win 
    score_difference = character_value(their_move) - shape_score(my_move)
    mod_score_difference = score_difference % 3
    negative_if_they_won = pow(-1, mod_score_difference)
    p = mod_score_difference + negative_if_they_won
    q = negative_if_they_won + abs(negative_if_they_won)
    return 0.75 * (2*p + q)

def shape_score(my_move):
    return character_value(my_move) - 23


def character_value(character):
    unicode_point = ord(character.lower())
    character_index = unicode_point - 96
    return character_index

def main():
    try: 
        filename = sys.argv[1]
    except IndexError: 
        print('Missing argument: file name')
        return 

    cumulative_score = 0

    with open(filename, encoding ='utf-8') as f:
        for line in f:
            their_move, my_move = line.split()
            round_score = outcome_score(their_move, my_move) + shape_score(my_move)
            cumulative_score += round_score
    
    print("Final score: ", cumulative_score)


if __name__ == "__main__":
   main()