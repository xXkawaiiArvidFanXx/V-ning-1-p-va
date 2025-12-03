from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated*", category=UserWarning)

import pygame


def sound(filväg):
    """Spelar en ljudfil. Skicka in sökvägen till filen som en sträng.
    Exempel: sound("ljud/kiosken.wav")"""
    pygame.init()
    
    try:
        ljud = pygame.mixer.Sound(filväg)
        ljud.play()
        
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Kunde inte spela ljud: {e}")


# Exempel på hur man använder funktionen:
sound("ljud/kiosken.wav")