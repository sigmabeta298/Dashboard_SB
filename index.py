# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:42:41 2020

@author: 320054667
"""

import dash_html_components as html
import layouts as lyt


from app import app

server = index.server
server.secret_key = os.environ.get('secret_key', 'secret')
app.layout = html.Div([
    
    lyt.main_page
])


app.config.suppress_callback_exceptions = True
if __name__ == '__main__':
    app.run_server(debug=False)
    #app.run_server(host= '0.0.0.0',debug=False)
