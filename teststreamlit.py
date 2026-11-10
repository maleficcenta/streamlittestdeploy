import streamlit as st
import pandas as pd
import numpy as np

# Настройка заголовка страницы
st.title("📊 Мое первое тестовое приложение Streamlit")

# Добавление простого текста
st.write("Привет! Это демонстрация базовых возможностей интерфейса Streamlit.")

# Интерактивный элемент: Ввод текста пользователем
user_name = st.text_input("Как вас зовут?", "Гость")
st.write(f"Добро пожаловать, **{user_name}**! 👋")

# Интерактивный элемент: Слайдер
st.header("⚙️ Работа с виджетами")
number = st.slider("Выберите число", min_value=1, max_value=100, value=25)
st.write(f"Вы выбрали число: **{number}**")

# Генерация и отображение данных
st.header("📈 Визуализация данных")

# Создаем случайный датафрейм
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Параметр А', 'Параметр Б', 'Параметр В']
)

# Отображаем таблицу данных
if st.checkbox("Показать сырые данные таблицей"):
    st.subheader("Таблица сгенерированных данных")
    st.dataframe(chart_data)

# Строим интерактивный линейный график
st.subheader("Линейный график")
st.line_chart(chart_data)
