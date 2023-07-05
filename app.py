import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Исследование по чаевым

Сделано Ивановой Викаськой

""")
# Загрузка данных
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

# Отображение данных
st.write(tips)

# Гистограмма столбца 'total_bill'
st.subheader('Гистограмма суммы счета')
fig, ax = plt.subplots()
ax.hist(tips['total_bill'], bins=10)
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')
ax.set_title('Histogram: Total Bill')
st.pyplot(fig)

# Scatter plot: Total Bill vs Tip
st.subheader('График зависимости суммы чаевых от суммы счета')
fig, ax = plt.subplots()
ax.scatter(tips['total_bill'], tips['tip'])
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_title('Scatter Plot: Total Bill vs Tip')
st.pyplot(fig)

# Scatter plot: Total Bill, Tip, and Size
st.subheader('График зависимости суммы чаевых от размера компании')
fig, ax = plt.subplots()
scatter = ax.scatter(tips['total_bill'], tips['tip'], c=tips['size'], cmap='bwr')
ax.colorbar(scatter, label='Size')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_title('Scatter Plot: Total Bill, Tip, and Size')
st.pyplot(fig)

# Scatter plot: Tip vs Day
st.subheader('График зависимости суммы чаевых от дня')
sex_mapping = {'Female': 0, 'Male': 1}
tips['sex_encoded'] = tips['sex'].map(sex_mapping)
fig, ax = plt.subplots()
scatter = ax.scatter(tips['tip'], tips['day'], c=tips['sex_encoded'], cmap='bwr')
ax.colorbar(scatter, label='Sex')
ax.set_xlabel('Tip')
ax.set_ylabel('Day')
ax.set_title('Scatter Plot: Tip vs Day')
ax.set_xticks(rotation=45, ha='right')
st.pyplot(fig)

# Bar plot: Выручка по дням недели
st.subheader('Выручка по дням недели')
fig, ax = plt.subplots()
ax.bar(tips['day'], tips['total_bill'], color='c')
ax.set_xlabel('Дни недели')
ax.set_ylabel('Доход')
ax.set_title('Выручка')
ax.set_xticks(rotation=45)
st.pyplot(fig)

# Box plot: Total Bill by Day and Time
st.subheader('Box Plot: Total Bill by Day and Time')
grouped_data = tips.groupby(['day', 'time'])['total_bill'].sum().reset_index()
fig, ax = plt.subplots()
ax.boxplot([grouped_data[grouped_data['time'] == 'Lunch']['total_bill'],
             grouped_data[grouped_data['time'] == 'Dinner']['total_bill']],
            labels=['Lunch', 'Dinner'])
ax.set_xlabel('Time')
ax.set_ylabel('Total Bill')
ax.set_title('Box Plot: Total Bill by Day and Time')
st.pyplot(fig)

# Histograms: Lunch Tips and Dinner Tips
st.subheader('Гистограммы чаевых на обед и ужин')
lunch_tips = tips[tips['time'] == 'Lunch']['tip']
dinner_tips = tips[tips['time'] == 'Dinner']['tip']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
ax1.hist(lunch_tips, bins=10, color='blue', alpha=0.7)
ax1.set_xlabel('Tip')
ax1.set_ylabel('Frequency')
ax1.set_title('Lunch Tips')
ax2.hist(dinner_tips, bins=10, color='green', alpha=0.7)
ax2.set_xlabel('Tip')
ax2.set_ylabel('Frequency')
ax2.set_title('Dinner Tips')
plt.tight_layout()
st.pyplot(fig)

# Scatter plots: Male and Female
st.subheader('Scatter Plots: Male and Female')
male_smokers = tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'Yes')]
female_smokers = tips[(tips['sex'] == 'Female') & (tips['smoker'] == 'Yes')]
male_nonsmokers = tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'No')]
female_nonsmokers = tips[(tips['sex'] == 'Female') & (tips['smoker'] == 'No')]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
ax1.scatter(male_smokers['total_bill'], male_smokers['tip'], c='blue', label='Male Smokers')
ax1.scatter(male_nonsmokers['total_bill'], male_nonsmokers['tip'], c='green', label='Male Non-smokers')
ax1.set_xlabel('Total Bill')
ax1.set_ylabel('Tip')
ax1.set_title('Scatterplot: Male')
ax1.legend()
ax2.scatter(female_smokers['total_bill'], female_smokers['tip'], c='red', label='Female Smokers')
ax2.scatter(female_nonsmokers['total_bill'], female_nonsmokers['tip'], c='purple', label='Female Non-smokers')
ax2.set_xlabel('Total Bill')
ax2.set_ylabel('Tip')
ax2.set_title('Scatterplot: Female')
ax2.legend()
plt.tight_layout()
st.pyplot(fig)
