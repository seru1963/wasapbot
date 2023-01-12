import pyautogui,time,sys,subprocess #librerias


def leerParametro():
    #declaracion de variables globales
    global numeroTelefono #almacenamiento del numero de telefono
    global mensajeTexto #almacenamiento del mensaje de texto que se va a mandar
    global contenido
    parametro = sys.argv[1] # identifica el nombre del parametro
    path = "C:/download/wasapbot/main/"+ parametro  #ESTA RUTA HAY QUE CONFIGURAR
    # Otro ejemplo de ruta puede ser "C:/Users/manolito123/Desktop/carpetaArchivos/" + NOMBREDEARCHIVO.txt
    archivo=open(path,encoding='utf-8')#abre el parametro con su ruta completa(se puede cambiar) 
      
    contenido = archivo.read() #leemos el contenido del parametro.txt
    lista = contenido.split("\n")#hacemos una lista con todo lo que leyo del parametro.txt
    numeroTelefono = lista[0]#el primer item sera el numero de telefono
    mensajeTexto = lista[1:]#y los siguientes items cada renglon
    archivo.close()#cerramos el archivo

def abrirWhatsapp():
	subprocess.run(["C:/Users/sromano/AppData/Local/WhatsApp/WhatsApp.exe"])
#	ubicacionLogoWhastapp = pyautogui.locateCenterOnScreen("media/logo10.png") #busca el logo de la aplicacion en la pantalla
#    pyautogui.leftClick(ubicacionLogoWhastapp) #clickea
time.sleep(1)#aguarda 
def buscarContacto():
  
    #RECONOCIMIENTO DE LA BARRA DE BUSQUEDA
    
    #cuando entramos a la aplicacion la barra de busqueda tiene un fondo negro,
    #pero si clickeamos un fondo gris, por eso "reconocimiento de como esta la barra de busqueda"
    
    lupaNegra = pyautogui.locateOnScreen("media/lupaNegra.png") #foto del primer estado de la barra
    lupaGris = pyautogui.locateOnScreen("media/lupaGris10.png")#foto del segundo
    
    #trato de sacar las coordenadas del primer estado
    try:
        x,y = pyautogui.center(lupaNegra) 
    except: 
        print("")
    #trato de sacar coordenadas del segundo estado
    try:
        a,b = pyautogui.center(lupaGris) 
    except:
        print("")
   
   #como no se cual de los dos estados existe. intento ir a los dos, sabiendo que solo va a ir uno.
   
    #lupa gris
    try: 
        A=int(a)
        B=int(b)
        pyautogui.leftClick(A,B) #me dirijo a la lupa gris
    except:
        print("")
  
    #lupa negra
    try:
        X= int(x)
        Y=int(y)
        pyautogui.leftClick(X,Y) #me dirijo a la lupa negra
    except:
        print("")
    
    
    
    #ESCRIBIR CONTACTO
    pyautogui.typewrite(numeroTelefono,interval=0.10) #escribir el numero
    time.sleep(2.5) #esperar que lo encuentre
    pyautogui.press("Tab") #lo selecciono
    pyautogui.press("Tab") #lo selecciono
    time.sleep(1)
    pyautogui.hotkey("enter")#entro al contacto
    time.sleep(2)#espero que cargue el chat
time.sleep(1)#aguardo
def mandarMensaje():
    #hago la secuencia para escribir el mensaje en el formato deseado
    for i in mensajeTexto: 
        pyautogui.typewrite(i)
        pyautogui.hotkey("Ctrl","Enter")
    time.sleep(0.5)
    pyautogui.press("Enter") #lo mando

def whatappBot():
    leerParametro()
    abrirWhatsapp()
    time.sleep(1.5)#espero un segundo y medio
    buscarContacto()
    time.sleep(1)#espero un segundo
    mandarMensaje()
        
whatappBot()
