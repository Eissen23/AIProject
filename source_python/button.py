import pygame

#button class
class Button():
    def __init__(self,x ,y ,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw_self(self, surface):

        action = False

        #get mouse position 
        pos = pygame.mouse.get_pos()
        
        #check mouseover and click condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 0 and action == True:
                self.clicked == False
                action = False
        
            #neu loi thi xoa cai segment nay
            if action == True:
                self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create button instance

