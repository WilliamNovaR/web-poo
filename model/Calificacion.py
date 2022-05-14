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
