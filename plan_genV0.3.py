import random, pygame, sys, math
from Celestial_Bodies import Moon, Planet, font
pygame.init()


width, height = 800, 500
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#set initial seed
random.seed(1)

#and button
button_img = pygame.image.load("images\\Sprite2.png")
button_rect = pygame.Rect(50, 50, button_img.get_width(), button_img.get_height())
button_img2 = pygame.image.load("images\\Sprite3.png")
button_rect2 = pygame.Rect(50, 100, button_img2.get_width(), button_img2.get_height())
button_img3 = pygame.image.load("images\\Sprite4.png")
button_rect3 = pygame.Rect(50, 150, button_img3.get_width(), button_img3.get_height())

#counter/seed
counter = 0
seed = 1
seed_text_number = font.render(f"{seed}", None, (255, 255, 255))
seed_text_text = font.render("Seed:", None, (255, 255, 255)) 
last_seed_number = seed
last_seed_text_text = font.render("Last Seed:", None, (255, 255, 255)) 
last_seed_text_number = font.render(f"{seed}", None, (255, 255, 255))

#enter field shit
enter_image = pygame.image.load("images\\Sprite5.png")
enter_rect = pygame.Rect(50, 200, enter_image.get_width(), enter_image.get_height())

input_field = pygame.Rect(50, 250, 100, enter_image.get_height())

inactive_color = (255, 255, 255)
active_color = (255, 255, 0)
color = inactive_color
active = False
text = ""

#current seed text
current = font.render(f"Current Seed:", None, (255 ,255, 255))

#function to add moons
def add_moon(list, x_pos, y_pos, ring):
    if ring == 1:
        list.append(Moon(rad = random.randint(5, 20), x=x_pos, y=y_pos, ring=1))
    if ring == 2:
        list.append(Moon(rad = random.randint(5, 20), x=(x_pos), y=(y_pos), ring=2))
    
def check_planets_and_adds_moons():
    global counter

    for planet in planets:
        if counter < planet.moon_count:
            add_moon(planet.moons, planet.outer_rad, planet.outer_rad, ring=random.randint(1, 2))
            counter += 1
        planet.draw()
        #draws the names of planets on screen
        window.blit(planet.name1_text, (220, 0))
        window.blit(planet.name2_text, (235 - len(planet.name2), 20))
        #checks the moons in the planet.moons list
        for moons in planet.moons:
            #draws moons and updates position based on current ring and angle
            moons.x = 500 + (planet.outer_rad * moons.ring) * math.cos(moons.angle)
            moons.y = 250 + (planet.outer_rad * moons.ring) * math.sin(moons.angle)
            moons.angle += moons.speed
            moons.draw()


def handle_buttons():
    global seed, seed_text_number, seed_text_text, planets, last_seed_number, last_seed_text_number, last_seed_text_text, counter, text, active, color, active_color, inactive_color, active_color

    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
            last_seed_number = seed
            seed += 1
            random.seed(seed)
            counter = 0
            planets = [Planet()]
            seed_text_text = font.render("Seed:", None, (255, 255, 255))
            seed_text_number = font.render(f"{seed}", None, (255, 255, 255))
    if button_rect2.collidepoint(mouse_pos):
            last_seed_number = seed
            if seed > 1:
                seed -= 1
            random.seed(seed)
            counter = 0
            planets = [Planet()]
            seed_text_text = font.render("Seed:", None, (255, 255, 255))
            seed_text_number = font.render(f"{seed}", None, (255, 255, 255))
    if button_rect3.collidepoint(mouse_pos):
            last_seed_number = seed
            random.seed()
            seed = random.randint(0, 9999999999999)
            random.seed(seed)
            counter = 0
            planets = [Planet()]
            seed_text_text = font.render("Seed:", None, (255, 255, 255))
            seed_text_number = font.render(f"{seed}", None, (255, 255, 255))
    if enter_rect.collidepoint(mouse_pos):
         last_seed_number = seed
         seed = int(text) if text.isdigit() else seed
         random.seed(seed)
         counter = 0
         planets = [Planet()]
         seed_text_number = font.render(f"{seed}", None, (255, 255, 255))
         text = ""
    
    if input_field.collidepoint(mouse_pos):
         active = not active
    else:
         active = False
         color = active_color if active else inactive_color

                    
#List to keep track of planets

planets = [Planet()]

def main_game():
    global text, window, text_surface, seed, seed_text_number, seed_text_number, seed_text_text

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_buttons()
            
            if event.type == pygame.KEYDOWN:
                if active:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        
                        else:
                            if len(text) < 13:
                                text += event.unicode

                    
            
    
        window.fill((0, 0, 0))

        text_surface = font.render(text, True, color)

        window.blit(button_img, dest=button_rect.topleft)
        window.blit(button_img2, dest=button_rect2.topleft)
        window.blit(button_img3, dest=button_rect3.topleft)
        window.blit(seed_text_number, dest=[50, 330])
        window.blit(current, dest=[50, 305] )
        window.blit(seed_text_text, dest=[50, 250])
        window.blit(enter_image, enter_rect.topleft)
        window.blit(text_surface, dest=[70 - len(text), 275])
        
        


        #checks planets and adds moons
        check_planets_and_adds_moons()
        
        clock.tick(60)
        pygame.display.update()

main_game()