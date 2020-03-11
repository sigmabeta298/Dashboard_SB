import os
from random import randint


import dash
import dash_html_components as html
import layouts as lyt


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'

app = dash.Dash(__name__)
server=app.server
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))


# Put your Dash code here
app.layout = html.Div([  
    lyt.main_page
])


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=False)
