class AlienShip:
    def __init__(self, x, y, speed, health):
        self.x = x           # horizontal position
        self.y = y           # vertical position
        self.speed = speed   # movement speed
        self.health = health # health points

    def move(self):
        # Move alien down the screen
        self.y += self.speed

    def take_damage(self, damage):
        self.health -= damage

    def is_destroyed(self):
        return self.health <= 0
