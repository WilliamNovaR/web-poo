from model.Cuenta import Cuenta


def crear_cuenta(st, cuentaController):
    nueva_cuenta = Cuenta()
    nueva_cuenta.usuario = st.text_input( "Usuario:", value = '' )
    nueva_cuenta.contrasena = st.text_input( "Contraseña:", value= ''  )
    nueva_cuenta.tipo = st.radio( "Que tipo de cuenta quieres crear?", ('Asistente', 'Jurado', 'Director/a') )
    crear = st.button( "Crear" )
    if crear:
        cuentaController.cuentas.append( nueva_cuenta )
        st.success( "Cuenta creada" )
        print( len( cuentaController.cuentas ) )

def iniciar_sesion( st, cuentasController, accionesController):
    usuario = st.text_input( "Usuario:", key = 23 )
    contrasena = st.text_input( "Contraseña:", key = 7 )
    col1, col2 = st.columns([0.2,1])
    with col1:
        login = st.button( "Iniciar sesion" )
        if login:
            for i in cuentasController.cuentas:
                if usuario == i.usuario and contrasena == i.contrasena:
                    if i.tipo == 'Asistente':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion',
                                                       'Inicilizar datos actas', 'Ver historico resumido actas',
                                                       'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'upload', 'book',
                                                     'file-bar-graph', 'person-x' ]
                    elif i.tipo == 'Jurado':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion', 'Evaluar nuevo trabajo',
                                                       'Ver o editar calificaciones', 'Exportar acta' , 'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'clipboard',
                                                     'clipboard-check', 'file-pdf','file-bar-graph', 'person-x']
                    elif i.tipo == 'Director/a':
                        accionesController.acciones = ['Home', 'Crear cuenta', 'Iniciar sesion',
                                                       'Modificar y ver criterios',
                                                       'Ver historico resumido actas', 'Estadisticas', 'Cerrar sesion']
                        accionesController.iconos = ['house', 'person-plus', 'person-check', 'list-check',
                                                     'book', 'file-bar-graph', 'person-x']
                    with col2:
                        st.button("Entrar")
                        return
            st.error( "Datos no validos" )

def cerrar_sesion(st, accionesController):
    st.subheader( "Cerrar sesion" )
    col1, col2 = st.columns([0.2, 1])
    with col1:
        logout = st.button("Cerrar sesion")
        if logout:
            accionesController.acciones = ["Home", 'Crear cuenta', 'Iniciar sesion']
            accionesController.iconos = [ 'house', 'person-plus', 'person-check' ]
            with col2:
                st.button("Salir")







