from dash import Dash, html, dcc

 

import plotly.express as px

import pandas as pd

# Sample data

x_values = df['employee active'] 
x_values = df['emplyee inactive']
y_values = df['employee packing']

data = {'X':[1,2,3,4,5],

        'Y':[10,11,8,15,12],

        'Category' : ['A', 'B','A', 'B','A']

    }

 

df = pd.DataFrame(data)

 

app= Dash(__name__)

 

fig = px.scatter(df, x='X', y = 'Y',color='Category')#, title='Simple scatter plot')

#fig = px.line(df, x='X', y = 'Y', title='Simple Line plot')

 

# Adds legend

fig.update_layout(legend_title_text = 'Legend')

 

 

# Add lables for x and y axes

 

fig.update_xaxes(title_text = 'x-Axis Lablel')

fig.update_yaxes(title_text = 'y-Axis Lablel')

 

# Change Size

# fig.update_layout(

#     width = 800,

#     height = 400

# )

 

app.layout = html.Div(children=[

    html.H1(children = "This is my headline"),

    dcc.Graph(

        id='scatter-plot',

        figure = fig,

        style ={'width': '50%', 'height': ' 50%',}

    ),

    dcc.Graph(

        id='another-plot',

        figure = px.line(df, x='X', y='Y', title="Simple Line Plot"),

        style = {'width': '50%', 'height': '50%'}

    ),

    dcc.Graph(

        id='another-one',

        figure = px.histogram(df, x='X', y='Y', title="Histogram graph"),

        style ={'width': '50%', 'height': ' 50%'}

 

    )

],style={'display': 'flex'}) # Lägg denna Style på Div-containern

 

app.run(debug=True)

# fig.show()