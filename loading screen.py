import pygame
import sys
import time
import math
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Splash Screen")

BLACK = (10, 10, 25)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (200, 0, 255)
BLUE = (0, 150, 255)

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 16)
clock = pygame.time.Clock()

# Charger le logo
logo_path = "image/logo.png"
if os.path.exists(logo_path):
    logo = pygame.image.load(logo_path)
    logo = pygame.transform.scale(logo, (150, 150))
    print(f"✓ Logo chargé : {logo_path}")
else:
    print(f"⚠ Logo non trouvé : {logo_path}")

def draw_animated_background(elapsed):
    """Dessine un fond futuriste animé"""
    screen.fill(BLACK)
    
    # Lignes horizontales animées
    for i in range(0, 600, 30):
        offset = (elapsed * 100) % 800
        pygame.draw.line(screen, (40, 60, 100), (0, i), (800, i), 1)
        pygame.draw.line(screen, CYAN, (offset, i), (offset + 100, i), 1)
    
    # Cercles concentriques au centre
    center_x, center_y = 400, 200
    for r in range(50, 300, 40):
        radius = (r + elapsed * 50) % 300
        if radius > 20:
            pygame.draw.circle(screen, (PURPLE if radius % 80 < 40 else CYAN), (center_x, center_y), int(radius), 1)
    
    # Particules en diagonale
    for i in range(10):
        offset = (elapsed * 60 + i * 80) % 1000
        x = (offset - 500) % 900
        y = (offset * 0.6) % 600
        pygame.draw.circle(screen, CYAN, (int(x), int(y)), 2)

def draw_futuristic_logo(elapsed, center_x, center_y):
    """Dessine un logo futuriste animé"""
    # Carré externe qui tourne
    angle = (elapsed * 100) % 360
    size = 100
    
    # Créer une surface pour le carré
    square = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
    
    # Dessiner des carrés imbriqués
    for i in range(3):
        s = size - (i * 20)
        rect = pygame.Rect(square.get_width() // 2 - s, square.get_height() // 2 - s, s * 2, s * 2)
        color = [CYAN, MAGENTA, BLUE][i]
        pygame.draw.rect(square, color, rect, 2)
    
    # Rotation
    rotated = pygame.transform.rotate(square, angle)
    rect = rotated.get_rect(center=(center_x, center_y))
    screen.blit(rotated, rect)
    
    # Diagonales croisées qui clignotent
    flicker = abs(math.sin(elapsed * 5)) > 0.5
    if flicker:
        pygame.draw.line(screen, MAGENTA, (center_x - 80, center_y - 80), (center_x + 80, center_y + 80), 2)
        pygame.draw.line(screen, CYAN, (center_x - 80, center_y + 80), (center_x + 80, center_y - 80), 2)

def splash_screen():
    start_time = time.time()
    duration = 15  # 15 secondes de chargement
    
    # PHASE 1 : Chargement
    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        elapsed = time.time() - start_time
        progress = elapsed / duration  # 0 à 1
        
        # Fond animé
        draw_animated_background(elapsed)
        
        # Logo futuriste
        draw_futuristic_logo(elapsed, 400, 150)
        
        # Barre de progression futuriste
        bar_width = 500
        bar_height = 20
        bar_x = 150
        bar_y = 350
        
        # Fond de la barre
        pygame.draw.rect(screen, (20, 40, 80), (bar_x, bar_y, bar_width, bar_height))
        
        # Barre de progression avec gradient (simulation)
        progress_width = bar_width * progress
        pygame.draw.rect(screen, CYAN, (bar_x, bar_y, progress_width, bar_height))
        pygame.draw.rect(screen, MAGENTA, (bar_x, bar_y, progress_width, bar_height), 2)
        
        # Contour de la barre
        pygame.draw.rect(screen, CYAN, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Texte futuriste
        percentage = int(progress * 100)
        text = font.render(f"> LOADING {percentage}% <", True, CYAN)
        text_rect = text.get_rect(center=(400, 420))
        screen.blit(text, text_rect)
        
        # Texte secondaire
        subtext = small_font.render("∆ FUTURISTIC SPLASH SCREEN ∆", True, MAGENTA)
        subtext_rect = subtext.get_rect(center=(400, 480))
        screen.blit(subtext, subtext_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    # PHASE 2 : Chargement terminé (15 secondes)
    completion_start = time.time()
    completion_duration = 15
    
    while time.time() - completion_start < completion_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        elapsed = time.time() - completion_start
        
        # Fond animé
        draw_animated_background(elapsed)
        
        # Logo futuriste
        draw_futuristic_logo(elapsed, 400, 150)
        
        # Message de completion avec effet de pulsation
        pulse = abs(math.sin(elapsed * 3))
        color_intensity = int(200 + pulse * 55)
        completion_color = (CYAN[0], color_intensity, color_intensity)
        
        text = font.render("✓ CHARGEMENT TERMINÉ ✓", True, completion_color)
        text_rect = text.get_rect(center=(400, 420))
        screen.blit(text, text_rect)
        
        # Texte secondaire
        subtext = small_font.render("∆ READY TO START ∆", True, MAGENTA)
        subtext_rect = subtext.get_rect(center=(400, 480))
        screen.blit(subtext, subtext_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    return True

if splash_screen():
    print("✓ Splash screen terminé")

pygame.quit()
sys.exit()
