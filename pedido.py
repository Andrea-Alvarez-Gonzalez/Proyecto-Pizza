from pizza import Pizza

mi_pizza = Pizza()
mi_pizza.realizar_pedido()


if mi_pizza.valida:
        print("¡Pedido confirmado!")
else:
        print("Pedido rechazado. Ingredientes no válidos.")
