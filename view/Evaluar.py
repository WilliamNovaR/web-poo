from model.Calificacion import Calificacion

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_evaluacion(st, controller, criterios_controller):
    nota_maxima = 5.0
    nota_minima = 0.0
    lista_nombres = []
    for nombres in controller.evaluaciones:
            lista_nombres.append( nombres.nombre_autor )
            if len( nombres.calificacion ):
                lista_nombres.pop()
    seleccion_estudiante = st.selectbox( "Calificar a:", lista_nombres )
    for evaluacion_obj in controller.evaluaciones:
        if evaluacion_obj.nombre_autor == seleccion_estudiante:
            lista_calificaciones = []
            criterios = []
            for i in range( len(  criterios_controller.criterios ) ):
                criterios.append(  criterios_controller.criterios[i].identificador )
                lista_calificaciones.append(Calificacion())
                lista_calificaciones[i].numero_jurados = 2
                lista_calificaciones[i].id_criterio = criterios_controller.criterios[i].identificador
                lista_calificaciones[i].ponderacion = criterios_controller.criterios[i].porcentaje_ponderacion
            for j in range( len( lista_calificaciones )  ):
                st.subheader( "Criterio "+ lista_calificaciones[j].id_criterio )
                lista_calificaciones[j].nota_jurado1 = st.number_input( "Nota jurado 1:", key = (j + 1) * 10, min_value = nota_minima, max_value = nota_maxima )
                lista_calificaciones[j].nota_jurado2 = st.number_input( "Nota jurado 2:", key = j, min_value = nota_minima, max_value = nota_maxima )
                lista_calificaciones[j].nota_final = round((lista_calificaciones[ j ].nota_jurado1 + lista_calificaciones[ j ].nota_jurado2) / lista_calificaciones[ j ].numero_jurados, 2)
                lista_calificaciones[j].comentario = st.text_input("Comentario:", key = (j + 1) * 20, )
                evaluacion_obj.nota = (lista_calificaciones[j].nota_final * lista_calificaciones[j].ponderacion) + evaluacion_obj.nota
            evaluacion_obj.nota = 0
            for j in range(len(lista_calificaciones)):
                evaluacion_obj.nota = (lista_calificaciones[j].nota_final * lista_calificaciones[j].ponderacion) + evaluacion_obj.nota
            evaluacion_obj.comentario_final = st.text_input( "Comentario Final:" )
            evaluacion_obj.correciones = st.text_input( "Correciones: " )
            if evaluacion_obj.nota >= 4.5:
                evaluacion_obj.recomendacion = st.text_input("Recomendación y apreciaciones:" )
            st.subheader("Nota final: " + str(evaluacion_obj.nota))
            if evaluacion_obj.nota > 3.5:
                st.success( "Aprobado" )
            else:
                st.error( "Reprobado" )
            enviado_btn = st.button("Send")
            evaluacion_obj.nota = round(evaluacion_obj.nota, 1)

            if enviado_btn:
                evaluacion_obj.calificacion = lista_calificaciones
                st.success("Evaluacion agregada exitosamente")
            else:
                st.error( "Faltan criterios por calificar!" )

    return controller


def listar_evaluacion(st, controller, criterios_controller ):
    st.title("Ver y editar calificaciones")
    ver_editar = st.radio("Que quieres hacer?", ('Ver', 'Editar') )
    estudiantes_nombres = []
    criterios = []
    for estudiantes in controller.evaluaciones:
        estudiantes_nombres.append( estudiantes.nombre_autor )
    for criterio in criterios_controller.criterios:
        criterios.append(criterio.identificador)
    seleccionar_estudiantes = st.selectbox( "seleccioanr estudiante", estudiantes_nombres )
    evaluacion: object
    for evaluacion in controller.evaluaciones:
        if seleccionar_estudiantes == evaluacion.nombre_autor:
            if ver_editar == 'Ver':
                st.subheader( "Id autor: " + evaluacion.id_estudiante )
                st.subheader( "Periodo evaluacion: " + evaluacion.periodo )
                st.subheader("Nombre autor: " + evaluacion.nombre_autor)
                st.subheader("Tipo de trabajo: " + evaluacion.tipo_trabajo)
                st.subheader("Titulo del trabajo: " + evaluacion.nombre_trabajo)
                st.subheader("Nombre director: " + evaluacion.nombre_director)
                st.subheader("Nombre codirector: " + evaluacion.nombre_codirector)
                st.subheader("Enfasis en: " + evaluacion.enfasis)
                st.subheader("Jurado1 : " + evaluacion.nombre_jurado1)
                st.subheader("Jurado2 : " + evaluacion.nombre_jurado2)
                seleccionar_criterio = st.selectbox("Escoger criterio", criterios)
                for i in evaluacion.calificacion:
                    if seleccionar_criterio == i.id_criterio:
                        st.subheader( "Nota jurado 1: " + str(i.nota_jurado1) )
                        st.subheader("Nota jurado 2: " + str(i.nota_jurado2) )
                        st.subheader( "Nota del criterio: " + str(i.nota_final) )
                        st.subheader("Comentario: ")
                        st.write( "" + i.comentario )
                st.subheader("Nota final : " + str(evaluacion.nota) )
                st.subheader("Comentario final : " + evaluacion.comentario_final)
                if evaluacion.nota >= 4.5:
                    st.subheader("Recomendación y apreciaciones: " + evaluacion.recomendacion)
            else:
                evaluacion.id_estudiante = st.text_input("Id estudiante", value = evaluacion.id_estudiante  )
                evaluacion.periodo = st.text_input("Periodo de evaluacion", value = evaluacion.periodo )
                evaluacion.nombre_autor = st.text_input("Nombre del autor", value = evaluacion.nombre_autor)
                if evaluacion.tipo_trabajo == 'Aplicado':
                    evaluacion.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion') )
                else:
                    evaluacion.tipo_trabajo = st.radio("Tipo de trabajo", ('Aplicado', 'Investigacion') , index = 1 )
                evaluacion.nombre_trabajo = st.text_input("Nombre del trabajo", value = evaluacion.nombre_trabajo )
                evaluacion.nombre_director = st.text_input("Nombre del director", value = evaluacion.nombre_director )
                st.write("codirector?")
                if evaluacion.nombre_codirector == "No aplica":
                    coodirector = st.radio("El trabajo tiene codirector?", ('Si', 'No'), index = 1 )
                else:
                    coodirector = st.radio("El trabajo tiene codirector?", ('Si', 'No'))
                if coodirector == 'Si':
                    evaluacion.nombre_codirector = st.text_input("Nombre del codirector", value = evaluacion.nombre_codirector )
                evaluacion.enfasis = st.text_input("Enfasis en:", value = evaluacion.enfasis )
                evaluacion.nombre_jurado1 = st.text_input("Nombre del jurado1", value = evaluacion.nombre_jurado1 )
                evaluacion.nombre_jurado2 = st.text_input("Nombre del jurado2", value = evaluacion.nombre_jurado2 )
                seleccionar_criterio = st.selectbox("Escoger criterio", criterios)
                for i in evaluacion.calificacion:
                    if seleccionar_criterio == i.id_criterio:
                        evaluacion.nota -= (( ( i.nota_jurado1 + i.nota_jurado2 ) / 2 ) * i.ponderacion)
                        i.nota_jurado1 = st.number_input("Nota jurado 1: ", value = i.nota_jurado1)
                        i.nota_jurado2 = st.number_input("Nota jurado 2: ", value = i.nota_jurado2)
                        i.comentario = st.text_input("Comentario ", value = i.comentario)
                        i.nota_final = ( i.nota_jurado1 + i.nota_jurado2 )
                        evaluacion.nota += ((i.nota_final) * i.ponderacion)
                evaluacion.comentario_final = st.text_input( "Comentario final", value = evaluacion.comentario_final )
                if evaluacion.nota >= 4.5:
                    evaluacion.recomendacion = st.text_input( "Recomendación y apreciaciones: ", value = evaluacion.recomendacion )
                enviar_btn = st.button( "Editar" )
                if enviar_btn:
                    st.success( "Cambio realizado" )