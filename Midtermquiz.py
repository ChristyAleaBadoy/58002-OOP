class Tempconversion:
  def __init__(self, fahrenheit, Celcius, kelvin):
    self.__fahrenheit = fahrenheit
    self.__Celcius = Celcius
    self.__kelvin = kelvin

  def display(self):
      print(f"Temperature conversion from fahrenheit", self.__fahrenheit, "to Celcius is",(self.__Celcius, (F-32)*5/9))
      print(f"Temperature conversion from Celcius", self.__Celcius, "to fahrenheit is", (self.__fahrenheit, (C*9/5)+32))
      print(f"Temperature conversion from kelvin", self.__kelvin, "to Celcius is", (self.__Celcius, (K-273.15)))
      print(f"Temperature conversion from Celcius", self.__Celcius, "to kelvin is", (self.__kelvin, (C+273.15)))
      print(f"Temperature conversion from kelvin", self.__kelvin, "to fahrenheit is", (self.__fahrenheit, (1.8*K)-459.67))
      print(f"Temperature conversion from fahrenheit", self.__fahrenheit, "to kelvin is", (self.__kelvin, (F+459.67)/1.8))


class FahrenheitToCelcius(Tempconversion):
    pass


class CelciusToFahrenheit(Tempconversion):
    pass

class KelvinToCelcius(Tempconversion):
    pass

class CelciusToKelvin(Tempconversion):
    pass

class KelvinToFahrenheit(Tempconversion):
    pass

class FahrenheitToKelvin(Tempconversion):
    pass



tempconversion = FahrenheitToCelcius(float(input("Enter Temperature: ")))
tempconversion.display()
tempconversion = CelciusToFahrenheit(float(input("Enter Temperature: ")))
tempconversion.display()
tempconversion = KelvinToCelcius(float(input("Enter Temperature: ")))
tempconversion.display()
tempconversion = CelciusToKelvin(float(input("Enter Temperature: ")))
tempconversion.display()
tempconversion = KelvinToFahrenheit(float(input("Enter Temperature: ")))
tempconversion.display()
tempconversion = FahrenheitToKelvin(float(input("Enter Temperature: ")))
tempconversion.display()







