import pygame, sys

ancho = 800
alto = 600
centro= (ancho // 2 , alto // 2)
FPS = 25
SPEED = 15
ROJO= (255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AMARILLO=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
CUSTOM=(72,134,232)

pygame.init()
display = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi Primer Juego")
clock= pygame.time.Clock()
gravedad = True

pepe = pygame.surface.Surface((120,80))
pepe.fill(CYAN)
rect_pepe = pepe.get_rect()
rect_pepe.center = centro

while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill(CUSTOM)
    
    if gravedad:
        if rect_pepe.bottom <= alto:
            rect_pepe.centery = rect_pepe.centery + SPEED
        else:
            gravedad=False
    else:
        if rect_pepe.top >= 0:
            rect_pepe.centery = rect_pepe.centery - SPEED 
        else:
            gravedad = True
    print(rect_pepe.y)
    

    display.blit(pepe,rect_pepe)
    pygame.draw.line(display,NEGRO,(ancho // 2 ,0 ),( ancho // 2,alto))
    pygame.display.flip()



# dibujos en la pantalla
    # pygame.draw.rect(display,ROJO,(150,70,100,70),5)
    # pygame.draw.rect(display,VERDE,(250,180,100,100),5)
    # pygame.draw.circle(display,MAGENTA,(600,200),120,3)
    # pygame.draw.ellipse(display,AMARILLO,(300,350, 130 , 200),5)
    # pygame.draw.line(display,AZUL,(0,0),(ancho,alto),5)
