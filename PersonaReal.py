class PersonaReal:
    def __init__(self, nombre, is_king,año_nacimiento, genero):
        self.nombre = nombre
        self.ano_nacimiento = año_nacimiento
        self.genero = genero
        self.hijos = []
        self.is_king = is_king
        self.descendencia = []

    def añadir_hijos(self, hijo):
        self.hijos.append(hijo)

    def ordenar_hijos(self):
        if len(self.hijos) > 0:

            for i in range(len(self.hijos)):
                if self.hijos[i].ano_nacimiento < 2011 and self.hijos[i].genero == "M":
                    container = self.hijos[i]
                    self.hijos.remove(self.hijos[i])
                    self.hijos.append(container)


    def iterar_descendencia(self):
        # Agregamos una función auxiliar para realizar la recursión
        self.ordenar_hijos()
        def agregar_descendencia(persona):
            if len(persona.hijos) > 0:
                for hijo in persona.hijos:
                    self.descendencia.append(hijo)
                    agregar_descendencia(hijo)

        agregar_descendencia(self)  # Llamamos a la función auxiliar con la persona actual
        return self.descendencia
