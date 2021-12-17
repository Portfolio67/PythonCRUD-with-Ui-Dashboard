from jupyter_plotly_dash import JupyterDash
import dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table as dt
import dash_table
from dash.dependencies import Input, Output
import base64
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from module5CRUD import AnimalShelter

# Data Manipulation / Model
username = "aacuser"
password = "Dog"
shelter = AnimalShelter(username, password)

# class read method must support return of cursor object and accept projection json input
df = pd.DataFrame.from_records(shelter.read({}))

# Dashboard Layout / View
app = JupyterDash('SimpleExample')

#Grazioso Salvare’s logo                              
image_filename = 'Grazioso Salvare Logo.png' 
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(html.B(html.H1('Grazioso Salvare - Animals in Shelters'))),
    html.Center(html.B(html.H5('Made by Shane Flaten'))),
    html.Hr(),
    # customer image 
    html.A([html.Img(id='customer-image',src='data:image/png;base64,{}'.format(encoded_image.decode()),alt='customer image'),
           ], href='https://www.snhu.edu'),
    
    #Radio Buttons
    dcc.RadioItems(
        id='filter-type', 
        persistence=True,
        persistence_type="memory", # not sure if this works with this code below, but no errors
        options = [
            {'label' : 'Water Rescue', 'value' : 'WR'},
            {'label' : 'Mountain or Wilderness Rescue', 'value' : 'MWR'},
            {'label' : 'Disaster Rescue or Tracking Rescue', 'value' : 'DR'},
            {'label' : 'Reset', 'value' : 'RS'},
        ],
        value = 'WR',
        labelStyle = {'display': 'inline-block'}
    ),
    dash_table.DataTable(
        id='datatable-id',
         columns=[
             {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
         ],
         data=df.to_dict('records'),
        #features for your interactive data table to make it user-friendly for your client
        editable=False,
        #suppress_callback_exceptions=True
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable=True,
        row_selectable=True,
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 30,
        #page_size= 300,

    ),
    html.Br(),
     html.Hr(),
     html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
    ])
])

# Interaction Between Components / Controller
@app.callback([Output('datatable-id','data'),
               Output('datatable-id','columns')],
              [Input('filter-type', 'value')])
def update_dashboard(filter_type): #loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
    if filter_type == 'WR':
        #pandas uses python operators,  the & did not work,  The + brought a smaller list that the or operator, weird?... https://www.w3schools.com/python/python_operators.asp
        # df is a pandas dataframe type. retreived from the mongo database
        #dffff is a pandas datafram type -> dfff..  and so on filtering each dataframes 
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram for strings.  iloc is for ints https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        dfff = dffff.loc[(dffff['breed'] == 'Labrador Retriever Mix') | (dffff['breed'] == 'Labrador Retriever') | (dffff['breed'] == 'Newfoundland Mix') | (dffff['breed'] == 'Newfoundland') | (dffff['breed'] == 'Chesapeake Bay Retriever')]
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Female')] 
        df = dff.query('26 <= age_upon_outcome_in_weeks <= 156')       #df.query('A > B') https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
        
    elif filter_type == 'MWR':
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram
        dfff = dffff.loc[(dffff['breed'] == 'German Shepherd') | (dffff['breed'] == 'Alaskan Malamute') | (dffff['breed'] == 'Old English Sheepdog') | (dffff['breed'] == 'Siberian Husky')| (dffff['breed'] == 'Rottweiler')]
       
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Male')]
        df = dff.query('26 <= age_upon_outcome_in_weeks <= 156')  
        
    elif filter_type == 'DR':
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram
        dfff = dffff.loc[(dffff['breed'] == 'Doberman Pinscher') | (dffff['breed'] == 'German Shepherd') | (dffff['breed'] == 'Golden Retriever') | (dffff['breed'] == 'Rottweiler')| (dffff['breed'] == 'Doberman Pinscher')]
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Male')]
        df = dff.query('20 <= age_upon_outcome_in_weeks <= 300')  
    elif filter_type == 'RS':
        df = pd.DataFrame.from_records(shelter.read({}))
            
    columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns]
    data=df.to_dict('records')
    return (data,columns)

#This callback will highlight a row on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_viewport_data")])
def update_graph(viewData):
    sff = pd.DataFrame.from_dict(viewData)
    return [
       dcc.Graph( # you must return a dash core component type, It  has a method Graph() 
           #####LINE####
           #figure = px.line(sff, x='breed', y= 'age_upon_outcome_in_weeks') #px is , and uses matlib,  it counts the frequency automatically
           #figure = px.scatter_matrix(sff, dimensions  = ['age_upon_outcome_in_weeks','sex_upon_outcome'], color = 'breed')
           figure = px.scatter_matrix(sff, dimensions  = ['age_upon_outcome_in_weeks'], color = 'breed')
       
       )    
    ]

@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_viewport_data")])
def update_map(viewData):
    dff = pd.DataFrame.from_dict(viewData)
    # Austin TX is at [30.75, -97.48]
    latitude = dff.iloc[0,13]
    longitude = dff.iloc[0,14]
    return[
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[dff.iloc[0,13],dff.iloc[0,14]], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            dl.Marker(position=[dff.iloc[0,13],dff.iloc[0,14]], children=[
                dl.Tooltip(dff.iloc[0,4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iloc[0,9]), # row, column
                    html.P(dff.iloc[0,13]), 
                    html.P(dff.iloc[0,14]) 
                    
                    
                ])
            ])
        ])
    ]
app
