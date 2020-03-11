# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:49:44 2020

@author: Syamanthaka
"""
import dash
import dash_bootstrap_components as dbc


server = index.server
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(__name__, server=server)
app.config.suppress_callback_exceptions = True
