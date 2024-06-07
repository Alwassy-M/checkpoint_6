class usuario:

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def mostrar_datos(self):
        print(f'{self.nombre_usuario}, {self.contraseña}')


usuario1 = usuario('QADDUR', 1234)
usuario1.mostrar_datos()