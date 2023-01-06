import pandas as pd
import streamlit as st
import base64
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Tracker',
                   layout='wide')
st.header('Tracker')
excel_file = 'REPORT SCHEDULING.xlsx'
sheet_name = 'REPORT'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:AM',
                   header=0
                   )

territory = df['Service Territory'].unique().tolist()
project = df['Project'].unique().tolist()

st.sidebar.header('Filters')
custom_filter = st.sidebar.text_input('Customer filter:',value='')
serial_filter = st.sidebar.text_input('Serial number:')
project_selection = st.sidebar.text_input('Project:',value='SY')
territory_selection = st.sidebar.multiselect('Service Territory:',
                                             territory,
                                             default=territory)

mask = df['Account Name'].str.contains(custom_filter,case=False, na=False) & df['Serial Number'].str.contains(serial_filter,case=False, na=False) & df['Project'].str.contains(project_selection,case=False, na=True) & df['Service Territory'].isin(territory_selection)

print(f'{mask}')
df[mask]





### image = Image.open('')
### st.image(image,
###          caption='by Pagno',
###          use_column_width=True)

