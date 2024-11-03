# Proyecto Urban Routes 

### 1. Título del Proyecto:
## "Prueba de Proceso de Pedir un Taxi" 
### Pruebas automatizadas que cubren el proceso completo de pedir un taxi en la aplicación.
### Axel Van Dyck, Grupo 14, Sprint 8
### 2. Descripción

Propósito: Este proyecto automatiza el proceso de pedir un taxi a través de la plataforma Urban.Routes.
Se cubren los siguientes pasos:

1. [x] Completar los campos de dirección "Desde" y "Hasta" para establecer una ruta.
2. [x] Seleccionar la tarifa "Comfort".
3. [x] Rellenar los campos de número de teléfono, obtención del código de confirmación, 
y aserción del contenido del campo.
4. [x] Rellenar los campos de método de pago.
5. [x] Colocación de comentario para el conductor, y aserción del mismo.
6. [x] Definir ajustes de viaje:
    - #### Pedir una manta y pañuelos.
    - #### Pedir 2 helados.
7. [x] Aserción de ventana emergente de búsqueda de taxi.
8. [x] Aserción de **ventana emergente de información del conductor**.
9. [x] Aserción de presencia y funcionalidad de botones de configuración de viaje.

## **3. Requisitos Previos**

**Lenguaje**: Python 3.x

    Bibliotecas/Dependencias:

    Selenium
    Pytest
    Webdriver para Chrome
    DesiredCapabilities (Chrome)
    ExpectedConditions
    WebDriverWait
    

## 4. Estructura del Proyecto

### **data.py**:
Hoja de datos que almacena la URL, datos del formulario de taxi, y direcciones para los campos "Desde" y "Hasta".
### **locators.py**: 
Almacena los localizadores de la página; en formato CSS_Selector, y XPATH. 
### **methods.py**:
Almacena la clase "UrbanRoutes" que contiene los métodos (funciones) a realizar por la clase de pruebas.
### **sms_code**:
Intercepta el código de confirmación para el campo de verificación de teléfono.

## 5. Instrucciones de Uso
Para ejecutar las pruebas, utiliza el siguiente comando en la terminal:

pytest -v main.py

**Recomiendo utilizar el operador -v para devolver un detalle más verboso de la prueba.**

## 6. 14 Casos de Prueba Disponibles:


      test_set_route: Verifica que la ruta inicial (origen y destino) se configure correctamente al inicio del proceso.
      
      test_ask_for_taxi_button: Confirma que el botón "Pedir un taxi" esté habilitado y el usuario acceda a las configuraciones.
         
      test_set_comfort_fare: Asegura que el botón de "Tarifa Comfort" esté disponible para su selección.
      
      test_phone_modal_appears: Verifica que el modal para introducir el número de teléfono aparezca.
         
      test_fill_phone_requirements: Rellena los campos para el teléfono y se asegura de esperar un codigo de verificacion.
         
      test_fill_phone_code: Intercepta el código, rellena el campo, y Comprueba que el número de teléfono es el esperado después de ingresar el código de verificación.
         
      test_select_payment_info: Confirma que el botón de "Método de Pago" esté habilitado.
         
      test_fill_payment_info: Verifica que el botón "Agregar tarjeta" sea visible y que el formulario de tarjeta esté accesible, entonces
                              rellena la informacion de pago.
         
      test_assert_card_info: Confirma que el número de tarjeta y el código coinciden con los datos ingresados.
         
      test_comment_for_driver: Asegura que el comentario ingresado para el conductor se guarde correctamente.
         
      test_define_ride_amenities: Comprueba que se muestren las opciones de "Amenidades" y que se puedan seleccionar.
         
      test_ice_cream_for_rider: Verifica que el contador de helados esté en cero inicialmente, que se pueda agregar helado, y que el conteo sea el correcto.
         
      test_confirm_taxi_modal_shows_up: Asegura que el botón "Confirmar" y el modal de búsqueda del taxi sean visibles.
         
      test_show_driver_info: Verifica que aparezca la información del conductor una vez el viaje esté confirmado.



