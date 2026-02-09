import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datos que exportaste de SQL
df = pd.read_csv('viajes_limpios.csv')

# 2. Configurar el estilo del gráfico
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# 3. Crear el histograma de Duración (limitando a viajes de menos de 1 hora para mejor vista)
sns.histplot(df['duration_seconds'] / 60, bins=30, kde=True, color='skyblue')

# 4. Personalización del reporte
plt.title('Distribución de la Duración de los Viajes (Datos Limpios)', fontsize=15)
plt.xlabel('Duración (Minutos)', fontsize=12)
plt.ylabel('Cantidad de Viajes', fontsize=12)

# 5. Guardar el gráfico como imagen para tu reporte
plt.savefig('reporte_distribucion.png')
print("✅ Histograma generado y guardado como 'reporte_distribucion.png'")
plt.show()