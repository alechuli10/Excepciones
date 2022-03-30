from Verificador import Verificador


def acceder ():
  verificador = Verificador("alejandrogoam200210@gmail.com")
  usuario= ""
  while usuario!=verificador.getEmail():
      usuario= input("-->")
      try:
          verificador.comprobarEmail(usuario)
      except ValueError as msg:
          print (msg)
      except Exception as msg:
          print (msg)
          exit()
          
  print("Bienvenido Alejandro")