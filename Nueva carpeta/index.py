
def pedido_pizzas():
    precio_base = 10 
    cliente = input("Ingrese el nombre del cliente: ")
    cantidad = int(input("Ingrese la cantidad de pizzas que desea comprar: "))
    quiere_bebida = input("¿Quiere bebida? (si/no):")
    total = precio_base * cantidad
    if quiere_bebida == "si":
        total += 3
    sabor_pizza = input("Sabor de la pizza: ")
    extra= input("desea un sabor extra? (si/no): ")
    if extra == "si":
        extra1 = input("Ingrediente extra 1: ")
        extras = input("desea otro ingrediente extra? (si/no): ")
        if extras == "si":
           extra2 = input("Ingrediente extra 2: ")
    else:
        extra1 = "Ninguno"
        extra2 = "Ninguno"
    estado_pizza = preparar_sabores(sabor_pizza, extra1, extra2)
    return cliente, total, cantidad
def preparar_sabores(sabor, extra1, extra2):
    ingredientes = [sabor, extra1, extra2]
    print(f"\nCocinando pizza de {sabor}...")
    for ing in ingredientes:
        print(f"Poniendo: {ing}")
    return "Lista"


def calcular_descuento(total):
    """Aplica un descuento basado en el monto total."""
    if total > 50:
        descuento = total * 0.20
        print("¡Descuento del 20% aplicado por compra mayor a $50!")
    elif total > 30:
        descuento = total * 0.10
        print("¡Descuento del 10% aplicado por compra mayor a $30!")
    else:
        descuento = 0
        print("No aplica descuento para esta compra.")
    return total - descuento


def control_calidad(cantidad_pizzas):
    """Simula una revisión de cada pizza usando un for."""
    print("\nIniciando control de calidad...")
    for i in range(1, cantidad_pizzas + 1):
        print(f"-> Pizza #{i}: Revisada y aprobada ✓")


def confirmar_pago():
    """Usa un while para asegurar que el usuario confirme el pedido."""
    confirmacion = ""
    while confirmacion != "si":
        confirmacion = input("\n¿Confirmar el procesamiento del pago? (escriba 'si'): ").lower()
    return "Pago Procesado"


def mostrar_ticket(cliente, total_final, estado, confirmacion_pago):
    print("\n" + "=" * 25)
    print("      TICKET DE VENTA      ")
    print("=" * 25)
    print(f"Cliente: {cliente}")
    print(f"Estado de Pizza: {estado}")
    print(f"Estado de Pago: {confirmacion_pago}")
    print(f"Total a Pagar: ${total_final}")
    print("=" * 25)

nombre_cli, monto_inicial, cant = pedido_pizzas()
control_calidad(cant)
monto_con_descuento = calcular_descuento(monto_inicial)
pago_estado = confirmar_pago()
mostrar_ticket(nombre_cli, monto_con_descuento, estado_pizza , pago_estado)
