# Src/Guns.py

class Bullet:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        # Move bullet upwards
        self.y -= self.speed

class Player:
    def __init__(self, x, y, screen_width):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.bullets = []
        self.speed = 5  # Player movement speed

    def shoot(self):
        # Create a new bullet at player's position
        new_bullet = Bullet(self.x, self.y)
        self.bullets.append(new_bullet)

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0  # Prevent going off-screen

    def move_right(self):
        self.x += self.speed
        if self.x > self.screen_width:
            self.x = self.screen_width  # Prevent going off-screen

    def update_bullets(self, screen_height):
        # Move bullets and remove off-screen bullets
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)
