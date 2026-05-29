# Proyecto: 5 Fuentes y Obtención de Datos

Este repositorio contiene el desarrollo del proyecto de análisis y visualización de fuentes de datos económicas y sociales en Sudamérica.  
El objetivo es integrar y documentar indicadores provenientes de organismos internacionales y regionales, garantizando la reproducibilidad del proceso.

## 📂 Estructura del repositorio
data_raw/  → Archivos de datos y gráficos generados

             desde los archivos resultado de las Api o web scraping hasta la generación de archivos resumen
             la subcarpeta \itbaro, es donde se descomprime el archivo latinobarometro_2024.zip
             
bcb.py     → Información del Banco Central de Brasil 

bcc.py     → Información del Banco Central de Colombia

fmi.py     → Información del Fondo monetario internacional

lbr.py     → Descargar el archivo Zip y extraer los archivos del Latinobarómetro

wb.py      → Información del Banco Mundial

clean_union.py   → Limpieza, estrucuturación y unificación de datasets en uno solo

resumen.py       → Generación de resumen estadístico y gráficos

README.md        → Presentación del proyecto
