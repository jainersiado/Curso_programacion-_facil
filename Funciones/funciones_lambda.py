#funciones lambda o anonimas

# formas de crear y llamar una funcion lambda
multiplicacion = lambda numero1, numero2: numero1 * numero2

resultado = print(multiplicacion(24,2))
#se almancena en una variable para hacer el llamado ya que la funcion no tiene nombre

#otra forma para llamarla en una sola linea. 
(lambda a,b :print(a*b)) (4,5)