import pygame,random
pygame.mixer.init()
"""
files = [pygame.mixer.music.load('Ipl_Trumpet.mp3'),pygame.mixer.music.load('preview.mp3')]
file_index = 0
"""

pygame.mixer.music.load('Ipl_Trumpet.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.mixer.music.load('preview.mp3')
pygame.mixer.music.play()




