
import sys
import pygame
from pygame.locals import *
import time
import random
from enemy import Enemy
from french import french_dictionary
from user_info import user_level

# global variables to move
screen_width = 800
screen_height = 600
white = (255, 255, 255)
black = (0, 0, 0)

# File paths to be moved later, inside Game class
save_file = 'C:/Users/Steven/Documents/01 School (OSU)/CS 361/Assignments/TBA/00_saves.txt'
char_file = 'C:/Users/Steven/Documents/01 School (OSU)/CS 361/Assignments/TBA/00_char.txt'
pic_folder = 'C:/Users/Steven/Documents/01 School (OSU)/CS 361/Assignments/TBA/images'


class Game:

    def __init__(self):
        """
        Initial values for Game class
        """

        # Pygame settings
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = screen_width, screen_height
        self._fps = 60
        self._frame_per_sec = pygame.time.Clock()

        # Background and layer images
        self._background_main_menu = pygame.image.load(pic_folder + "/background2.jpg")
        self._background_load_menu = pygame.image.load(pic_folder + "/background3.jpg")
        self._background_game_intro = pygame.image.load(pic_folder + "/background4.jpg")
        self._background_defeat = pygame.image.load(pic_folder + "/correct01.jpg")
        self._corridor_01 = pygame.image.load(pic_folder + "/Corridor01a.jpg")
        self._corridor_selection = ''
        self._corridor_count = 3
        self._button = pygame.image.load(pic_folder + '/button01.jpg')

        # Navigation variables
        self._pathing_type = 'a'
        self._pathing = 1
        self._pathing_count = 0

        # Other variables
        self._quit_mess = None
        self._rng_number = None
        self._rng_txt = None
        self._rng_pic = None

        # Fonts
        self._font = None
        self._font_small = None

        # Screen checks
        self._main_menu_chk = True
        self._load_menu_chk = False
        self._game_intro_chk = False
        self._defeat_chk = False
        self._combat_rng = 0
        self._combat_chk = False

        # Enemy variables
        self._enemy_max = 7
        self._enemy_image = ''
        self._enemy_background = None
        self._enemy_num = None
        self._enemy_guy = None

        # Translation variables
        self._french_word = ''
        self._translation = ''
        self._wrong_one = ''
        self._wrong_two = ''
        self._correct_answer = 0

        # XP and Level
        self._user_xp = 0
        self._user_level = 1
        self._xp_anim = 0

    def on_event(self, event):
        # checking if event type is quit, if so, change self._running
        if event.type == pygame.QUIT:
            self._running = False

    def on_initialization(self):

        # initializing pygame instance
        pygame.init()

        # Creates main display of self.size and uses hardware acceleration
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(white)

        # Title of Game in the top portion of border
        pygame.display.set_caption("Revinir's Lament")

        # Setting running to true
        self._running = True

        # Setting text for future messages
        self._font = pygame.font.SysFont("Verdana", 40)
        self._font_small = pygame.font.SysFont("Verdana", 20)
        self._quit_mess = self._font.render("Goodbye!", True, black)

    def main_menu_loop(self):

        pressed_keys = pygame.key.get_pressed()

        # Quit UI App
        if pressed_keys[K_ESCAPE] or pressed_keys[K_q]:
            self.on_cleanup()

        # Load menu keystroke
        if pressed_keys[K_l]:
            self._main_menu_chk = False
            self._load_menu_chk = True
            time.sleep(0.25)

        # Load menu keystroke
        if pressed_keys[K_n]:
            self._main_menu_chk = False
            self._game_intro_chk = True
            time.sleep(0.25)

        # Load menu keystroke
        if pressed_keys[K_m]:
            self.stop_music()
            time.sleep(0.25)

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            # New Game button press (x range) and (y range)
            if (mouse_pos[0] > 50 and mouse_pos[0] < 233) and (mouse_pos[1] > 478 and mouse_pos[1] < 524):
                self._main_menu_chk = False
                self._game_intro_chk = True
                time.sleep(0.25)

            # Load game button press (x range) and (y range)
            if (mouse_pos[0] > 308 and mouse_pos[0] < 489) and (mouse_pos[1] > 478 and mouse_pos[1] < 524):
                self._main_menu_chk = False
                self._load_menu_chk = True
                time.sleep(0.25)

            # Quit button press (x range) and (y range)
            if (mouse_pos[0] > 555 and mouse_pos[0] < 740) and (mouse_pos[1] > 478 and mouse_pos[1] < 524):
                self.on_cleanup()

    def load_menu_loop(self):

        pressed_keys = pygame.key.get_pressed()

        # checking if b button has been pressed to go back to main menu
        if pressed_keys[K_b]:
            self._main_menu_chk = True
            self._load_menu_chk = False
            time.sleep(0.25)

        # checking if mouse button has been pressed
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            # Back to main menu button press (x range) and (y range)
            if (mouse_pos[0] > 265 and mouse_pos[0] < 510) and (mouse_pos[1] > 435 and mouse_pos[1] < 500):
                self._main_menu_chk = True
                self._load_menu_chk = False
                time.sleep(0.25)

    def game_intro(self):

        pressed_keys = pygame.key.get_pressed()

        # checking if c button is pressed, brings user to main game
        if pressed_keys[K_c]:
            self._game_intro_chk = False
            time.sleep(0.25)

        # checking if mouse button has been pressed
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            # Back to main menu button press (x range) and (y range)
            if (mouse_pos[0] > 296 and mouse_pos[0] < 506) and (mouse_pos[1] > 472 and mouse_pos[1] < 527):
                self._game_intro_chk = False
                time.sleep(0.25)

    def defeat_loop(self):

        pressed_keys = pygame.key.get_pressed()

        # checking if c button is pressed, brings user to main game
        if pressed_keys[K_c]:
            self._defeat_chk = False
            time.sleep(0.25)

        # checking if mouse button has been pressed
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            # Back to main menu button press (x range) and (y range)
            if (mouse_pos[0] > 296 and mouse_pos[0] < 506) and (mouse_pos[1] > 472 and mouse_pos[1] < 527):
                self._defeat_chk = False
                time.sleep(0.25)

    def main_menu_render(self):

        # display background and button
        self._display_surf.blit(self._background_main_menu, (0, 0))

        title_text = ''

        # setting up font objects
        text_01 = self._font.render(str(title_text), True, black)

        # # creating display surfaces for text
        self._display_surf.blit(text_01, (111, 25))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def load_menu_render(self):

        self._display_surf.blit(self._background_load_menu, (0, 0))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def game_intro_render(self):

        self._display_surf.blit(self._background_game_intro, (0, 0))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def defeat_render(self):
        self._display_surf.blit(self._background_defeat, (0, 0))

        # logic for xp animation
        if self._xp_anim < 2:
            user_xp_total = 'Total XP earned: ' + str(int(round(self._user_xp / 10, 0)))
            self._xp_anim += 1
        elif self._xp_anim < 4:
            user_xp_total = 'Total XP earned: ' + str(int(round(self._user_xp / 8, 0)))
            self._xp_anim += 1
        elif self._xp_anim < 6:
            user_xp_total = 'Total XP earned: ' + str(int(round(self._user_xp / 6, 0)))
            self._xp_anim += 1
        elif self._xp_anim < 8:
            user_xp_total = 'Total XP earned: ' + str(int(round(self._user_xp / 4, 0)))
            self._xp_anim += 1
        elif self._xp_anim < 10:
            user_xp_total = 'Total XP earned: ' + str(int(round(self._user_xp / 2, 0)))
            self._xp_anim += 1
        else:
            user_xp_total = 'Total XP earned: ' + str(self._user_xp)

        # setting up font objects
        text_01 = self._font.render(str(user_xp_total), True, black)

        text_02 = self._font.render('Current level: ' + str(self._user_level), True, black)

        # creating display surfaces for text
        self._display_surf.blit(text_01, (200, 300))
        self._display_surf.blit(text_02, (250, 350))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def combat_loop(self):

        pressed_keys = pygame.key.get_pressed()

        # Quit UI App
        if pressed_keys[K_ESCAPE] or pressed_keys[K_q]:
            self.on_cleanup()

        # Logic when user makes a selection
        # exit combat and enter defeat (if correct selection) and update user xp/level
        if pressed_keys[K_1]:
            if self._correct_answer == 1:
                self._combat_chk = False
                self._defeat_chk = True
                self._user_xp += 10
                self._xp_anim = 0
                self._user_level = user_level(self._user_xp)
            else:
                self.random_translation()
            time.sleep(0.25)

        if pressed_keys[K_2]:
            if self._correct_answer == 2:
                self._combat_chk = False
                self._defeat_chk = True
                self._user_xp += 10
                self._xp_anim = 0
                self._user_level = user_level(self._user_xp)
            else:
                self.random_translation()
            time.sleep(0.25)

        if pressed_keys[K_3]:
            if self._correct_answer == 3:
                self._combat_chk = False
                self._defeat_chk = True
                self._user_xp += 10
                self._xp_anim = 0
                self._user_level = user_level(self._user_xp)
            else:
                self.random_translation()
            time.sleep(0.25)

        self._enemy_image = self._enemy_guy.get_image()

    def combat_render(self):

        # display enemy
        self._enemy_background = pygame.image.load(self._enemy_image)
        self._display_surf.blit(self._enemy_background, (0, 0))

        self._display_surf.blit(self._button, (15, 525))
        self._display_surf.blit(self._button, (280, 525))
        self._display_surf.blit(self._button, (545, 525))

        fw_text = 'Creature: ' + self._french_word
        tran_text = '(1)' + self._translation
        w1_text = '(2)' + self._wrong_one
        w2_text = '(3)' + self._wrong_two

        # setting up font objects
        text_01 = self._font_small.render(str(fw_text), True, black)
        text_02 = self._font_small.render(str(tran_text), True, black)
        text_03 = self._font_small.render(str(w1_text), True, black)
        text_04 = self._font_small.render(str(w2_text), True, black)

        # creating display surfaces for text
        self._display_surf.blit(text_01, (30, 500))
        self._display_surf.blit(text_02, (85, 540))
        self._display_surf.blit(text_03, (350, 540))
        self._display_surf.blit(text_04, (615, 540))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def random_translation(self):
        # get French word, translation, and two incorrect translations
        self._french_word, self._translation, self._wrong_one, self._wrong_two = french_dictionary(1)
        listo = [random.randint(1, 999999), random.randint(1, 999999), random.randint(1, 999999)]
        frencho = [self._translation, self._wrong_one, self._wrong_two]
        listo, frencho = zip(*sorted(zip(listo, frencho)))
        self._correct_answer = 0
        count = 1
        for item in frencho:
            # print(item, self._translation)
            if item == self._translation:
                self._correct_answer = count
            else:
                count += 1

        self._translation, self._wrong_one, self._wrong_two = frencho

    def on_loop(self):

        pressed_keys = pygame.key.get_pressed()

        # Quit UI App
        if pressed_keys[K_ESCAPE] or pressed_keys[K_q]:
            self.on_cleanup()

        # asdw key presses
        if pressed_keys[K_w] or pressed_keys[K_a] or pressed_keys[K_f] or pressed_keys[K_d]:
            if random.randint(1, 9) > 7:
                self._combat_chk = True
                self._enemy_num = random.randint(1, self._enemy_max)
                self._enemy_guy = Enemy(self._enemy_num)
                self.random_translation()
                time.sleep(0.25)
            else:
                self._pathing = max((self._pathing + 1) % (self._corridor_count + 1), 1)
                time.sleep(0.25)

        # arrow key presses
        if pressed_keys[K_UP] or pressed_keys[K_DOWN] or pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
            if random.randint(1, 9) > 7:
                self._combat_chk = True
                self._enemy_num = random.randint(1, self._enemy_max)
                self._enemy_guy = Enemy(self._enemy_num)
                self.random_translation()
                time.sleep(0.25)
            else:
                self._pathing = max((self._pathing + 1) % (self._corridor_count + 1), 1)
                time.sleep(0.25)

    def on_render(self):
        """
        Renders the corridors
        :return:
        """

        # Need to create a class for random background generation
        # as there are 60 fps, there are 10 frames for each generation
        if self._pathing_count < 10:
            self._pathing_type = 'a'
        elif self._pathing_count < 20:
            self._pathing_type = 'b'
        elif self._pathing_count < 30:
            self._pathing_type = 'c'
        else:
            self._pathing_count = 0
            self._pathing_type = 'a'
        self._pathing_count += 1

        # Adding together variables for image path
        image_path = pic_folder + '/Corridor0' + str(self._pathing) + str(self._pathing_type) + '.jpg'
        self._corridor_01 = pygame.image.load(image_path)
        self._display_surf.blit(self._corridor_01, (0, 0))

        # updates the screen with all the commands up to this point
        pygame.display.update()

        # make sure this only occurs 60 times per second
        self._frame_per_sec.tick(self._fps)

    def on_cleanup(self):

        # Create black surface and update screen
        self._display_surf.fill(black)
        pygame.display.update()

        # wait and then quit out
        time.sleep(0.25)
        pygame.quit()
        sys.exit()

    def on_execute(self):
        """
        Method that controls music and which screen user is on
        return: nothing
        """
        if self.on_initialization() is False:
            self._running = False

        self.play_music()

        # logic for which screen user should be directed to
        while self._running:
            self.run_events()
            if self._main_menu_chk:
                self.main_menu_loop()
                self.main_menu_render()
            elif self._load_menu_chk:
                self.load_menu_loop()
                self.load_menu_render()
            elif self._game_intro_chk:
                self.game_intro()
                self.game_intro_render()
            elif self._combat_chk:
                self.combat_loop()
                self.combat_render()
            elif self._defeat_chk:
                self.defeat_loop()
                self.defeat_render()
            else:
                self.on_loop()
                self.on_render()
        self.on_cleanup()

    def run_events(self):
        # Run all current events
        for event in pygame.event.get():
            self.on_event(event)

    def play_music(self):
        # Initializing mixer, loading song, and playing on infinite loop
        pygame.mixer.init()
        pygame.mixer.music.load('01_Main_Menu.wav')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.1)

    def stop_music(self):
        # Stops all music
        pygame.mixer.music.stop()


if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute()
