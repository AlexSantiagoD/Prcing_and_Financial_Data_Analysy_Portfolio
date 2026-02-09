import pandas as pd

# CONFIGURACIÓN: Escribe el nombre exacto de tu archivo .parquet
nombre_archivo = 'yellow_tripdata_2025-01.parquet' 

def procesar_fase_1(archivo):
    print(f"--- Iniciando Fase 1 (Parquet): ETL para {archivo} ---")
    
    try:
        # 1. Lectura del archivo Parquet
        df_completo = pd.read_parquet(archivo)
        
        # Tomamos una muestra de las primeras 100,000 filas
        df = df_completo.head(100000).copy()
        print("✅ Archivo Parquet cargado exitosamente.")
        
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return

    # 2. Análisis y Limpieza
    # Asegúrate de que estos nombres existan en tu archivo
    col_inicio = 'tpep_pickup_datetime'
    col_fin = 'tpep_dropoff_datetime'
    
    # Convertimos a formato fecha
    df[col_inicio] = pd.to_datetime(df[col_inicio])
    df[col_fin] = pd.to_datetime(df[col_fin])

    # Filtramos datos coherentes (distancia y montos mayores a cero)
    # [cite_start]Esto es similar a lo requerido en el análisis de Zuber [cite: 10, 11]
    df_filtrado = df[(df['trip_distance'] > 0) & (df['total_amount'] > 0)].copy()

    # 3. Cálculo de duración
    df_filtrado['duration_seconds'] = (df_filtrado[col_fin] - df_filtrado[col_inicio]).dt.total_seconds()

    # --- CAMBIO IMPORTANTE AQUÍ ---
    # 4. Seleccionar SOLO las columnas que coinciden con tu tabla de MySQL
    cols_to_keep = [
        'tpep_pickup_datetime', 
        'tpep_dropoff_datetime', 
        'trip_distance', 
        'fare_amount', 
        'tip_amount', 
        'total_amount', 
        'duration_seconds'
    ]
    
    # Creamos un nuevo dataframe limpio solo con esas columnas
    df_final = df_filtrado[cols_to_keep].copy()

    # 5. Exportar a CSV
    archivo_salida = 'nyc_taxi_listo_para_sql.csv'
    df_final.to_csv(archivo_salida, index=False)
    
    print(f"✅ Archivo '{archivo_salida}' generado sin índices.")
# Esta línea debe ir al ras de la pared (sin espacios al inicio)
procesar_fase_1(nombre_archivo)