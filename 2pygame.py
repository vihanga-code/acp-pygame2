import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("my first game screen")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()

    pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,30,60,60))      
 
      
    pygame.display.flip()        

