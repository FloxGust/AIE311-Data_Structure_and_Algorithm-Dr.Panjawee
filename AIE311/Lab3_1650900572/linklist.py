class cylinder():
    def __init__(self, radius, height):
      self.radius = radius
      self.heigth = height
      
    def calculate(self):
        volume = 3.14 * (self.radius^2) * self.heigth
        return volume
      
      
First_cy = cylinder(5,18)
Second_cy = cylinder(7,13)

print("First Volume :" ,First_cy.calculate())
print("Secound Volume :" ,Second_cy.calculate())