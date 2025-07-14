class Conversor:
  def celsius_para_fahrenheit(self, celsius):
    return (celsius * 9/5) + 32

celsius = float(input("digite a temperatura em celcius: "))

conversor = Conversor()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)