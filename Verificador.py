import re

class Verificador :
  def __init__ (self,email):
    self.email= email

  def getEmail (self):
    return self.email
    
  def comprobarEmail (self,cadena):
    if cadena== "":
        raise ValueError("'' es una entrada incorrecta. Introduzca una dirección de correo electrónico")
    
    if re.search(".*@.*\..*", cadena)== None:
        raise ValueError ("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
    if cadena!= self.email:
        raise Exception ("Cuenta bloqueada a causa de un ataque")