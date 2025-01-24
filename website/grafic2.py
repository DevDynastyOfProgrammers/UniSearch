import pandas as pd
import plotly.express as px
import os

def PlotHistogram():
    # Чтение данных из CSV файла
    df = pd.read_csv('web-uni/universitetiFINAL.csv')

    # Преобразование строковых значений в NaN и перевод в числовой формат
    df['Teachers with scientists step(%)'] = pd.to_numeric(df['Teachers with scientists step(%)'], errors='coerce')

    # Построение гистограммы
    fig = px.histogram(df, x="Teachers with scientists step(%)", nbins=20,
                    title="Распределение процента преподавателей с учеными степенями",
                    labels={"Teachers with scientists step(%)": "Процент преподавателей с учеными степенями"})

    # Обновление осей
    fig.update_xaxes(title_text="Процент преподавателей с учеными степенями")
    fig.update_yaxes(title_text="Частота")

    # Получаем HTML-код графика
    histogram_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return histogram_html