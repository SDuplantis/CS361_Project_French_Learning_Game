

class Enemy:
    """
    Enemy object used in TBA game
    """

    def __init__(self, number):
        """
        Initializing private variables
        :param number:
        """
        self._enemy_num = number
        self._image_dir = 'C:/Users/Steven/Documents/01 School (OSU)/CS 361/Assignments/TBA/images'

    def get_image(self):

        return self._image_dir + '/Creature0' + str(self._enemy_num) + '.jpg'
