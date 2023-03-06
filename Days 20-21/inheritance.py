class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale")
        
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.num_eyes = 5
        
    def breathe(self):
        super().breathe()
        print("doing this underwater")
          
    def swim(self):
        print("moving in water")
         

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)