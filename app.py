import os
from random import randint
import dash_html_components as html
import layouts as lyt

import callbacks

server = index.server
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True

app.config.suppress_callback_exceptions = True
if __name__ == '__main__':
    app.run_server(debug=False)
