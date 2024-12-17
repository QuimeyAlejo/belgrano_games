class Platform:
    def __init__(self,platform_name,platform_id):
        self.platform_name = platform_name
        self.platform_id= platform_id
class Games:
    def __init__(self, name, genre, price, description,):
        self.name = name
        self.genre = genre
        self.price = price
        self.description = description

    def get_game_info(self):
        return {
            "game_id": self.game_id,
            "name": self.name,
            "genre": self.genre,
            "price": self.price,
            "stock": self.stock,
            "platform": self.platform.name if isinstance(self.platform, Platform) else self.platform
        }
