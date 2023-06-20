def agregar_precio_adicional_open_top(builder_class):
    class BuilderContenedorOpenTopDecorator(builder_class):
        def __init__(self):
            super().__init__()
            self.precio_adicional = 10000

        def set_precio_adicional(self, precio_adicional):
            self.precio_adicional = precio_adicional
            return self

        def get_contenedor(self):
            contenedor = super().get_contenedor()
            contenedor.set_precio_adicional(self.precio_adicional)
            return contenedor

    return BuilderContenedorOpenTopDecorator