class Toronja:

    def __init__(self):
        self.__nombre = None
        self.__cantidad=None
        self.__precio = None
        self.__vitaminaAportada=None

    #DECLARANDO EL METODO GET(OBTENGO/MUESTRO UN ATRIBUTO)
    @property
    def nombre(self):
        return self.__nombre
    
    #DECLARANDO EL METODO GET(CONFIGURO,LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre = dato

    def agregarFrutar(self):

        print("Se pela y se hecha")

    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,dato):
        self.__cantidad = dato

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,dato):
        self.__precio = dato

    @property
    def vitaminaAportada(self):
        return self.vitaminaAportada
    
    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
        self.__vitaminaAportada = dato