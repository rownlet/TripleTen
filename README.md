# Data Science Bootcamp Projects

Bienvenido a la documentación de los proyectos desarrollados durante el Bootcamp de Ciencia de Datos en **TripleTen**. A lo largo del Bootcamp, se aplicaron técnicas de análisis de datos, limpieza, transformación y modelado utilizando herramientas de Data Science y Software Development.  

Cada proyecto cuenta con una descripción detallada del contexto, las herramientas utilizadas, el proceso de desarrollo, los análisis de resultados y las conclusiones.  

Para quienes deseen ejecutar el código y validar los resultados obtenidos, el repositorio con los datos se encuentra disponible en el siguiente enlace:  

📂 **Repositorio en Google Drive:** [Acceder a los archivos](https://drive.google.com/drive/folders/1VWdZzKb58ncf8SD0QUKrhCRngkU0ApIK?usp=drive_link)  

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

## Proyecto 3: Nombre del Proyecto

*(Información pendiente de agregar...)*

---

## Herramientas y Tecnologías

- **Frontend:** HTML, CSS, JavaScript, frameworks modernos (React, Angular, etc.)
- **Backend:** Node.js, Python (Django, Flask), entre otros.
- **Bases de Datos:** MySQL, PostgreSQL, MongoDB, etc.
- **Otras herramientas:** Git, GitHub, Docker, herramientas de testing, etc.

---

## Guía de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
