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
plt.figure(figsize=(10,6))
sns.barplot(data=tabla_fuente, x="fuente", y="cantidad_registros", palette="viridis")

plt.title("Cantidad de registros por fuente de datos")
plt.xlabel("Fuente")
plt.ylabel("Número de registros")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data_raw/grafico_conteo_fuentes.png", dpi=300)
plt.show()

print("\n✔ Gráfico guardado en data_raw/grafico_conteo_fuentes.png")

# ---------------------------------------------------------
# 5. Gráfico adicional: proporción de registros (pie chart)
# ---------------------------------------------------------
plt.figure(figsize=(8,8))
plt.pie(
    tabla_fuente["cantidad_registros"],
    labels=tabla_fuente["fuente"],
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("viridis", len(tabla_fuente))
)

plt.title("Proporción de registros por fuente")
plt.tight_layout()

plt.savefig("data_raw/grafico_proporcion_fuentes.png", dpi=300)
plt.show()

print("✔ Gráfico de proporciones guardado en data_raw/grafico_proporcion_fuentes.png")
