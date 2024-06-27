<<<<<<< HEAD:app.py
import dash
import dash_bootstrap_components as dbc

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", dbc.themes.LUX]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
# FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"


app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server
=======
import dash
import dash_bootstrap_components as dbc

estilos = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    dbc.themes.LUX,
]
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

app.config["suppress_callback_exceptions"] = True
app.scripts.config.serve_locally = True

if __name__ == "__main__":
    app.run_server(debug=True)
    # server = app.server
>>>>>>> 67fc00654a305bd6d5ce595f76249a36d8ed6de5:Asimov_Associates/app.py
