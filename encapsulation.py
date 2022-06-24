class Contractor:
    def __init__(self, name, hourlyRate, age):
        # public attribute
        self.name = name
        # protected attribute
        self._hourlyRate = hourlyRate
        #private attribute
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age
        
              
# create an object of the Contractor class
con = Contractor('Rob', 150, 18)
print(con.name)#print public attribute
print(con._hourlyRate)#print protected attribute value
con._hourlyRate = 160# print protected attribute new value
print('Hourly Rate in USD:', con._hourlyRate)
#print private atributes value
print("{}".format(con.getAge()))
#set new value for private attribute and print it
con.setAge(23)
print("{}".format(con.getAge()))




