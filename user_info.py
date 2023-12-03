
def user_level(points):
    """
    Determines user level based on experience points
    :param points: experience points the user has
    :return: curr_level
    """

    level_list = [
        [50, 1],
        [100, 2],
        [200, 3],
        [400, 4],
        [800, 5],
        [1600, 6],
        [3200, 7],
        [6400, 8],
        [12800, 9],
        [25600, 10],
        [51200, 11],
        [102400, 12],
        [204800, 13],
        [409600, 14],
        [819200, 15],
        [987654321, 16]
    ]

    # retrieve appropriate level based on experience points
    for item in level_list:
        if points <= item[0]:
            return item[1]

    # in case user has crazy amount of xp
    return 19
