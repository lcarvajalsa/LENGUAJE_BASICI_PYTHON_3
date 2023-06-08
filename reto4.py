lista=[] 
intructores2557861={
        "":""
}
repetirtodo=1
nom=str(input("Agregar el nombre del instructor \n"))
nom=nom.lower()
lista.append(nom)
aceptar=int(input("Desea agregar un instructor mas a la lista UNO para si, DOS para NO \n"))
while aceptar==1:
    nom=str(input("Agregar nuevo instructor \n"))
    nom=nom.lower()
    lista.append(nom)
    aceptar=int(input("Desea agregar otro instructor mas a la lista UNO para si, DOS para NO \n"))
    for i, e in enumerate(lista):
        print(i,e)          
dato=int(input("Desea modificar el nombre del Instructor UNO para si, DOS para no\n"))
while dato==1:
        dato1=int(input("Selecciona numero del Instructor a modificar\n"))
        nom=str(input("Ingrese nombre\n"))
        nom=nom.lower()
        lista[dato1]=nom
        dato=int(input("Desea modificar el nombre de otro Instructor UNO para si, DOS para no\n"))
        for i, e in enumerate(lista):
            print(i,e)       
modificar=int(input("Desea eliminar un Instructor de la lista UNO para si, DOS para no\n"))
while modificar==1:
    nom=str(input("Seleccionar el nombre del Instructor\n"))
    nom=nom.lower()
    lista.remove(nom)
    modificar=int(input("Desea eliminar otro Instructor de la lista UNO para si, DOS para no\n"))
    for i, e in enumerate(lista):
        print(i,e)    
buscar=int(input("Desea buscar un Instructor de la lista UNO para si, DOS para no\n"))
while buscar==1:
    nom=str(input("Nombre del Instructor\n"))
    nom = nom.lower()
    esta_lista=lista.count(nom)
    if esta_lista>0:
        print ("esta en la lista")
        buscar=int(input("Desea buscar otro Instructor de la lista UNO para si, DOS para no\n"))
        for i, e in enumerate(lista):
            print(i,e)
    else:
        print ("no esta en la lista")
        buscar=int(input("Desea buscar otro Instructor de la lista UNO para si, DOS para no\n"))
        for i, e in enumerate(lista):
            print(i,e)        
lista.sort()
print("LISTA ORDENADA",lista)
while repetirtodo == 1:
    menu=(int(input("Uno para agregar, DOS para buscar, TRES para borrar, CUATRO para listar, CINCO para salir\n")))
    #Agregar
    if menu==1:
        nom=(str(input("Ingrese el nombre del instructor\n")))
        nom=nom.lower()
        #este bloque valida si el istructor está en el diccionario
        for i in intructores2557861:
            if i == nom:
                x=True
            else: 
                x=False
        #en el caso de que si está se realizará la modificación
        if x==True:
            print (intructores2557861[nom])
            modificar=int(input("Desea modificar algún valor? UNO para SI, DOS para NO"))
            if modificar==1:
                mod=int(input("Que valor desea modificar??\nUNO para Nombre\nDOS para materia\nTRES para telefono"))
                if mod==1:
                    mod1=str(input("Ingrese el nombre"))
                    intructores2557861[nom]["nombre"]=mod1
                    intructores2557861[mod1]=intructores2557861[nom]
                    del intructores2557861[nom]
                    #AQUI FALTA LO QUE ESTA HACIENDO DEINER
                elif mod==2:
                    mod1=str(input("Ingrese la materia"))
                    intructores2557861[nom]["materia"]=mod1
                elif mod==3:
                    mod1=str(input("Ingrese el telefono"))
                    intructores2557861[nom]["telefono"]=mod1
        #De lo contrario agrega al nuevo instructor
        else:
            print("Registrar instructor ")   
            nom1={}
            mat=str(input("ingrese la materia\n"))
            tel=str(input("ingrese telefono\n"))
            nom1={
                "nombre":nom,
                "materia":mat,
                "telefono":tel
            }
            intructores2557861[nom] = nom1
            print(intructores2557861[nom])
            #Buscar
    elif menu == 2:
        #solicita al usuario ingresar el texto de la busqueda
        prefijo = input("Ingrese el prefijo a buscar: ")
        resultados = []
        #revisa todo el diccionario y compara todos los registros dentro, si coincide que comienzan con lo ingresado por el usuario, entonces los guarda en la variable resultados
        for key in intructores2557861:
            if key.startswith(prefijo):
                resultados.append(intructores2557861[key])
        #siempre y cuando halla encontrado resultados imprimirá todos los resultados
            if len(resultados) > 0:
                for resultado in resultados:
                    print(resultado)
            else:
                print("No se encontraron registros con el prefijo especificado.")
    elif menu == 3:            
        nom=(str(input("Ingrese el nombre del instructor\n")))
        nom=nom.lower()
        for i in intructores2557861:
            if i == nom:
                x=True
            else: 
                x=False
        #en el caso de que si está se realizará la modificación
        if x==True:
            print (intructores2557861[nom])
            borrar=int(input("Desea borrar el valor? UNO para SI, DOS para NO"))
            if borrar==1:
                del intructores2557861[nom]
                print (intructores2557861)
            else: 
                print (intructores2557861[nom])
    