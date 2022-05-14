from model.Acta import PDF
from datetime import datetime
import base64


# esta funcion permite crear la opcion de descargar la acta creada
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

#la funcion establece los datos del acta y permite descargarla
def crearActa(st, actas_controller, controller):
    st.title("Crear acta")
    lista_nombres = [] # creamos un arreglo para almacenar todos los nombres de los estudiantes calificados para poner estos en el select box
    for nombres in controller.evaluaciones:
        if len(nombres.calificacion) > 0 :
            lista_nombres.append(nombres.nombre_autor) #el ciclo recorre el arreglo que tiene todas las calificaciones y guarda en el arreglo los nombres
    seleccionar_estudiante_acta = st.selectbox("a que estudiante le quieres hacer el acta?", lista_nombres)
    indice_estudiante = 0
    key = 7
    for nombre in controller.evaluaciones:
        if nombre.nombre_autor == seleccionar_estudiante_acta:
            acta = PDF('P', 'mm', 'Letter')
            acta.nombre_pdf = 'acta' + str(len(actas_controller.actas) + 1) + seleccionar_estudiante_acta + '.pdf'
            acta.nombre_pdf = st.text_input("Nombre con el que se guardara el pdf del acta", value=acta.nombre_pdf, key = key)
            if st.button("Crear acta", key = key * 123):
                acta.set_left_margin(10.0)
                acta.fecha = datetime.today().strftime('%Y-%m-%d')
                acta.num_acta = str(len(actas_controller.actas) + 1) + '-' + datetime.today().strftime('%Y')
                acta.set_auto_page_break(auto=True, margin=15)
                acta.add_page()
                acta.titulo += controller.evaluaciones[indice_estudiante].nombre_trabajo + '"'
                acta.autor = controller.evaluaciones[indice_estudiante].nombre_autor
                acta.id = controller.evaluaciones[indice_estudiante].id_estudiante
                acta.periodo = controller.evaluaciones[indice_estudiante].periodo
                acta.director = controller.evaluaciones[indice_estudiante].nombre_director
                acta.codirector = controller.evaluaciones[indice_estudiante].nombre_codirector
                acta.enfasis = controller.evaluaciones[indice_estudiante].enfasis
                acta.modalidad = controller.evaluaciones[indice_estudiante].tipo_trabajo
                acta.jurado1 = controller.evaluaciones[indice_estudiante].nombre_jurado1
                acta.jurado2 = controller.evaluaciones[indice_estudiante].nombre_jurado2
                acta.datos()
                contador = 1
                for i in controller.evaluaciones[indice_estudiante].calificacion:
                    acta.num_criterio = str(contador) + "."
                    acta.nombre_criterio = i.id_criterio
                    acta.ponderacion = 'Ponderacion: ' + str(i.ponderacion * 100) + '%'
                    acta.calificacion = str(i.nota_final)
                    acta.observacion = 'Observaciones: ' + i.comentario
                    acta.criterio()
                    contador += 1
                acta.calificacion_final = str(controller.evaluaciones[indice_estudiante].nota)
                acta.comentario_final = 'Observaciones adicionales: ' + controller.evaluaciones[indice_estudiante].comentario_final
                acta.correcciones = 'La calificación final queda sujeta a que se implementen las siguientes correcciones: ' + controller.evaluaciones[indice_estudiante].correciones
                acta.nota_final()
                acta.firmas()
                if float(acta.calificacion_final) >= 4.5:
                    acta.add_page()
                    acta.datos()
                    acta.extra()
                html = create_download_link(acta.output(dest="S").encode("latin-1"), acta.nombre_pdf)
                actas_controller.actas.append(acta)
                st.success("Acta Creada")
                st.markdown(html, unsafe_allow_html=True)
            key *= key + 4
        indice_estudiante += 1
