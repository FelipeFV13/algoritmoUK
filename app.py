from PersonaReal import PersonaReal

isabel = PersonaReal("Reina Isabel II", is_king=True,)
carlos = PersonaReal("Carlos III", is_king=False)
andres = PersonaReal("andres", is_king=False)
eduardo = PersonaReal("Eduardo", is_king=False)
ana = PersonaReal("Ana", is_king=False)
henry = PersonaReal("Henry", is_king=False)
pancho = PersonaReal("Pancho", is_king=False)

isabel.añadir_hijos(carlos)
isabel.añadir_hijos(andres)
isabel.añadir_hijos(eduardo)
isabel.añadir_hijos(ana)

carlos.añadir_hijos(henry)
isabel.definir_posicion()


print(isabel.posicion)
print(carlos.posicion)
print(andres.posicion)
