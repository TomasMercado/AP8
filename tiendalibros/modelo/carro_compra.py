class CarroCompras:
    def __init__(self):
       self.items = [] 
       
    def agregar_item(self, libro, cantidad):
        nuevo_item = ItemCompra(libro, cantidad)
        self.items.append(nuevo_item)
        return nuevo_item
    
    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self.items)
        return total
    
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]
        
    def retirar_item_de_carrito(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]
        
        
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item

    # Defina el metodo calcular_total

    # Defina el metodo quitar_item
