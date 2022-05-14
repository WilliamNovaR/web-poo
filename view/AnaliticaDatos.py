from model.EvalEstudiante import EvaluacionEstudiante
import matplotlib.pyplot as plt



def analisis(st, controller, criterio_controler):
    opcion = st.radio( "Que analisis quieres hacer?", ('Encontrar Calificacion más alta', 'notas estudiantes', 'Estadistica criterios') )
    if opcion == 'Encontrar Calificacion más alta':
        if len( controller.evaluaciones ) > 0:
            mejor_calificacion = EvaluacionEstudiante()
            for i in controller.evaluaciones:
                if i.nota > mejor_calificacion.nota:
                    mejor_calificacion = i
            st.subheader( "El estudiante con mejor calificiacion es: " + mejor_calificacion.nombre_autor )
            st.subheader("Id:" + mejor_calificacion.id_estudiante)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
            st.subheader("Nota: " + str(round(mejor_calificacion.nota, 1)))
        else:
            st.error( "No han calificado a nadie" )
    elif opcion == 'notas estudiantes':
        notas = []
        nombres = []
        for i in controller.evaluaciones:
            if len(i.calificacion) > 0:
                nombres.append(i.nombre_autor)
                notas.append( i.nota )
        print( notas )
        fig = plt.figure(figsize=(10, 5))
        plt.bar(nombres, notas)
        plt.xlabel("Notas de estudiantes")
        plt.ylabel("Nombre estudiantes")
        plt.title("Notas")
        st.pyplot(fig)

    elif opcion == 'Estadistica criterios':
        cantidad = 0
        nombre_criterios = []
        notas = []
        numeros_criterio = []
        contador = 1
        for personas in controller.evaluaciones:
            if len(personas.calificacion) > 0:
                cantidad += 1
        for name in criterio_controler.criterios:
            notas.append( 0 )
            nombre_criterios.append( name.identificador )
            numeros_criterio.append( contador  )
            contador += 1
        for i in controller.evaluaciones:
            for j in range(len(i.calificacion)):
                notas[j] += i.calificacion[j].nota_final
        for k in range(len(notas)):
            if cantidad > 0:
                notas[k] /= cantidad
                print(notas[k])
        fig = plt.figure(figsize=(10, 5))
        plt.bar(numeros_criterio, notas)
        plt.xlabel("Criterios")
        plt.ylabel("Notas criterios")
        plt.title("Notas")
        st.pyplot(fig)
        for iterador in range( len(nombre_criterios) ):
            st.write( str(numeros_criterio[iterador]) + " = " + nombre_criterios[iterador]  )



