lista=[]


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


            
