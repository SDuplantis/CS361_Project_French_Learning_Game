
import random
import math

def french_dictionary(level):
    """
    Recieves a user level and then returns a random french word along with its translation and two incorrect ones
    :param level: User level
    :return: tuple -> (french_word, translated, wrong_one, wrong_two)
    """
    level_one_to_five = [
        ('Pomme', 'Apple'),
        ('Chien', 'Dog'),
        ('Chat', 'Cat'),
        ('Manger', 'To Eat'),
        ('Rester', 'To Stay'),
        ('Marcher', 'To Walk'),
        ('Gauche', 'Left'),
        ('Droite', 'Right'),
        ('Verte', 'Green'),
        ('Rouge', 'Red'),
        ('Un', 'A or One'),
        ('Deux', 'Two'),
        ('Trois', 'Three'),
        ('Quartre', 'Four')
    ]

    # getting length of list to dynamically pick random number
    level_one_length = len(level_one_to_five)
    # picking random number to get random word
    rng = random.randint(0, level_one_length - 1)

    # French word and translation based on rng
    french_word = level_one_to_five[rng][0]
    translated = level_one_to_five[rng][1]

    # list of chosen random numbers so can pick unique ones...
    chosen = [rng]

    # loop until we have 3 unique randos in chosen
    while len(chosen) < 3:
        new_rng = random.randint(0, level_one_length - 1)
        if new_rng not in chosen:
            chosen.append(new_rng)

    # Voila! our incorrect translations
    wrong_one = level_one_to_five[chosen[1]][1]
    wrong_two = level_one_to_five[chosen[2]][1]

    return french_word, translated, wrong_one, wrong_two

# user_input = 0
# while user_input != 1:
#     user_input = int(input("Enter 0 to get french stuff. 1 to quit.  "))
#     if user_input == 0:
#         print(french_dictionary(1))


