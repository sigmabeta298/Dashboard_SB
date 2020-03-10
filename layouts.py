# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:46:23 2020

@author: 320054667
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_n_graphs as grf

page_title = dbc.Row([dbc.Col(html.H2("Syamanthaka Balakrishnan", style={'text-align' : 'center'}), width=12)])

#-----------------------------------------------------------        
career_timeline = dbc.Card(children=[
    dbc.CardHeader(html.H5("Career Timeline")),
    dbc.CardBody([
        dcc.Graph(id="career_tl", 
            figure = grf.career_tl
        )  
    ])
])
#-----------------------------------------------------------
        
row1_cards = dbc.Row([dbc.Col(career_timeline, width=12)], no_gutters=True)

#-----------------------------------------------------------        
#skills_cyto = dbc.Card(children=[
#    dbc.CardHeader(html.H5("Technical Skills")),
#    dbc.CardBody([
##        dcc.Graph(id="skills_cyt", 
##            figure = html.Div([grf.skills_cyt])
##        )  
#          html.Div([grf.skills_cyt])
#    ])
#])
skills_cyto = html.Div([grf.skills_cyt])
#-----------------------------------------------------------
row2_cards = dbc.Row([dbc.Col(skills_cyto, width=12)], no_gutters=True)

tab1_content = dbc.Container([
      row2_cards,
      row1_cards
#      row3_cards,
#      row5_cards
], fluid=True)

tabs = dbc.Tabs([
     dbc.Tab(tab1_content, label="Home"),
#     dbc.Tab(erl.tab2_content, label="Error Analytics"),
#     dbc.Tab(prl.prot_tab_content, label="Protocols")
])

main_page = dbc.Container([
      page_title,
      tabs
], fluid=True)