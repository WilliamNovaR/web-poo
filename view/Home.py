from PIL import Image
"""Instructions"""


def consultar_instrucciones(st):
    img = Image.open( "C:\\Users\\willi\\OneDrive\\Escritorio\\imagenes\\logo.png" )
    img2 = Image.open( "C:\\Users\\willi\\OneDrive\\Escritorio\\imagenes\\PlazoletaJaverianaCali.jpg" )
    col1, col2 = st.columns([1.1, 10])

    with col1:

        st.image(img, width=75)
    with col2:
        st.header("Calificacion de trabajos finales")

    st.write("Programa de la Universidad Javeriana Cali realizado para la evaluación de proyectos de grado de posgrado,"
             " creación y descargar de las actas de calificacion")
    st.write( "Dependiendo de tu rol tenemos diferentes acciones para ti:" )
    st.write(" * Asistente -> Creación del Acta de Evaluación y ver actas creadas ")
    st.write(" * Jurado -> Calificar, Exportar acta, editar calificacion y ver calificaciones realizadas ")
    st.write(" * Director/a -> Modificar los criterios de calificacion y ver las actas creadas")
    st.image( img2, caption='Software made by William Nova' )




