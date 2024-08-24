# Importamos listas de ingredientes
from ingredientes import proteicos, vegetales, tipos_masa

# Definimos la clase Pizza
class Pizza:
    
    # Este es el método que se ejecuta cuando creamos una nueva Pizza.
    def __init__(self):
        self.proteico = ""  # Guardará el ingrediente proteico
        self.vegetal1 = ""  # Guardará el primer ingrediente vegetal
        self.vegetal2 = ""  # Guardará el segundo ingrediente vegetal
        self.masa = ""      # Guardará el tipo de masa
        self.valida = False # Indicará si la pizza es válida o no

    # Verificar si un ingrediente está en la lista de opciones válidas
    @staticmethod
    def validar_elemento(elemento, lista_posibles):
        elemento = elemento.strip().lower()
        return elemento in [item.lower() for item in lista_posibles]  #Compara con la lista de válidos

    # Método que pide al usuario los ingredientes de la pizza y verifica si son válidos
    def realizar_pedido(self):
        # Pedimos ingresar ingredientes, los limpiamos y convertimos a minúsculas
        self.proteico = input("Ingrese el ingrediente proteico: ").strip().lower()
        self.vegetal1 = input("Ingrese el primer ingrediente vegetal: ").strip().lower()
        self.vegetal2 = input("Ingrese el segundo ingrediente vegetal: ").strip().lower()
        self.masa = input("Ingrese el tipo de masa: ").strip().lower()

        # Verificamos si cada ingrediente es válido comparándolo con las listas importadas
        proteico_valido = self.validar_elemento(self.proteico, proteicos)
        vegetal1_valido = self.validar_elemento(self.vegetal1, vegetales)
        vegetal2_valido = self.validar_elemento(self.vegetal2, vegetales)
        masa_valida = self.validar_elemento(self.masa, tipos_masa)

        # Si todos los ingredientes son válidos, marcamos la pizza como válida
        self.valida = proteico_valido and vegetal1_valido and vegetal2_valido and masa_valida

        if self.valida:
            print("La pizza es válida y se ha creado con éxito.")
        else:
            print("La pizza no es válida. Por favor, revise los ingredientes.")
            # Si alguno de los ingredientes no es válido, mostramos cuál es el ingrediente inválido
            if not proteico_valido:
                print(f"Ingrediente proteico '{self.proteico}' no es válido.")
            if not vegetal1_valido:
                print(f"Primer vegetal '{self.vegetal1}' no es válido.")
            if not vegetal2_valido:
                print(f"Segundo vegetal '{self.vegetal2}' no es válido.")
            if not masa_valida:
                print(f"Tipo de masa '{self.masa}' no es válido.")

# 
if __name__ == "__main__":
    mi_pizza = Pizza()
    mi_pizza.realizar_pedido()

    if mi_pizza.valida:
        print("¡Pedido confirmado!")
    else:
        print("Pedido rechazado. Ingredientes no válidos.")