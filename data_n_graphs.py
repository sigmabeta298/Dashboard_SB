# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:50:14 2020

@author: Syamanthaka
"""
import pandas as pd
import plotly.figure_factory as ff
import dash_cytoscape as cyto
cyto.load_extra_layouts()
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots

#career = pd.read_excel('Skills.xlsx', sheet_name='Career')
df_sheet_map = pd.read_excel('Skills.xlsx', sheet_name=None)

#print(df.head())
## Value for total count of studies

#################################################################################################
#
career = df_sheet_map['Career']
career_tl = ff.create_gantt(career, index_col='Finish', colors=['#333F44', '#93e4c1'], title="", bar_width=0.2, showgrid_x=True, showgrid_y=True)

#elements = {}
pls = df_sheet_map['Programminglanguage']
fmw = df_sheet_map['Frameworks']
db = df_sheet_map['DB']
tls = df_sheet_map['Tools']
dms = df_sheet_map['Domains']

elements = []
def create_child_dict(df, label_col, parent):
   for i, row in df.iterrows():
      tmp_dct = {}
      tmp_dct['id'] = row[label_col].lower()
      tmp_dct['label'] = row[label_col]
      tmp_dct['parent'] = parent
      more_tmp_dct = {}
      more_tmp_dct['data'] = tmp_dct
      elements.append(more_tmp_dct)
   
   return elements

def create_parent_dict(lst):
   for key,val in lst.items():
      dct1 = {}
      dct1['id'] = key
      dct1['label'] = lst[key]
      dct2 = {}
      dct2['data'] = dct1
      elements.append(dct2)
      
   return elements

def create_connects(lst):
   for key, val in lst.items():
      dc1 = {}
      ith_idx = list(lst.keys()).index(key)
      
      if ith_idx + 1 < len(lst.items()):
         new_key = list(lst.keys())[ith_idx + 1]
         dc1['id'] = ith_idx
         dc1['source'] = key
         dc1['target'] = new_key
         dc2 = {}
         dc2['data'] = dc1
         elements.append(dc2)
      
   return elements


elements = create_child_dict(pls, 'Language', 'pls')
#elements = create_child_dict(fmw, 'Names', 'fmw')
elements = create_child_dict(db, 'Name', 'db')
#elements = create_child_dict(tls, 'Tools', 'tls')
#elements = create_child_dict(dms, 'Domains', 'dms')

parent_list = {'pls' : 'ProgLang', 'db': 'DBs'}#, , 'fmw': 'FrameWork''tls' : 'Tools', 'dms': 'Domains'}
elements = create_parent_dict(parent_list)
elements = create_connects(parent_list)

print(elements)

#elements = [
#    {'data': {'id': 'a', 'parent': 'b', 'label': 'a'}},
#    {'data': {'id': 'b', 'label': 'b'}},
#    {'data': {'id': 'c', 'parent': 'b', 'label': 'c'}},
#    {'data': {'id': 'd', 'label' : 'd'}},
#    {'data': {'id': 'e', 'label' : 'e'}},
#    {'data': {'id': 'f', 'parent': 'e', 'label':'f'}},
#    {'data': {'id': 'ad', 'source': 'a', 'target': 'd'}},
#    {'data': {'id': 'eb', 'source': 'e', 'target': 'b'}}
#]
                                                           
skills_cyt = cyto.Cytoscape(
        id='skills_cyto',
        layout={'name': 'random'},
        style={'width': '100%', 'height': '800px'},
        elements=elements
    )                                                   

## Pie chart for distribution of countries
#def generate_country_pie():
#   country_labels = df['Country'].unique()
#   country_vals = df['Country'].value_counts()
#   
#   country_pie = go.Figure(data=[go.Pie(labels=country_labels, values=country_vals)])
#   return(country_pie)
#country_pie = generate_country_pie()
#
#Plotly.plot('graph', [{
#  type: 'bar',
#  y: [0,0,0],
#  x: [1,2,1],
#  orientation: 'h',
#  base: [0,2,5]
#}, {
#  type: 'bar',
#  y: [1,1,1],
#  x: [2,1,2],
#  orientation: 'h',
#  base: [0,3,5]
#}])
