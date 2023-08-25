import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd


df = pd.read_excel("data/data.xlsx")


columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "cellRenderer": "StockLink",
        'filter':True,
    },
    {
        "headerName": "Company",
        "field": "company",
        "editable": True,
        "cellRenderer": "Images",
        'filter':True,
    },
    {
        "headerName": "Shares",
        "field": "quantity",
        "editable": True,
        "cellRenderer": "NumberStyle",
        'filter':True,
    }
]


grid = dag.AgGrid(
    dangerously_allow_code=True,
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef={"editable": False},
)


app = Dash(__name__)

app.layout = html.Div(
    [grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run(debug=True)
