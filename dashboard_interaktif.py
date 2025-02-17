import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import base64
import io

# Membuat aplikasi Dash dengan Bootstrap
theme = "plotly_dark"  # Tema Dark Mode yang cocok untuk Gen Z
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Placeholder Data Kosong
DEFAULT_DF = pd.DataFrame(columns=["Produk", "Kategori", "Penjualan", "Pendapatan"])

# Layout Dashboard dengan sentuhan warna neon pastel
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dashboard Penjualan", className="text-center text-warning mt-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Upload(
            id='upload-data',
            children=dbc.Button('Upload File Excel', color="primary", className="mt-2"),
            multiple=False
        ), width=4),
        dbc.Col(dcc.Dropdown(id="kategori-dropdown", clearable=False, className="mt-2"), width=8)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="grafik-penjualan"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id="tabel-produk",
            columns=[
                {"name": "Produk", "id": "Produk"},
                {"name": "Kategori", "id": "Kategori"},
                {"name": "Penjualan", "id": "Penjualan"},
                {"name": "Pendapatan", "id": "Pendapatan"}
            ],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center", "backgroundColor": "#121212", "color": "#FAD02E"}
        ), width=12)
    ])
], fluid=True)

# Callback untuk memuat data dari file Excel
def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_excel(io.BytesIO(decoded))
    return df

@app.callback(
    [Output("kategori-dropdown", "options"),
     Output("kategori-dropdown", "value"),
     Output("tabel-produk", "data"),
     Output("grafik-penjualan", "figure")],
     [Input("upload-data", "contents"), Input("kategori-dropdown", "value")]
)
def update_dashboard(contents, selected_category):
    local_df = DEFAULT_DF.copy()

    if contents:
        local_df = parse_contents(contents)

    if local_df.empty or "Kategori" not in local_df.columns or local_df["Kategori"].nunique() == 0:
        return [], None, [], px.bar(title="Tidak ada data tersedia", template=theme)
    
    kategori_options = [{"label": k, "value": k} for k in local_df["Kategori"].unique()]
    if selected_category not in local_df["Kategori"].unique():
        selected_category = local_df["Kategori"].unique()[0]

    filtered_df = local_df[local_df["Kategori"] == selected_category]

    if filtered_df.empty:
        fig = px.bar(title="Tidak ada data untuk kategori ini", template=theme)
    else:
        fig = px.bar(
            filtered_df, x="Produk", y="Penjualan", text="Penjualan",
            title=f"Penjualan Produk ({selected_category})", color="Produk",
            template=theme, color_discrete_sequence=["#FF6F61", "#1E90FF", "#32CD32", "#FAD02E", "#6A0572"]
        )
        fig.update_traces(textposition="outside")

    return kategori_options, selected_category, filtered_df.to_dict("records"), fig

# Menjalankan aplikasi
if __name__ == "__main__":
    app.run_server(debug=True)
