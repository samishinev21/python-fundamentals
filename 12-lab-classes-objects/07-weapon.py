class Weapon:
    bullets = 0

    def __init__(self, bullets):
        Weapon.bullets = bullets

    def shoot(self):
        if Weapon.bullets <= 0:
            return "no bullets left"
        else:
            Weapon.bullets -= 1
            return "shooting..."
        
    def __repr__(self):
         return f"Remaining bullets: {Weapon.bullets}"
    
weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)