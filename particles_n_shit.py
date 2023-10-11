import pygame, sys, random
pygame.init()

#wind speed
wind = 0
wind_y = 0

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


#Particle class
class Particle:
    def __init__(self, mov_x, mov_y, rad, pos, light_color):
        self.pos = pos
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.rad = rad
        self.size = [100, 100]
        self.color = [255, 255, 255]
        self.light_color = light_color
    
    def update(self):
            self.pos[0] += self.mov_x
            self.pos[1] += self.mov_y
            self.rad -= 0.15
            self.pos[0] -= wind
            self.pos[1] -= wind_y
            self.pos[1] += 9

            
            #makes the particles darker over time so they fade out slowly
            if self.color[1] > 5 and self.color[0] > 5 and self.color[2] > 5:
                self.color[1] -= 4
                self.color[2] -= 4
                self.color[0] -= 4
          
            #cap for particle minimum color, so they dont break the pygame.draw.circle function
            elif self.color[1] <= 5 or self.color[0] <= 5 or self.color[2] <= 5:
                self.color[1] = 0
                self.color[2] = 0
                self.color[0] = 0

            #drawing the circles and glowing effect
            pygame.draw.circle(window, (self.color), self.pos, self.rad, width = self.size[0])
            radius = self.rad * 1.8

            if self.light_color == 0:
               window.blit(circle_surf(radius, (68, 109, 148)), ((self.pos[0] - (self.rad * 1.6)), (self.pos[1] - (self.rad * 1.6))), special_flags=pygame.BLEND_RGB_ADD)
               window.blit(circle_surf((radius * 1.6), (41, 67, 92)), ((self.pos[0] - (self.rad * 2.4)), (self.pos[1] - (self.rad * 2.4))), special_flags=pygame.BLEND_RGB_ADD)
            if self.light_color == 1:
               window.blit(circle_surf(radius, (217, 112, 26)), ((self.pos[0] - (self.rad * 1.6)), (self.pos[1] - (self.rad * 1.6))), special_flags=pygame.BLEND_RGB_ADD)
               window.blit(circle_surf((radius * 1.6), (133, 36, 21)), ((self.pos[0] - (self.rad * 2.4)), (self.pos[1] - (self.rad * 2.4))), special_flags=pygame.BLEND_RGB_ADD)
            if self.light_color == 2:
               window.blit(circle_surf(radius, (181, 27, 104)), ((self.pos[0] - (self.rad * 1.6)), (self.pos[1] - (self.rad * 1.6))), special_flags=pygame.BLEND_RGB_ADD)
               window.blit(circle_surf((radius * 1.6), (125, 17, 71)), ((self.pos[0] - (self.rad * 2.4)), (self.pos[1] - (self.rad * 2.4))), special_flags=pygame.BLEND_RGB_ADD)
            if self.light_color == 3:
               window.blit(circle_surf(radius, (78, 63, 161)), ((self.pos[0] - (self.rad * 1.6)), (self.pos[1] - (self.rad * 1.6))), special_flags=pygame.BLEND_RGB_ADD)
               window.blit(circle_surf((radius * 1.6), (38, 31, 77)), ((self.pos[0] - (self.rad * 2.4)), (self.pos[1] - (self.rad * 2.4))), special_flags=pygame.BLEND_RGB_ADD)

            

#usuals, setting timer
width, height = 500, 500
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()



#particles list and on/off variable and light_color
particles = []
spawning = False
light_color = 0
#game loop



while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          
          #particles spawn when holding down mouse, and wind for cool blowing effect *pause
          if event.type == pygame.MOUSEBUTTONDOWN:
               spawning = not spawning
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                    wind = 4
               if event.key == pygame.K_d:
                    wind = -4
               if event.key == pygame.K_w:
                    wind_y = 3
               if event.key == pygame.K_s:
                    wind_y = -3
               if event.key == pygame.K_1:
                    light_color = 0
               if event.key == pygame.K_2:
                    light_color = 1
               if event.key == pygame.K_3:
                    light_color = 2
               if event.key == pygame.K_4:
                    light_color = 3
               

          if event.type == pygame.KEYUP:
               wind = 0
         
          mouse_x, mouse_y = pygame.mouse.get_pos()


     if spawning:
          particles.append(Particle(mov_x=random.randint(-1, 1), mov_y=random.randint(-2, -1), rad=random.randint(4, 6), pos= [(mouse_x), (mouse_y)], light_color=light_color))
          
     #usual pygame screen clearing shenanigans
     window.fill((0, 0, 0))
     
     #draws particles and removes them if they are too small
     for particle in particles:
          particle.update()
          if particle.rad <= 1:
               particles.remove(particle)
          

     clock.tick(70)
     pygame.display.flip()

     
