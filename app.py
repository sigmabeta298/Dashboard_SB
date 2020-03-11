import dash_html_components as html
import layouts as lyt

import callbacks

server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    
    lyt.main_page
])


app.config.suppress_callback_exceptions = True
if __name__ == '__main__':
    app.run_server(debug=False)
