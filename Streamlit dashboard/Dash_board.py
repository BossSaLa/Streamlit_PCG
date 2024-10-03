import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
import datetime

st.set_page_config(
    page_title="NIR COATER DASHBOARD",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
df_form_SQL = pd.read_csv('datafromSQL.csv')

with st.sidebar:
    st.title('🏂 NIR COATER DASHBOARD')
    
    Formular_list = list(df_form_SQL.FORMULA_CODE.unique())[::-1]
    
    selected_Formular = st.selectbox('Select a formular', Formular_list, index=len(Formular_list)-1)
    df_selected_formular = df_form_SQL[df_form_SQL.FORMULA_CODE == selected_Formular]
    df_selected_year_sorted = df_selected_formular.sort_values(by="START_DATETIME", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

    Value_pre_list = ["MOISTURE","CP","FAT","FIBER","DENSITY"]
    Value_list = st.selectbox('Select a Value', Value_pre_list, index=len(Value_pre_list)-1)

    selected_Value = st.selectbox('Select a formular', Formular_list, index=len(Formular_list)-1)

# def make_chart():
    
#     df_form_SQL['START_DATETIME'] = pd.to_datetime(df_form_SQL['START_DATETIME'])

#     date_selector = st.date_input('Select a date', value=df_form_SQL['START_DATETIME'].min())
    
#     st.line_chart(pd.DataFrame(np., columns=["a", "b", "c"]))


#     # Filter data by selected date
#     df_filtered = df_form_SQL[df_form_SQL['START_DATETIME'].dt.date == date_selector]

#     # Create a month selector
#     month_selector = st.selectbox('Select a month', df_filtered['START_DATETIME'].dt.month.unique())

#     # Filter data by selected month
#     df_monthly = df_filtered[df_filtered['START_DATETIME'].dt.month == month_selector]

#     # Create a line chart
#     chart = alt.Chart(df_monthly).mark_line().encode(
#         x='START_DATETIME',
#         # y='column1'  # replace with your actual column name
#     )

def make_chart():
    df_form_SQL['START_DATETIME'] = pd.to_datetime(df_form_SQL['START_DATETIME'])
    
    # Filter data by selected formula
    df_formula = df_form_SQL[df_form_SQL.FORMULA_CODE == selected_Formular]
    
    # Filter data by selected date
    date_selector = st.date_input('Select a date', value=df_formula['START_DATETIME'].min())
    df_date = df_formula[df_formula['START_DATETIME'].dt.date == date_selector]
    
    # Create a line chart for FAT
    chart_fat = alt.Chart(df_date).mark_line().encode(
        x='START_DATETIME',
        y='FAT'  # assuming FAT is the column name for Fat Acid Transesterification data
    ).properties(
        title=f"FAT for Formula: {selected_Formular} on {date_selector}"
    )
    
    st.altair_chart(chart_fat, use_container_width=True)

    
    print("Chart")

make_chart()

# st.rerun()