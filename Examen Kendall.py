import os
os.system("cls")


saldo=int(0)
usuario=str.lower("banco")
clave=int("8585")
total=saldo
contador=0




while contador<3:
      usuario=input("Digite el usuario: ")
      contador=contador+1
      if str(usuario)== "banco":
            print("Usuario correcto")
            contraseña=input("ingrese su contraseña : ")
            if (contraseña)== "8585":
                  print("Bienvenido al cajero del banco de la comunidad")
                  break      
            else:
                  print("Clave incorrecta")
                  if    contador==3:
                        quit(print("Sistema bloqueado"))
                        
      else:
            print("Usuario incorrecto")
            if    contador==3:
                  quit(print("sistema bloqueado"))
                  
            
      

while True:
      print(f"Seleccione la opcion\n\
1-Hacer deposito:\n\
2-Retiro:\n\
3-Consulta saldo:\n\
4-Salir:")

      opcion=input()    
      
      if opcion=="1":
            ingreso=float(input(f"Digite el monto:"))
            saldo+=ingreso 
            print(f"Su saldo es de {saldo}:\n\
Monto depositado es:{total+saldo}")
                     
      if opcion=="2":
            egreso=float(input(f"Digite el monto a retirar :"))
            
            print(f'Su retiro es de:{egreso}')

            if egreso>saldo:
                  print(f"Su saldo es insuficiente")
                  
            else:
                  saldo-=egreso
                  print(f"Su saldo es de: {saldo}")
                  

      if opcion=="3":
            print(f"El saldo de su cuenta es de :{saldo}")

      if opcion=="4":
            quit(print("Gracias por preferir nuestro cajero"))
      