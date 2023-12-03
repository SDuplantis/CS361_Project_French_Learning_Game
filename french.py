
# import random
# import math

import socket
import subprocess


def french_dictionary(level):
    """
    Receives a user level and then returns a random French word along with its translation and two incorrect ones
    :param level: User level
    :return: tuple -> (french_word, translated, wrong_one, wrong_two)
    """

    # # location of microservice script
    # micro_service = 'C:/Users/Steven/Documents/01 School (OSU)/CS 361/Assignments/TBA_MS/tba_MS.py'
    # # Calling on microservice to start
    # subprocess.Popen(['python', micro_service])

    # Set up connection
    my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5544
    my_server.connect((host, port))

    # determining message to send to microservice
    if level <= 5:
        french_lvl = 'level_one_to_five'
    elif level <= 10:
        french_lvl = 'level_six_to_ten'
    else:
        french_lvl = 'level_eleven_to_fifteen'

    # sending level text to microservice
    my_server.send(french_lvl.encode())

    french_binary = my_server.recv(4096)
    french_decode = french_binary.decode('utf-8')
    french_list = eval(french_decode)
    print(french_list)
    french_word, translated, wrong_one, wrong_two = french_list

    print(french_word, translated, wrong_one, wrong_two)
    # closing connection
    my_server.close()

    return french_word, translated, wrong_one, wrong_two
