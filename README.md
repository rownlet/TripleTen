# Data Science Bootcamp Projects

Welcome to the documentation of the projects developed during the Data Science Bootcamp at TripleTen. Throughout the Bootcamp, data analysis, cleansing, transformation and modeling techniques were applied using tools of Data Science and Software Development.

Each project has a detailed description of the context, tools used, development process, results analysis and conclusions.

For those who wish to run the code and validate the results obtained, the repository with the data is available at the following link: 

📂 **Repository in Google Drive:** [Portfolio](https://drive.google.com/drive/folders/1VWdZzKb58ncf8SD0QUKrhCRngkU0ApIK?usp=drive_link)  

---

## Tabla de Contenido

- [Proyecto 1: Evaluación y Preparación de Datos de Store 1](#proyecto-1-evaluación-y-preparación-de-datos-de-store-1)
- [Proyecto 2: Análisis de Preferencias Musicales - "Déjame escuchar la música"](#proyecto-2-análisis-de-preferencias-musicales)
- [Proyecto 3: Nombre del Proyecto](#proyecto-3-nombre-del-proyecto)
- [Herramientas y Tecnologías](#herramientas-y-tecnologías)
- [Guía de Ejecución](#guía-de-ejecución)
- [Contacto](#contacto)

---

## Proyecto 1: Evaluación y Preparación de Datos de Store 1

### Contexto
Una empresa de comercio electrónico, **Store 1**, recientemente comenzó a recopilar datos sobre sus clientes. Su objetivo final es comprender mejor el comportamiento de los usuarios y tomar decisiones basadas en datos para mejorar su experiencia online. Como parte del equipo de análisis, la primera tarea consiste en evaluar la calidad de una muestra de datos recopilados y prepararla para futuros análisis.

### Herramientas y Tecnologías Utilizadas
El análisis de los datos fue realizado utilizando herramientas de procesamiento y limpieza de datos en **Python**. Se emplearon librerías como:
- **Pandas** para manipulación y transformación de datos.
- **NumPy** para cálculos numéricos.
- **Matplotlib / Seaborn** para visualización de datos (si aplica).
- **Regex** para correcciones de formato en variables de texto.

### Desarrollo y Análisis de Datos
Durante la evaluación de la calidad de los datos, se identificaron las siguientes inconsistencias:
1. La variable **user_name** contenía espacios innecesarios y un guion bajo entre el nombre y el apellido, lo que podía causar problemas en la estandarización de los datos.
2. La variable **user_age** estaba almacenada como número decimal en lugar de entero, lo que podía dificultar operaciones matemáticas sobre la edad.
3. La lista **fav_categories** contenía cadenas en mayúsculas, lo que podía afectar la coherencia en el análisis. Se sugirió convertirlas a minúsculas para mejorar la consistencia.

### Conclusiones
El proceso de limpieza y normalización de datos permitió mejorar la calidad de la información para análisis futuros. La corrección de formatos en los nombres, edades y preferencias de los clientes ayuda a garantizar una mejor integración de los datos en futuros modelos analíticos.

**Repositorio:** [Enlace al repositorio](https://drive.google.com/drive/folders/1VWdZzKb58ncf8SD0QUKrhCRngkU0ApIK?usp=drive_link)

---

## Proyecto 2: Análisis de Preferencias Musicales - "Déjame escuchar la música"

### Contexto
Como analista de datos, el objetivo de este proyecto es analizar datos de transmisión de música online para identificar patrones de consumo en dos ciudades: **Springfield** y **Shelbyville**. A través del análisis de datos, se busca validar hipótesis sobre el comportamiento de los usuarios y usuarias con respecto a la reproducción de música en diferentes días de la semana.

### Herramientas y Tecnologías Utilizadas
Para el análisis de datos se emplearon las siguientes herramientas:
- **Pandas** para manipulación y limpieza de datos.
- **NumPy** para cálculos numéricos.
- **Matplotlib / Seaborn** para visualización de patrones y tendencias en los datos.
- **Métodos estadísticos** para la validación de hipótesis.

### Desarrollo y Análisis de Datos
El proyecto se llevó a cabo en tres etapas principales:

1. **Descripción de los Datos**  
   Se revisó la estructura del conjunto de datos (`music_project_en.csv`) y se analizaron las variables disponibles para la comparación de patrones de escucha.

2. **Preprocesamiento de Datos**  
   Se corrigieron problemas en los datos, tales como:
   - Errores en los encabezados de las columnas.
   - Manejo de valores ausentes.
   - Eliminación de duplicados.
   - Conversión de tipos de datos para asegurar la coherencia del análisis.

3. **Prueba de Hipótesis**  
   Se comparó el número de canciones reproducidas en **lunes, miércoles y viernes** para determinar si el comportamiento de los usuarios/as variaba entre ciudades y días de la semana.  
   **Conclusión de la prueba de hipótesis:**  
   - En **Springfield**, los viernes son los días de mayor reproducción de música.  
   - En **Shelbyville**, los miércoles presentan la mayor actividad de reproducción.  
   - En general, Springfield muestra un mayor volumen de reproducción de música en comparación con Shelbyville.  

### Conclusiones
Los resultados confirmaron diferencias significativas en el consumo de música entre ambas ciudades. Se observó que la frecuencia de reproducción varía según el día de la semana y la ubicación geográfica. Esto sugiere que las plataformas de streaming pueden optimizar sus estrategias de recomendación y promociones en función del comportamiento de sus usuarios en cada ciudad.

---

## Proyecto 3: Análisis de Pedidos en Instacart - "¡Llena ese carrito!"

### Contexto
Instacart es una plataforma de entregas de comestibles que permite a los clientes registrar un pedido y recibirlo en su domicilio. El objetivo de este proyecto es analizar los datos de pedidos para identificar patrones de compra y optimizar la experiencia del usuario en la plataforma. 

El conjunto de datos utilizado ha sido modificado para reducir su tamaño y hacer que los cálculos sean más rápidos. Además, se introdujeron valores ausentes y duplicados para mejorar la experiencia de limpieza y preparación de datos.

### Herramientas y Tecnologías Utilizadas
Para el análisis de datos se emplearon las siguientes herramientas:
- **Pandas** para manipulación y limpieza de datos.
- **NumPy** para cálculos numéricos.
- **Matplotlib / Seaborn** para visualización de patrones y tendencias en los datos.
- **Métodos estadísticos** para análisis exploratorio de datos y optimización de procesos.

### Desarrollo y Análisis de Datos
El proyecto se llevó a cabo en varias etapas principales:

1. **Preprocesamiento de Datos**
   - Verificación y corrección de tipos de datos en columnas clave.
   - Identificación y manejo de valores ausentes en los pedidos y productos.
   - Eliminación de valores duplicados para garantizar la integridad de los datos.
   - Conversión de datos categóricos y numéricos a formatos adecuados.

2. **Análisis de Patrones de Compra**
   - Evaluación de las horas y días con mayor actividad de compras.
   - Identificación de productos más populares y su frecuencia de compra.
   - Análisis de la repetición de compras y hábitos de los clientes.

3. **Validación de Datos**
   - Revisión de la calidad de los datos y verificación de posibles errores de entrada.
   - Aplicación de imputaciones y correcciones en las variables afectadas.

### Conclusiones
Los resultados confirmaron importantes patrones de comportamiento en los pedidos de Instacart:
- **Horarios de compra:** La actividad de pedidos se concentra en ciertas horas del día y días de la semana.
- **Productos populares:** Algunos productos tienen una alta tasa de recompra, lo que sugiere patrones de consumo regulares.
- **Estrategia de recomendaciones:** El análisis de repeticiones de compra permite mejorar las recomendaciones y personalizar la experiencia del usuario.

Estos hallazgos pueden ser utilizados por Instacart para optimizar la distribución de productos y mejorar la personalización de las ofertas para sus clientes.

---

## Proyecto 4: Análisis de Tarifas de Telecomunicaciones - "¿Cuál es la mejor tarifa?"

### Contexto
Trabajas como analista de datos para la empresa de telecomunicaciones **Megaline**, que ofrece dos tarifas de prepago: **Surf** y **Ultimate**. El objetivo del proyecto es determinar cuál de estas tarifas genera más ingresos para ayudar al equipo comercial a optimizar el presupuesto de publicidad.

Para el análisis, se dispone de los datos de 500 clientes, incluyendo información sobre su consumo de llamadas, mensajes de texto y uso de Internet a lo largo de 2018.

### Herramientas y Tecnologías Utilizadas
Para el análisis de datos se emplearon las siguientes herramientas:
- **Pandas** para manipulación y limpieza de datos.
- **NumPy** para cálculos numéricos.
- **Matplotlib / Seaborn** para visualización de tendencias en los datos.
- **Pruebas estadísticas** (prueba t de Student) para validar diferencias en ingresos entre los planes.

### Desarrollo y Análisis de Datos
El proyecto se llevó a cabo en varias etapas principales:

1. **Limpieza y Preprocesamiento de Datos**
   - Conversión de fechas a formato `datetime` para facilitar el análisis temporal.
   - Manejo de valores ausentes y estandarización de tipos de datos.
   - Redondeo de la duración de las llamadas para alinearse con la política de facturación de la empresa.
   - Consolidación de datos de consumo (llamadas, mensajes e Internet) en un solo conjunto de datos por usuario.

2. **Análisis del Comportamiento del Cliente**
   - Exploración del uso de llamadas, mensajes y datos por tipo de tarifa.
   - Identificación de patrones de consumo y diferencias entre usuarios de los planes **Surf** y **Ultimate**.

3. **Análisis de Ingresos**
   - Cálculo del ingreso mensual por usuario.
   - Comparación de ingresos entre planes y regiones geográficas.
   - Evaluación de la rentabilidad de cada plan.

4. **Pruebas Estadísticas**
   - Aplicación de pruebas estadísticas (prueba t de Student) para determinar si las diferencias en ingresos entre los dos planes son estadísticamente significativas.
   - Validación de hipótesis sobre patrones de uso y rentabilidad de los planes.

### Conclusiones
Los resultados confirmaron diferencias significativas en el consumo de servicios entre los usuarios de los planes **Surf** y **Ultimate**:
- **El plan Ultimate genera mayores ingresos promedio que el plan Surf** debido a un mayor consumo de datos y llamadas por parte de sus usuarios.
- **El uso de mensajes de texto ha disminuido**, lo que sugiere que los clientes prefieren comunicarse a través de datos móviles.
- **Los ingresos varían por región**, lo que puede ayudar a definir estrategias de marketing más focalizadas.

Estos hallazgos pueden ayudar a la empresa **Megaline** a tomar decisiones estratégicas sobre su estructura de precios y campañas de publicidad.

---

## Guía de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
