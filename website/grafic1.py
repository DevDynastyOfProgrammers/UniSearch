import pandas as pd
import plotly.graph_objects as go

def PlotPie(pars=None):
    # Чтение базы данных
    df = pd.read_csv('web-uni/universitetiFINAL.csv')

    # место для фильтра

    # Преобразование данных в числовой формат
    df['Budget places (total)'] = pd.to_numeric(df['Budget places (total)'], errors='coerce')
    df['Paid places'] = pd.to_numeric(df['Paid places'], errors='coerce')

    # Метки и значения
    labels = ['Бюджетные места', 'Платные места']
    values = [df['Budget places (total)'].sum(), df['Paid places'].sum()]

    # Создание фигуры
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title_text="Соотношение бюджетных и платных мест")

    # Сохранение графика в формате div
    pie_chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return pie_chart_html

if __name__ == '__main__':
    PlotPie(None)
