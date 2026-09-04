# ther are meany types of inharitance. single level,  multilevel inharitance, multi inharitance, 


class bags():
    pass
class rebock(bags):
    pass
class rebockstar(rebock):
    pass

# these are multi level inharitance,

# mulit inharitance ka matlab hai do parants hai matlb kai class ke udahar liye hai.

class livingorganism():
    def __init__(self, hight):
      self.hight = hight


class chutiya():
    def __init__(self, number):
      self.level = number



class humans(livingorganism, chutiya):
    # def __init__(self, number):
    #     super().__init__(number) yaha py super() method sirf ek parant ko inharit kar payega hamko manuualy marna padega
    def __init__(self, hight, number):
        livingorganism.__init__(self, hight)
        chutiya.__init__(self, number)

# human me milti inharitance hua hai.
insam = humans("run_sleep", 10 )


print(insam.hight)
print(insam.level)

