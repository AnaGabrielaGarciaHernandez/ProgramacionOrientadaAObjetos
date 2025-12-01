<<<<<<< HEAD
class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    def suma(self):
        Suma = self.num1 + self.num2
        return Suma

    def resta(self):
        return f"{self._num1} - {self._num2} = {self._num1 - self._num2}"

    def mult(self):
        return f"{self._num1} * {self._num2} = {self._num1 * self._num2}"

    def div(self):
        if self._num2 != 0:
            return f"{self._num1} / {self._num2} = {self._num1 / self._num2}"
        else:
            return "Error: División por cero"

# Entrada del usuario
A = int(input("Ingrese un número: "))
B = int(input("Ingrese otro número: "))

# Crear instancia y mostrar resultados
calc = Calculadora(A, B)
print(calc.suma())
print(calc.resta())
print(calc.mult())
print(calc.div())
=======
class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, value):
        self._num1 = value

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, value):
        self._num2 = value

    def suma(self):
        Suma = self.num1 + self.num2
        return Suma

    def resta(self):
        return f"{self._num1} - {self._num2} = {self._num1 - self._num2}"

    def mult(self):
        return f"{self._num1} * {self._num2} = {self._num1 * self._num2}"

    def div(self):
        if self._num2 != 0:
            return f"{self._num1} / {self._num2} = {self._num1 / self._num2}"
        else:
            return "Error: División por cero"

# Entrada del usuario
A = int(input("Ingrese un número: "))
B = int(input("Ingrese otro número: "))

# Crear instancia y mostrar resultados
calc = Calculadora(A, B)
print(calc.suma())
print(calc.resta())
print(calc.mult())
print(calc.div())
>>>>>>> 8e61c9a1959ff5c6e0ce93371cba338e259fc566
