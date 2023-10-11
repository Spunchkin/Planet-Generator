import random, pygame

pygame.init()

width, height = 800, 500
window = pygame.display.set_mode((width, height))

names1 = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega","Apex", "Nebula", "Orbit", "Starlight", "Cosmos", "Galaxy", "Quasar", "Celestial", "Nova", "Eclipse", "Radiant", "Astro", "Comet", "Luminous", "Meteor", "Infinity", "Spectrum", "Astral", "Cosmic", "Stellar", "Ambatakum"]
names2 = ["Andromeda", "Aquila", "Cassiopeia", "Draco", "Lyra", "Pegasus", "Perseus", "Ursa", "Vulpecula", "Aether", "Chronos", "Erebus", "Hypnos", "Nyx", "Phoebe", "Selene", "Thanatos", "Aurora", "Calypso", "Electra", "Aegis", "Alterra", "Astraea", "Caelus", "Cassiopeia", "Cygnus", "Elysium", "Hyperion", "Icarus", "Luna", "Nova", "Orion", "Pandora", "Phobos", "Quasar", "Rhea", "Serenity", "Terra", "Umbra", "Ambassing", "Vesta", "Zephyr", "B", "A", "C"]

font = pygame.font.SysFont("None", 32)

#Planet Class
class Planet:
    def __init__(self):
        self.pos = [500, (height // 2)]
        self.rad = random.randint(30, 50)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.moons = []
        self.moon_count = random.randint(0, 4)
        self.outer_rad = self.rad * 2
        self.name1 = random.choice(names1)
        self.name2 = random.choice(names2)
        self.name1_text = font.render(f"{self.name1}", False, (255, 255, 255))
        self.name2_text = font.render(f"{self.name2}", False, (255, 255, 255))

    def draw(self):
        pygame.draw.circle(window, self.color, self.pos, self.rad)
        #draws the orbit circle for the moons
        for moon in self.moons:
            if moon.ring == 1:
                pygame.draw.circle(window, (255, 255, 255), self.pos, self.outer_rad, 2)
            if moon.ring == 2:        
                pygame.draw.circle(window, (255, 255, 255), self.pos, self.outer_rad * 2, 2)
 

 #Moon Class
class Moon:
    def __init__(self, rad, x, y, ring):
        self.angle = random.randint(0, 360)
        self.x = x
        self.y = y
        self.rad = rad
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.speed = random.uniform(0.000002, 0.02)
        self.ring = ring
        self.rect = pygame.Rect(self.x, self.y, self.rad * 2, self.rad * 2)

        

    def draw(self):
        self.rect.x = self.x - (self.rad)
        self.rect.y = self.y - (self.rad)

        pygame.draw.circle(window, self.color, (self.x, self.y), self.rad)
        pygame.draw.rect(window, self.color, self.rect, 2)
       