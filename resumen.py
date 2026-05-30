import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. Cargar archivo final ya unificado
# ---------------------------------------------------------
df = pd.read_csv("data_raw/union_final.csv")

print("✔ Archivo final cargado correctamente")
print(df.head())

# ---------------------------------------------------------
# 2. Resumen estadístico general
# ---------------------------------------------------------
print("\n================ RESUMEN ESTADÍSTICO ================\n")

# describe() sin datetime_is_numeric
resumen = df.describe(include="all")

print(resumen)

# Guardar resumen en CSV
resumen.to_csv("data_raw/resumen_estadistico.csv", index=True)
print("\n✔ Resumen estadístico guardado en data_raw/resumen_estadistico.csv")

# ---------------------------------------------------------
# 3. Tabla resumen por fuente
# ---------------------------------------------------------
print("\n================ RESUMEN POR FUENTE ================\n")

tabla_fuente = df["fuente"].value_counts().reset_index()
tabla_fuente.columns = ["fuente", "cantidad_registros"]

print(tabla_fuente)

tabla_fuente.to_csv("data_raw/resumen_por_fuente.csv", index=False)
print("\n✔ Tabla por fuente guardada en data_raw/resumen_por_fuente.csv")

# ---------------------------------------------------------
# 4. Gráfico alternativo: barras del tamaño de cada dataset
# ---------------------------------------------------------
# Sort the data by 'cantidad_registros' for better visualization
tabla_fuente_sorted = tabla_fuente.sort_values(by='cantidad_registros', ascending=False)

plt.figure(figsize=(12, 8)) # Increase figure size for better readability
sns.barplot(data=tabla_fuente_sorted, y='fuente', x='cantidad_registros', palette='viridis')
plt.title('Cantidad de Registros por Fuente de Datos')
plt.xlabel('Cantidad de Registros')
plt.ylabel('Fuente de Datos')
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.savefig('data_raw/grafico_conteo_fuentes.png')
plt.close() # Close the figure to free up memory

print('✔ Gráfico de conteo de fuentes guardado en data_raw/grafico_conteo_fuentes.png')

# ---------------------------------------------------------
# 5. Gráfico adicional: proporción de registros (pie chart)
# ---------------------------------------------------------
# Calculate proportions
tabla_fuente['proporcion'] = tabla_fuente['cantidad_registros'] / tabla_fuente['cantidad_registros'].sum()

# Sort by proportion for better visualization
tabla_fuente_proporcion_sorted = tabla_fuente.sort_values(by='proporcion', ascending=False)

plt.figure(figsize=(12, 8)) # Increase figure size
sns.barplot(data=tabla_fuente_proporcion_sorted, y='fuente', x='proporcion', palette='magma')
plt.title('Proporción de Registros por Fuente de Datos')
plt.xlabel('Proporción')
plt.ylabel('Fuente de Datos')
plt.xlim(0, 1) # Set x-axis limit from 0 to 1 for proportions
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x))) # Format as percentage
plt.tight_layout()
plt.savefig('data_raw/grafico_proporcion_fuentes.png')
plt.close()

print('✔ Gráfico de proporciones guardado en data_raw/grafico_proporcion_fuentes.png')
