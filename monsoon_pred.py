import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import dash_table
import plotly.graph_objs as go
import plotly.tools as tls
from dash.dependencies import Input, Output


app = dash.Dash(__name__, static_folder='assets')
app.config['suppress_callback_exceptions']=True
app.scripts.config.serve_locally=True
app.css.config.serve_locally=True


df=pd.read_csv('monsoon_data.csv')
df.columns = ['Set_id', 'View', 'Rank', 'Skip', 'Density', 'Convg', 'Root', 'Rain','Obsv','Year']


def dict_func(x):
    a = {str(i):str(i) for i in range(int(x.min())+10-(int(x.min())%10),int(x.max()),10)}
    a[str(int(x.min()))] = str(int(x.min()))
    a[str(int(x.max()))] = str(int(x.max()))
    return a

app.layout = html.Div([
    html.Link(href='/assets/css_dv.css', rel='stylesheet'),
    html.Link(href='/assets/css_dv2.css', rel='stylesheet'),
    html.Link(href='/assets/css_dv3.css', rel='stylesheet'),
    html.Link(href='/assets/css_dv4.css', rel='stylesheet'),
    html.Link(href='/assets/css_dv5.css', rel='stylesheet'),


    html.Div([
        
        html.H2('Monsoon Rainfall Prediction',
        style = {
            'textAlign':'center',
            'font-family': 'Arial Narrow',
            'font-weight': 'bold',
        },
        className = "row gs-header gs-text-header"
    ),

        html.Div([
            html.H6('X-axis', className = "gs-header gs-text-header padded"),
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                placeholder="Select X-axis",
                value='Set_id'
            )
        ],
        style={'width': '32.33%', 'padding': '12px', 'float': 'none','display': 'inline-block','textAlign': "center", 'font-weight': 'bold','font-family':'Arial Narrow'}),

        html.Div([
            html.H6('Y-axis 1', className = "gs-header gs-text-header padded"),
            dcc.Dropdown(
                id='crossfilter-y1axis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                placeholder="Select Y1-axis",
                value='Rain'
            )
        ], style={'width': '32.33%','padding': '12px', 'float': 'none','display': 'inline-block','textAlign': "center",'font-weight': 'bold','font-family':'Arial Narrow'}),

        html.Div([
            html.H6('Y-axis 2', className = "gs-header gs-text-header padded"),
            dcc.Dropdown(
                id='crossfilter-y2axis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                placeholder="Select Y2-axis",
                value='Obsv'
            )
        ], style={'width': '32.33%', 'padding': '12px','float': 'none', 'display': 'inline-block','textAlign': "center",'font-weight': 'bold','font-family':'Arial Narrow'}),

    ], style={
        'border': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 10px'
    }),
    html.Div([
            html.H6('Year',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-year--slider1',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=[min(df['Year']),max(df['Year'])],
        marks={str(year): str(year) for year in df['Year'].unique()}
    )
        ,
        html.Br([])
        ,
        html.Br([])
        ,
        html.Div([
            html.H6('View',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
                id='crossfilter-view--slider1',
                min=df['View'].min(),
                max=df['View'].max(),
                value=[min(df['View']),max(df['View'])],
                marks={str(year): str(year) for year in df['View'].unique()}
            )
        ,
        html.Br([])
        ,
            html.H6('Rank',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-rank--slider2',
        min=df['Rank'].min(),
        max=df['Rank'].max(),
        value=[min(df['Rank']),max(df['Rank'])],
        marks={str(year): str(year) for year in df['Rank'].unique()}
    )
        ,
        html.Br([])
        ,
            html.H6('Skip',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-skip--slider3',
        min=df['Skip'].min(),
        max=df['Skip'].max(),
        value=[min(df['Skip']),max(df['Skip'])],
        marks={str(year): str(year) for year in df['Skip'].unique()}
    )
        ,
        html.Br([])
        ,
            html.H6('Density',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-density--slider4',
        min=df['Density'].min(),
        max=df['Density'].max(),
        value=[min(df['Density']),max(df['Density'])],
        marks=dict_func(df['Density'])
    )
        ,
        html.Br([])
        ,
            html.H6('Convg',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-convg--slider5',
        min=df['Convg'].min(),
        max=df['Convg'].max(),
        value=[min(df['Convg']),max(df['Convg'])],
        marks=dict_func(df['Convg'])
    )
        ,
        html.Br([])
        ,
            html.H6('Root',className = "gs-header gs-table-header padded"),
            dcc.RangeSlider(
        id='crossfilter-root--slider6',
        min=df['Root'].min(),
        max=df['Root'].max(),
        value=[min(df['Root']),max(df['Root'])],
        marks=dict_func(df['Root'])
    )
        ], className = "four columns" ,style={'width': '30.33%','padding': '10px 10px 10px 10px', 'float': 'none','display': 'inline-block','textAlign': "center"}),
    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter'
        )
    ], className = "eight columns",style={'padding':'5px','border': 'lightgrey solid'}), 
    html.Br([]) 
    ,  
    html.Br([]) 
    ,
    html.Div(id='output-container-range-slider1',
    style={
        'color': '#008080',
        'font-family': 'Arial Narrow',
        'font-size':'20px',
        'font-weight': 'bold',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '0px 0px 0px 0px',
        }),
    ], className = "row ",style={
        'border': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 50px 10px 20px',
        'textAlign': "center"
    }),
    html.Div([
        html.H5('Selected data',style={'font-weight': 'bold','font-family':'Arial Narrow'}),
        html.Div([dcc.Graph(id='graphs_2')])],
        style={'border': 'thin lightgrey solid'}
        ),
    html.Div([
        html.Div([html.H5(id='selPoint',style={'font-weight': 'bold','font-family':'Arial Narrow'})]),
        html.Div([dcc.Graph(id='graphs')])],
        style={'border': 'thin lightgrey solid'}
        ),
    html.Div([
        html.H5('Data table',style={'font-weight': 'bold','font-family':'Arial Narrow'}),
        html.Div(id='selected-data')],
        style={'border': 'thin lightgrey solid'}
        )
    
])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-y1axis-column', 'value'),
     dash.dependencies.Input('crossfilter-y2axis-column', 'value'),
     dash.dependencies.Input('crossfilter-year--slider1', 'value'),
     dash.dependencies.Input('crossfilter-view--slider1', 'value'),
     dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
     dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
     dash.dependencies.Input('crossfilter-density--slider4', 'value'),
     dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
     dash.dependencies.Input('crossfilter-root--slider6', 'value'),

    ])
def update_graph(xaxis_column_name, y1axis_column_name,y2axis_column_name,slider0,slider1,slider2,slider3,slider4,slider5,slider6):
    g_cols = ['Year','View', 'Rank', 'Skip', 'Density', 'Convg', 'Root']
    input_value = [slider0,slider1, slider2, slider3, slider4, slider5, slider6]
    dff = df.copy()
    for i, col_range in enumerate(input_value):
        dff = dff[col_range[0]<=dff[g_cols[i]]][dff[g_cols[i]]<=col_range[1]]
    Predicted = go.Scattergl(
            x=list(dff[xaxis_column_name]),
            y=list(dff[y1axis_column_name]),
            customdata=list(dff[xaxis_column_name]),            
            name=y1axis_column_name,
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'},
                'color' : dff[y1axis_column_name],
                'colorscale':'Viridis'
            }
        )
    Observed = go.Scattergl(
        x=list(dff[xaxis_column_name]),
        y=list(dff[y2axis_column_name]),
        customdata=list(dff[xaxis_column_name]),
        name=y2axis_column_name,
        mode='markers',
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'},
        }
    )
    data = [Predicted,Observed]
    layout = go.Layout(
        xaxis={
            'title': xaxis_column_name,
        },
        yaxis={
            'title': y1axis_column_name,
        },
        yaxis2={
            'title': y2axis_column_name,
        },
        margin={'l': 40, 'b': 100, 't': 10, 'r': 40},
        height=450,
        hovermode='closest',
        clickmode='event+select'
    )
    return {
        'data': data,
        'layout': layout
    }

@app.callback(
    dash.dependencies.Output('output-container-range-slider','children'),[
    dash.dependencies.Input('crossfilter-year--slider1', 'value'),
    dash.dependencies.Input('crossfilter-view--slider1', 'value'),
    dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
    dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
    dash.dependencies.Input('crossfilter-density--slider4', 'value'),
    dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
    dash.dependencies.Input('crossfilter-root--slider6', 'value'),
    ]
)

def slider_ouput(*val1):
    return 'You have selected Year = {}, View = {}, Rank = {}, Skip = {}, Density = {}, Convg = {}, Root = {}'.format(*val1)

@app.callback(
    dash.dependencies.Output('output-container-range-slider1','children'),[
    dash.dependencies.Input('crossfilter-year--slider1', 'value'),
    dash.dependencies.Input('crossfilter-view--slider1', 'value'),
    dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
    dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
    dash.dependencies.Input('crossfilter-density--slider4', 'value'),
    dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
    dash.dependencies.Input('crossfilter-root--slider6', 'value'),
    ]
)

def slider_ouput(*val1):
    return 'You have selected Year = {}, View = {}, Rank = {}, Skip = {}, Density = {}, Convg = {}, Root = {}'.format(*val1)

@app.callback(
    dash.dependencies.Output('selPoint', 'children'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'selectedData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-y1axis-column', 'value'),
     dash.dependencies.Input('crossfilter-y2axis-column', 'value')
    ])
def show_selPoint(selectedData,xaxis_column_name, y1axis_column_name,y2axis_column_name):
    try: 
        x = selectedData['points'][0]['customdata']
        y = selectedData['points'][0]['y']
        c = selectedData['points'][0]['curveNumber']
        if c==0:
            t = y1axis_column_name
        else:
            t = y2axis_column_name
        return 'Selected point X: {}, Y: {}, Type: {}'.format(x,y,t)
    except:
        return 'Selected point'

@app.callback(
    dash.dependencies.Output('selected-data', 'children'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'selectedData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-y1axis-column', 'value'),
     dash.dependencies.Input('crossfilter-y2axis-column', 'value'),
     dash.dependencies.Input('crossfilter-year--slider1', 'value'),
     dash.dependencies.Input('crossfilter-view--slider1', 'value'),
     dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
     dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
     dash.dependencies.Input('crossfilter-density--slider4', 'value'),
     dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
     dash.dependencies.Input('crossfilter-root--slider6', 'value')
    ])
def display_selected_data(selectedData,xaxis_column_name, y1axis_column_name,y2axis_column_name,slider0,slider1,slider2,slider3,slider4,slider5,slider6):
    try:
        g_cols = ['Year','View', 'Rank', 'Skip', 'Density', 'Convg', 'Root']
        input_value = [slider0,slider1, slider2, slider3, slider4, slider5, slider6]
        dff = df.copy()
        for i, col_range in enumerate(input_value):
            dff = dff[col_range[0]<=dff[g_cols[i]]][dff[g_cols[i]]<=col_range[1]]
        
        x = selectedData['points'][0]['customdata']
        y = selectedData['points'][0]['y']
        c = selectedData['points'][0]['curveNumber']
        
        if c==0:
            dff = dff[dff[xaxis_column_name]==x][dff[y1axis_column_name]==y]
        else:
            dff = dff[dff[xaxis_column_name]==x][dff[y2axis_column_name]==y]
        ddt = dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in dff.columns],
                data=dff.to_dict('records'),
                n_fixed_rows=1,
                style_cell={'textAlign': 'left'},
                style_cell_conditional=[{
                        'if': {'column_id': 'Region'},
                        'textAlign': 'left'
                    }],
                sorting=True,
                )
        return ddt
    except TypeError:
        return (' ')

@app.callback(
    dash.dependencies.Output('graphs', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'selectedData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-y1axis-column', 'value'),
     dash.dependencies.Input('crossfilter-y2axis-column', 'value'),
     dash.dependencies.Input('crossfilter-year--slider1', 'value'),
     dash.dependencies.Input('crossfilter-view--slider1', 'value'),
     dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
     dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
     dash.dependencies.Input('crossfilter-density--slider4', 'value'),
     dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
     dash.dependencies.Input('crossfilter-root--slider6', 'value')
    ])
def display_selected_graph(selectedData,xaxis_column_name, y1axis_column_name,y2axis_column_name,slider0,slider1,slider2,slider3,slider4,slider5,slider6):
    try:
        g_cols = ['Year','View', 'Rank', 'Skip', 'Density', 'Convg', 'Root']
        input_value = [slider0,slider1, slider2, slider3, slider4, slider5, slider6]
        dff = df.copy()
        for i, col_range in enumerate(input_value):
            dff = dff[col_range[0]<=dff[g_cols[i]]][dff[g_cols[i]]<=col_range[1]]
        
        x = selectedData['points'][0]['customdata']
        y = selectedData['points'][0]['y']
        c = selectedData['points'][0]['curveNumber']
        
        if c==0:
            dff = dff[dff[xaxis_column_name]==x][dff[y1axis_column_name]==y]
        else:
            dff = dff[dff[xaxis_column_name]==x][dff[y2axis_column_name]==y]       
        fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=False,
                        vertical_spacing=0.5,horizontal_spacing=0.1,
                        subplot_titles=('View', 'Rank', 'Skip', 'Density', 'Convg', 'Root'))
    
        fig.append_trace({'x':dff['View'].value_counts().index,'y':dff['View'].value_counts().values,'type':'bar','name':'View'},1,1)
        fig.append_trace({'x':dff['Rank'].value_counts().index,'y':dff['Rank'].value_counts().values,'type':'bar','name':'Rank'},1,2)
        fig.append_trace({'x':dff['Skip'].value_counts().index,'y':dff['Skip'].value_counts().values,'type':'bar','name':'Skip'},1,3)
        fig.append_trace({'x':dff['Density'],'type':'histogram','name':'Density'},2,1)
        fig.append_trace({'x':dff['Convg'],'type':'histogram','name':'Convg'},2,2)
        fig.append_trace({'x':dff['Root'],'type':'histogram','name':'Root'},2,3)

        fig['layout'].update(title='Distribution of parameters of selected point')
        
        return fig 
    except TypeError:
        return {}

@app.callback(
    dash.dependencies.Output('graphs_2', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-y1axis-column', 'value'),
     dash.dependencies.Input('crossfilter-y2axis-column', 'value'),
     dash.dependencies.Input('crossfilter-year--slider1', 'value'),  
     dash.dependencies.Input('crossfilter-view--slider1', 'value'),
     dash.dependencies.Input('crossfilter-rank--slider2', 'value'),
     dash.dependencies.Input('crossfilter-skip--slider3', 'value'),
     dash.dependencies.Input('crossfilter-density--slider4', 'value'),
     dash.dependencies.Input('crossfilter-convg--slider5', 'value'),
     dash.dependencies.Input('crossfilter-root--slider6', 'value'),

    ])
def graph_selectd_slider(xaxis_column_name, y1axis_column_name,y2axis_column_name,slider0,slider1,slider2,slider3,slider4,slider5,slider6):
    g_cols = ['Year','View', 'Rank', 'Skip', 'Density', 'Convg', 'Root']
    input_value = [slider0,slider1, slider2, slider3, slider4, slider5, slider6]
    dff = df.copy() 
    for i, col_range in enumerate(input_value):
        dff = dff[col_range[0]<=dff[g_cols[i]]][dff[g_cols[i]]<=col_range[1]]

    try:
        
        fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=False,
                        vertical_spacing=0.5,horizontal_spacing=0.1,
                        subplot_titles=('View', 'Rank', 'Skip', 'Density', 'Convg', 'Root'))
    
        fig.append_trace({'x':dff['View'].value_counts().index,'y':dff['View'].value_counts().values,'type':'bar','name':'View'},1,1)
        fig.append_trace({'x':dff['Rank'].value_counts().index,'y':dff['Rank'].value_counts().values,'type':'bar','name':'Rank'},1,2)
        fig.append_trace({'x':dff['Skip'].value_counts().index,'y':dff['Skip'].value_counts().values,'type':'bar','name':'Skip'},1,3)
        fig.append_trace({'x':dff['Density'],'type':'histogram','name':'Density'},2,1)
        fig.append_trace({'x':dff['Convg'],'type':'histogram','name':'Convg'},2,2)
        fig.append_trace({'x':dff['Root'],'type':'histogram','name':'Root'},2,3)

        fig['layout'].update(title='Distribution of parameters of selected data')
        
        return fig 
    except TypeError:
        return {}
if __name__ == '__main__':
    app.run_server(debug=True)