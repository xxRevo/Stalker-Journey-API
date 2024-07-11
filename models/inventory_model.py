class Inventory:
    def __init__(self):
        self.money = 0
        self.primary_weapon = RangedWeapon()
        self.sidearm_weapon = RangedWeapon()
        self.meele_weapon = MeeleWeapon()
        self.armor = Armor()
        self.gasmask = Gasmask()
        self.healing_medicine = HealingMedicine()
        self.bandages = Bandages()
        self.radiation_medicine = RadiationMedicine()
        self.detector = Detector()
        self.utility = Utility()
    
    def swap_primary_weapon(self, primary_weapon):
        self.primary_weapon = primary_weapon

    def swap_sidearm_weapon(self, sidearm_weapon):
        self.sidearmy_weapon = sidearm_weapon
    
    def swap_meele_weapon(self,meele_weapon):
        self.meele_weapon = meele_weapon

    def swap_armor(self,armor):
        self.armor = armor

    def swap_gasmask(self,gasmask):
        self.gasmask = gasmask

    def swap_detector(self, detector):
        self.detector = detector

    def swap_utility(self, utility):
        self.utility = utility

    def change_money(self,amount):
        self.money = self.money + amount
