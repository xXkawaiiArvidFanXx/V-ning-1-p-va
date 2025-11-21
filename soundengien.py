from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated*", category=UserWarning)

import pygame


def sound(filväg):
    """Högerklickar på ljudfilen och tryck på "Copy reletive path" och klistra in den inom paranteserna med citattecken."""
    pygame.init()


    ljud = pygame.mixer.Sound(filväg)

    ljud.play()

    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)



#Exempel sound("ljud\kiosken.wav")