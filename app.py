# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
from plotly.express import line
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame

df = pd.read_csv('data/processed_data.csv')




print(df.head())

fig = line(df, x="date", y="sales", title = "Pink Morsel Sales")

app.layout = html.Div(children=[
    html.H1(children='Sales Pink Morsel'),

    html.Div(children='''
        Comparing sales data
    '''),

    dcc.Graph(
        id='pink-morsel-sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
