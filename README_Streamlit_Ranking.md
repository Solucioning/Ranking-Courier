
# App de Consulta de Ranking para Couriers 🚴‍♂️📊

Esta es una app creada con [Streamlit](https://streamlit.io) que permite a los couriers consultar sus métricas de desempeño semanal introduciendo su ID.

## 📦 Archivos necesarios

- `app_courier_ranking.py` — el script principal de la aplicación Streamlit
- `Ranking_Couriers_Semanal.xlsx` — archivo con los datos de ranking, incluyendo:
  - Semana, Ciudad, Vehicle, IDCourier
  - Eficiencia, CDT, Speed, No show, CAPU, Reassignament
  - Score_total, Ranking_posicion, Incentivo_semanal, Reto_mensual

## 🚀 ¿Cómo ejecutarla localmente?

```bash
pip install streamlit pandas openpyxl
streamlit run app_courier_ranking.py
```

## 🌐 ¿Cómo publicarla online?

1. Sube estos archivos a un nuevo repositorio en GitHub.
2. Entra a [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Conecta tu cuenta de GitHub y selecciona el repositorio.
4. Selecciona `app_courier_ranking.py` como archivo principal.
5. Haz clic en "Deploy" y comparte el enlace generado.

## 📋 Vista de ejemplo

![screenshot](https://placehold.co/600x400?text=Preview+Ranking+App)

---

**Creado por**: [Tu nombre o equipo]  
**Contacto**: carolina.artiel@solucioning.net
