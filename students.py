class Student: 
    # To hide class things that we dont want to public , 
    # use concept like encapsulation, 
    # Also knowns as getter and Setter method
    """"""
    def __init__(self,roll_num, name,gender, course ):
        self._roll_num = roll_num
        self._name = name
        self.gender = gender
        self.course = course

    def attending_class(self):
        print(f"{self._name} is above 75%  in his  attendance!! ")

    def result(self):
        print(f"{self.roll_num}  with roll number {self.roll_num} passed exam!!")

    def get_name(self):
        print(self._name)
    def set_name(self,new_name):
        self._name = new_name
        