#!/usr/bin/env python3

import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        for bullet in bullets.copy():
        	if bullet.rect.bottom <= 0:
        		bullets.remove(bullet)
        print(len(bullets))

run_game()