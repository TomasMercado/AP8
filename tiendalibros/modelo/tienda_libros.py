class TiendaLibros:
   def __init__(self):
        self.catalogo = {} 
        self.carrito = CarroCompras()
        
   def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError("El libro ya existe en el catálogo.")
        nuevo_libro = Libro(titulo, isbn, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    
   def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias <= 0:
            raise LibroAgotadoError("El libro está agotado.")
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError("No hay suficientes unidades disponibles.")
        
            self.carrito.agregar_item(libro, cantidad)
        libro.existencias -= cantidad
    pass
    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
