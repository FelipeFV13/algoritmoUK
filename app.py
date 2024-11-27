from PersonaReal import PersonaReal


isabel = PersonaReal("Reina Isabel II", True,1926, "M")

#descendencia isabel

charles = PersonaReal("Charles III ", True, 1948, "H")
anna = PersonaReal(" Anne, Princess Royal ", False,1950, "M")
andrew = PersonaReal(" Prince Andrew, Duke of York", False, 1960, "H")
edward = PersonaReal(" Prince Edward, Duke of Edinburgh ", False, 1964, "H")

#los nacidos antes 2011, los hombres tiene prioridad en el orden de sucesion a la corona britanica antes que las mujeres

isabel.añadir_hijos(charles)
isabel.añadir_hijos(anna)
isabel.añadir_hijos(andrew)
isabel.añadir_hijos(edward)


#descendencia de charles

william = PersonaReal("William, Prince of Wales", False, 1982, "H")
harry = PersonaReal("Prince Harry, Duke of Sussex ", False, 1984, "H")

charles.añadir_hijos(william)
charles.añadir_hijos(harry)

#descendencia de william
Geroge = PersonaReal("Prince George of Wales", False, 2013, "H")
charlotte = PersonaReal(" Princess Charlotte of Wales", False, 2015,"M")
louis = PersonaReal("Prince Louis of Wales ", False, 2018, "H")

william.añadir_hijos(Geroge)
william.añadir_hijos(charlotte)
william.añadir_hijos(louis)

#descendencia de Harry
archie= PersonaReal("Prince Archie of Sussex", False, 2019, "H")
lilibet = PersonaReal(" Princess Lilibet of Sussex",False, 2021, "M")

harry.añadir_hijos(archie)
harry.añadir_hijos(lilibet)


#descendencia de Andrew
beatrice = PersonaReal(" Princess Beatrice", False, 1988, "M")
eugenie = PersonaReal(" Princess Eugenie", False, 1990, "M")

andrew.añadir_hijos(beatrice)
andrew.añadir_hijos(eugenie)

# descendencia de Beatrice
sienna = PersonaReal("Sienna Mapelli Mozz", False,2021, "M")
beatrice.añadir_hijos(sienna)

# descendencia de eugenie
august = PersonaReal("August Brooksbank",False,2021, "M")
ernest = PersonaReal("Ernest Brooksbank",False, 2023, "H")

eugenie.añadir_hijos(august)
eugenie.añadir_hijos(ernest)

#descendencia de Edward
james = PersonaReal("James Mountbatten-Windsor, Earl of Wessex", False, 2007, "H")
lady = PersonaReal("Lady Louise Mountbatten-Windsor ", False, 2003, "M")

edward.añadir_hijos(james)
edward.añadir_hijos(lady)

#descendencia de Anna
peter = PersonaReal("Peter Phillips", False,1977,"H")
zara = PersonaReal("Zara Tindall", False, 1981, "M")

anna.añadir_hijos(peter)
anna.añadir_hijos(zara)

#descendencia Peter:
savannah = PersonaReal("Savannah Phillips ", False, 2010, "H")
isla =PersonaReal(" Isla Phillips ", False, 2012, "M")

peter.añadir_hijos(savannah)
peter.añadir_hijos(isla)

#descendencia Zara

mia = PersonaReal(" Mia Tindall ", False, 2014, "M")
lena = PersonaReal(" Lena Tindall", False, 2018, "M")
lucas = PersonaReal ("Lucas Tindall", False, 2021, "H")

zara.añadir_hijos(mia)
zara .añadir_hijos(lena)
zara.añadir_hijos(lucas)

if __name__ == "__main__":
    ## Preguntar al usuario que posicion quiere saber
    # Lista externa para guardar la descendencia del antiguo rey, en este caso es isabell
    posiciones_sucesion_al_trono = isabel.iterar_descendencia()

    while True:
        userOption = int(input("Ingrese la posición del trono Britanico que desea saber :"))

        try:
            #mostramos al usuario el resultado de su busqueda
            print(posiciones_sucesion_al_trono[userOption].nombre)
            break
        except IndexError:
            print("Posicion Fuera de rango")

    ## Eliminar a alguien perteneciente a la sucesion del trono
    entry_point = False

    while not entry_point:
        userOption = int(input("Desea eliminar a alguien perteneciente a la cadena de sucesion: \n"
                           "Escriba 1, si desea eliminar: \n"+
                            "Escriba 2, si desea imprimir toda la sucesion al trono del reino unido: "))

        if userOption == 1:
            eleccion_usuario = input("Ingrese el nombre de la persona a eliminar o la posición: ")

            if eleccion_usuario.isdigit():

                while True:
                    try:
                        posicioon_persona = posiciones_sucesion_al_trono[int(eleccion_usuario)]

                        print("\nSe ha eliminado a ",posicioon_persona.nombre)

                        for hijo in posiciones_sucesion_al_trono:
                            if hijo.nombre == posicioon_persona.nombre:
                                posiciones_sucesion_al_trono.remove(hijo)
                        entry_point = True
                        break
                    except IndexError:
                        print("Lo siento esa posicion esta fuera de rango")
                        break


            else:
                nombre = ""
                for hijo in posiciones_sucesion_al_trono:
                    if hijo.nombre == eleccion_usuario:
                        nombre = hijo.nombre
                        posiciones_sucesion_al_trono.remove(hijo)
                print("\nSe ha eliminado a ", nombre)
                entry_point = True

            if entry_point:
                print("Sucesion al Trono Britanico: \n")
                for i in range(1, len(posiciones_sucesion_al_trono)):
                    print(i, posiciones_sucesion_al_trono[i].nombre)
        elif userOption == 2:
            for i in range(len(posiciones_sucesion_al_trono)):
                if i == 0:
                    print(f"king: {posiciones_sucesion_al_trono[i].nombre}")
                else:
                    print(f"{i}: {posiciones_sucesion_al_trono[i].nombre}")
            entry_point = True
        else:
            print(userOption, "No se encuentra en las opciones")

