# Data-Analysis-Portfolio
Proyectos de análisis de datos y limpieza con Python y SQL.

**Análisis de Taxis NYC (2005)**

Descripción: Procesamiento y limpieza de 100k registros de viajes en Nueva York para identificar patrones de rentabilidad y errores de sistema.

Desafíos superados:

ETL: Limpieza de datos en bruto y cálculo de duraciones en Python.

SQL Data Cleaning: Identificación de errores de GPS donde se registraban velocidades de hasta 3,900 MPH.

Segmentación: Clasificación de viajes por distancia para entender la distribución de propinas.

Herramientas usadas: Python (Pandas, Seaborn), MySQL Workbench.

**Proyecto Zuber: Análisis de Viajes en Chicago**

Descripción: > Este proyecto analiza las pautas de los pasajeros de la empresa Zuber en Chicago. El objetivo principal fue comprender las preferencias de los clientes y el impacto de factores externos, como el clima, en la duración de los viajes.

Desafíos y Habilidades Aplicadas:

Extracción de Datos Web (Scraping): Se obtuvieron datos meteorológicos de un sitio externo para correlacionarlos con los registros de viajes.

Análisis SQL Avanzado: Se realizaron uniones (JOIN) complejas para vincular barrios (barrios como Loop y O'Hare) con registros de clima y duración de trayectos.

Prueba de Hipótesis Estadística: Utilicé Python para realizar un test de hipótesis sobre si la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia durante los días lluviosos.

Hallazgos Clave:

Impacto del Clima: Se confirmó mediante un análisis estadístico que las condiciones meteorológicas afectan significativamente la duración de los viajes, permitiendo a Zuber optimizar sus tarifas dinámicas.

Zonas de Alta Demanda: Identifiqué los barrios con mayor frecuencia de viajes, lo que ayuda en la redistribución de la flota de conductores.

Stack Tecnológico:

Lenguajes: Python (Pandas, Scipy para tests estadísticos).

Base de Datos: SQL (PostgreSQL/MySQL).

Herramientas: Jupyter Notebooks, Visual Studio Code.
