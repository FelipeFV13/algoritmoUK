class PersonaReal:
    def __init__(self, nombre, is_king):
        self.nombre = nombre
        self.hijos = []
        self.is_king = is_king
        self.posicion = 0
        self.nivel = 0


    def añadir_hijos(self, hijo):
        self.hijos.append(hijo)

    def definir_posicion(self):
        if self.is_king == True:
            self.posicion = 0

        if len(self.hijos) > 0:
            if len(self.hijos) > 1:
                self.hijos[0].posicion = self.posicion +1
                for i in range(len(self.hijos)-1):
                    self.hijos[i+1].posicion = self.hijos[i].posicion +1


    def nivel(self):
        if self.is_king == True:
            self.nivel = 0
        for i in range(len(self.hijos)):
            self.hijos[i].nivel = self.nivel + 1




