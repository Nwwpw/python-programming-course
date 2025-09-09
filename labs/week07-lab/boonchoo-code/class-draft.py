class ClassName:
    """Class docstring"""
    
    def __init__(self, parameters): #ทุกmethod ต้องมีparameterตัวที่เรียกว่าselfทุกmethod
        # Constructor method
        self.attribute = value
    
    def method_name(self):
        # Instance method
        return something

#3บรรทัดนี้ คือการเอามาใช้
myObj = ClassName(parameters) #ถ้าบรรทัดที่4มาแค่ def __init__(self): บรรทัดนี้(13)ก็จะเป็นmyObj = ClassName()
print(myObj.attribute)
resultFromMethod = myObj.method_name()