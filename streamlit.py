# --------------------LIBRERÍAS----------------------------#
import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model
from PIL import Image

# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(
    page_title="Alojamiento en la Ciudad de Mexico.",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Logo_Secretaria_de_Gobierno_de_la_Ciudad_de_M%C3%A9xico.png/640px-Logo_Secretaria_de_Gobierno_de_la_Ciudad_de_M%C3%A9xico.png"



# Función principal
def main():
    # --------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#

    df = pd.read_csv("C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/Streamlit_proyecto_2/data/datos_limpios_airbnb_columnas_finales.csv")

    # --------------------HEADER----------------------------#
    st.image(logo, width=350)
    st.title("Análisis del alquiler turístico en Ciudad de México")
    
    
    # --------------------BODY----------------------------#


    # --------------------TABS----------------------------#
    tab1, tab2, tab3 = st.tabs(
        ["Introducción", "Paneles Descriptivos", "Predictor de Precio"]
    )
    # --------------------PRESENTACIÓN----------------------------#
    with tab1:
        st.header("Introducción")
    
        # Lista de rutas de las imágenes locales
        image_paths = ["C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/fotos/1.PNG", "C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/fotos/2.PNG", "C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/fotos/3.PNG", "C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/fotos/4.PNG", "C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/fotos/5.PNG"]  
        
        # Carga y muestra las imágenes
        for image_path in image_paths:
            image = Image.open(image_path)
            st.image(image, caption='Image', use_column_width=True)



    # --------------------PANELES DESCRPTIVOS----------------------------#
    with tab2:
        st.header("Paneles Descriptivos")
        st.markdown(f'<iframe title="Ciudad_de_Mexico_2" width="800" height="836" src="https://app.powerbi.com/view?r=eyJrIjoiYjYzYWVjNTAtM2IwMC00Y2ZkLWIzMTItMmQ0NGVlMWE4MjA2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=ReportSection2ad6698e3ca009e83e74" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
            # Aquí puedes agregar tus enlaces de los paneles de Power BI usando la función st.markdown o st.components.

    # --------------------PREDICTOR DE PRECIO----------------------------#
    with tab3:
        st.title('Predicción del precio de alojamiento en Ciudad de México')

        # Cargar el modelo entrenado
        model = load_model("C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/Streamlit_proyecto_2/models/dt_model")

        # Cargar el DataFrame con los datos
        df = pd.read_csv("C:/Users/pejer/Desktop/BOOTCAMP/9-PROYECTOS/Proyecto_Modulo_2/Streamlit_proyecto_2/data/datos_limpios_airbnb_columnas_finales.csv")

        # Definir diccionario para mapear valores numéricos a nombres de barrios
        neighbourhood_dict = {
            1: 'Álvaro Obregón',
            2: 'Azcapotzalco',
            3: 'Benito Juárez',
            4: 'Coyoacán',
            5: 'Cuajimalpa de Morelos',
            6: 'Cuauhtémoc',
            7: 'Gustavo A. Madero',
            8: 'Iztacalco',
            9: 'Iztapalapa',
            10: 'La Magdalena Contreras',
            11: 'Miguel Hidalgo',
            12: 'Milpa Alta',
            13: 'Tláhuac',
            14: 'Tlalpan',
            15: 'Venustiano Carranza',
            16: 'Xochimilco'
        }

        # Definir diccionario para mapear valores numéricos a nombres de tipo de alojamiento
        room_type_dict = {
            1: 'Vivienda completa',
            2: 'Habitación privada',
            3: 'Habitación compartida',
            4: 'Habitacion de hotel'
        }

        # Factor de conversión de pesos mexicanos a euros
        factor_conversion = 0.056

        # Formulario para la predicción
        with st.form("prediction_form"):
            # Campos de entrada para los predictores
            barrio = st.selectbox('Barrio', df['neighbourhood_group_cleansed'].map(neighbourhood_dict).unique())
            room_type = st.selectbox('Tipo de alojamiento', df['room_type'].map(room_type_dict).unique(), index=0)
            
            # Si el tipo de alojamiento no es "Vivienda completa"
            if room_type != 'Vivienda completa':
                # Limitar la selección de habitaciones a 1
                habitaciones = 1
                st.write("Se ha establecido automáticamente el número de habitaciones a 1 debido al tipo de alojamiento seleccionado.")
                
                # Limitar el número de personas entre 1 y 12
                accommodates = st.selectbox('Número de personas', list(range(1, 13)), index=0)
                
                # Limitar el número de camas a 8
                camas = st.selectbox('Número de camas', list(range(1, 9)), index=0)
            else:
                habitaciones = st.selectbox('Número de habitaciones', list(range(1, 36)), index=0)
                accommodates = st.selectbox('Número de personas', list(range(1, 50)), index=0)
                camas = st.selectbox('Número de camas', list(range(1, 50)), index=0)
            
            calidad = st.selectbox('Calificación (1 sobre 5)', list(range(1, 5)), index=0)
            
            # Botón para realizar la predicción
            submitted = st.form_submit_button("Predecir Precio")
            if submitted:
                # Mapear valores seleccionados por el usuario a los valores numéricos
                barrio_numeric = list(neighbourhood_dict.keys())[list(neighbourhood_dict.values()).index(barrio)]
                room_type_numeric = list(room_type_dict.keys())[list(room_type_dict.values()).index(room_type)]
                
                # Preparar los datos de entrada para la predicción
                input_data = pd.DataFrame([[barrio_numeric, habitaciones, room_type_numeric, accommodates, camas, calidad]],
                                          columns=['neighbourhood_group_cleansed', 'habitaciones', 'room_type', 'accommodates', 'camas', 'total_review'])
                input_data['host_calification_score'] = 7.35  

                # Predecir el precio utilizando el modelo cargado
                prediction = predict_model(model, data=input_data)

                # Obtener la predicción de precio
                predicted_price = prediction.iloc[0, -1]

                # Convertir el precio de pesos mexicanos a euros
                predicted_price_eur = predicted_price * factor_conversion

                # Mostrar el precio convertido al usuario
                st.subheader(f"El precio del alojamiento en {barrio} será de {predicted_price_eur:.2f} € por noche aproximadamente.")

if __name__ == "__main__":
    main()

