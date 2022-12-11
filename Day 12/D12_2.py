# Global scope
player_health = 10

def game():
    # drink_potion() is local within game()
    def drink_potion():
        potion_strenght = 2
        print(player_health)
    drink_potion()

game()