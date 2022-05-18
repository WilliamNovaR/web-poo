#clase creada para almacenar las calificaciones de cada uno de los criterios a evaluar

class Calificacion:

    def __int__(self) -> None:
        self.numero_jurados = 0
        self.id_criterio = ""
        self.ponderacion = 0
        self.nota_jurado1 = 0
        self.nota_jurado2 = 0
        self.nota_final = 0
        self.comentario = ""

    def crear_dic(self):
        diccionario = { 'numero_jurados':self.numero_jurados,'id_criterio':self.id_criterio,'ponderacion':self.ponderacion,'nota_jurado1':self.nota_jurado1,'nota_jurado2':self.nota_jurado2,'nota_final':self.nota_final,'comentario':self.comentario }
        return diccionario