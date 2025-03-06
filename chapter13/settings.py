class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (135,206,235)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_width = 90  # New attribute for ship width
        self.ship_height = 128  # New attribute for ship height

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 20,147)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
