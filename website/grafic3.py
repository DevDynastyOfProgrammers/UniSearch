import pandas as pd
import plotly.express as px
import os

def PlotBar():
    # Чтение базы данных
    df = pd.read_csv('web-uni/universitetiFINAL.csv')

    # Разделение значений в столбце Specialties на отдельные строки
    splitted_specialties = df['Specialties'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)

    # Создание нового DataFrame с отдельными строками для каждой специальности
    new_df = pd.DataFrame({'Specialty': splitted_specialties})

    # Подсчет количества каждой специальности
    counted_specialties = new_df['Specialty'].value_counts()

    # Выбираем топ-10 специальностей
    top_10_specialties = counted_specialties.head(10)

    # Построение диаграммы Plotly для топ-10 специальностей
    fig = px.bar(top_10_specialties, x=top_10_specialties.index, y=top_10_specialties.values,
                title='Топ-10 самых популярных специальностей',
                labels={'x': 'Специальность', 'y': 'Количество'})

    # Сохранение графика в формате div
    bar_chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return bar_chart_html