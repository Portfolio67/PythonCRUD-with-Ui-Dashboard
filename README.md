<!doctype html>
<html>
<head>
	<meta charset="UTF-8">
	<title>CRUD Python Ui SFlaten.txt</title>
</head>
<body>
<h1>README SFlaten</h1>

<h2>About the Project/CRUD with Python and MongoDB</h2>

<p><em>This project takes up CVS database from a dog kennel resource management company, and places that data into an interactive sorting data chart with filters and maps.</em></p>

<p><em>This project uses a python</em> <em>library called</em> <em>Pymongo</em> <em>in a python</em> <em>module that connects</em> at a_ <em>mongo database.</em> <em>From there the python module will Create a new data element in a dictionary form to be</em> <em>an</em> <em>input into the mongo database,</em> <em>then</em> <em>this python module will</em> <em>Read from that same database any item that is called</em> _after locating it. </p>

<h2>Motivation</h2>

<p><em>This project exists for learning and testing purposes. It’s a relatively simple project with powerful usages. Being able to do crud commands is a</em> <em>stepping</em> _point into API calls from any website or software you design. <em>MongoDB is a very effective database. It uses the JavaScript language, so you don’t have to re-learn a different database language if you’re developing for the web in JavaScript. I think Python</em> <em>is a very versatile language, with easy syntax and</em> <em>a</em> _wide range of pre-made <em>libraries.</em> <em>This project also helps a real-life situation where someone is trying to organize kennels throughout a metropolitan area to provide service for people who need service dogs.</em></p>

<h2><strong><em>About</em></strong> <strong><em>writing code for a client.</em></strong></h2>

<p><em>Programs must be read and maintained. This is true if you’re working with group of people. The main way to keep it maintainable and readable is to make your project modular. This project uses a model view and controller. In the crud python module, the methods of that class are defined as create read update and delete. There are code comments within, and above, the methods to explain what the method does, and any unique features inside the method; like changing the format from a Json to dictionary. It is also good practice to explain which section of the code will be manipulating what. It’s better to use the larger comments sections for outlining. This format keeps it modular for anyone reading the code for wanting to add to it. Format changing can be difficult to see in the code, I put in comments when data is being reformatted for another library. In this project the client had clear and defined needs that can be translated into goals for the project. In this case they needed to filter specific dog breeds and age into groups, where they could be searched for certain types of rescue missions. The client wanted to see this on the user interface. When I tackled the goals of the project, I went one component at a time down the list and fulfilled the requirements outlined. This project required the CRUD module to not change. In the future I would make it more dynamic and modular that allowed for filtering inside the CRUD. This was a difficult task to do with python libraries alone. Computer scientists do a lot more than writing code. Computer scientists have to</em> <em>work through a problem in a step-by-step basis to come up with a solution that works for the company. In this project the computer scientist would ask what’s more important, the age of the dog or the breed? The client asked for a chart, without any specifications. As a computer scientist I thought the main contributing factor on the train ability of a dog, is the age. Taking this into consideration I made a chart that showed the breed of the dog versus the age of the dog.</em></p>

<h2><strong><em>Required functionality</em></strong></h2>

<p><em>The app must pull data from a CSV file into a mongo DB database. Python module must be used to create read update and delete the database. This database must also be password-protected. A separate file must have the functionality of retrieving the data from Mongo Via the python CRUD module to perform actions on that data. The data must be put into a pandas data frame which is a python library. A user interface must be made, and that user interface must have the logo of the company with a hyperlink, the name of the creator, user interaction buttons to perform sorting on the data, a database is then displayed on the Ui of the app, from my displayed data a chart along side</em> <em>a map must display the filter data.</em></p>

<figure>
<img images="s1.png" alt="" />
</figure>

<figure>
<img src="s2.png" alt="" />
</figure>

<figure>
<img src="s3.png" alt="" />
</figure>

<figure>
<img src="s4.png" alt="" />
</figure>

<figure>
<img src="s5.png" alt="" />
</figure>

<h2>****_Tools used to achieve functionality.**</h2>

<p><em>Python and mongo DB are the two main resources used. The python libraries are Jupiter</em> <em>plotly</em> <em>Dash, the dash library, dash core components used in user interface areas that interact with html and other components in python,</em> _plotly <em>express which is used for the chart, dash table which is used for the map.</em> <em>Pandas</em> <em>python library which is used for the data set, pandas python library which is used for the data set and</em> <em>pymongo</em> <em>which is used to communicate with mongo DB.</em></p>

<h2><strong><em>Steps taken to complete the project</em></strong></h2>

<p><em>This was an iterative project required to first develop the mongo DB database by importing the data, then the crud module to interact with that data. There was a lot of testing during this phase to get authentication to work. From their the user interface dashboard was created to display a spreadsheet on a user interface. From there filtering that interface, finally piping that interface data that’s displayed to a map and chart. Testing is done throughout.</em></p>

<h2><strong><em>Challenges.</em></strong></h2>

<p><em>Challenges were testing the mongo DB database and authentication because it’s in command line makes it more difficult. Testing the Bungo database against the crud was difficult because of the debugger was difficult to understand in terminal. The biggest difficulty was the @app.callbacks. This information is continually piped into the user interface and is difficult to the bug, sometimes it just will not run the program at all without any explanation in the debugger.</em> <em>Finally</em> _the biggest challenge for me was putting this on my own system. This works great in Linux, but Mac has a lot of issues with making charts maps even after everything has been downloaded an imported. </p>

<h2>Getting Started</h2>

<p><em>This area I’ll show you how to set up the same project. You may want to scroll down to the installation if you do not have everything installed to run this project. You will need</em> <em>mongoDB,</em> <em>python,</em> <em>Jupiter notebook, from Mac you’ll need</em> <em>Xcodecommand line tools. This could run on Mac or Linux,</em> <em>and I have given examples for both.</em> <em>But the instructions here are for Mac</em> <em>to run it locally. It is simple to run this on Linux. Jupiter notebooks is a great IDE for</em> <em>learning, as</em> <em>you can run specific code snippets.</em> _Another tool you can use as mongo compass. <em>You can also get a free account and run mongo online</em> <em>if you wish.</em> <em>You’re also going to need Dash, with many python libraries to go with.</em></p>

<p>_To start mongo from command line and create an admin account </p>

<p>brew services start mongodb-community@5.0</p>

<p>mongo</p>

<p>use admin</p>

<p>db.createUser({user: &quot;myUserAdmin&quot;,pwd: passwordPrompt(),roles: [ { role: &quot;userAdminAnyDatabase&quot;, db: &quot;admin&quot; }, &quot;readWriteAnyDatabase&quot; ]})</p>

<p>exit</p>

<p>brew services stop mongodb-community@5.0</p>

<p><em>To</em> <em>start</em> <em>mongo</em> <em>an import a json or PDF file to make a new database</em></p>

<p><em>LINUX*****</em></p>

<p><em>Start mongo from shell</em></p>

<p>/usr/local/bin/mongod_ctl start-noauth</p>

<p><em>Move into the location of where the file is located. In this case its datasets</em></p>

<p>cd /usr/local/datasets</p>

<p>mongoimport --port ##### --db enron --collection emails ./enron.json</p>

<p>mongoimport --port ##### --db AAC --collection animals --type=csv --headerline ./aac_shelter_outcomes.csv</p>

<p><em>MAC***** my datasets are in my home directory. As shown</em> ~/ <em>In order to import you cannot be in the</em> <em>mongoDB</em> <em>shell you must be in the regular shell.</em></p>

<p>brew services start mongodb-community@5.0</p>

<p>mongo</p>

<p>show dbs</p>

<p>mongoimport --db enron --collection emails 

 --file ~/datasets/enron.json</p>

<p>mongoimport --db city --collection inspections 

 --file ~/datasets/city_inspections.json</p>

<p>mongoimport --db AAC --collection animals --type=csv --headerline 

 --file ~/datasets/aac_shelter_outcomes.csv</p>

<p>use enron <span class="hashtag">#this</span> sets db to the enron database</p>

<p>show collections <span class="hashtag">#lists</span> directory of collections</p>

<p>db.emails.findOne() </p>

<p><em>To</em> <em>start</em> <em>mongo from command line</em> <em>and create a user account.</em> <em>Remember to use straight quotation marks, not curved ones or this will not work.</em></p>

<p>brew services start mongodb-community@5.0</p>

<p>mongo --authenticationDatabase &quot;admin&quot; -u &quot;myUserAdmin&quot; -p</p>

<p>use AAC</p>

<p>db.createUser(</p>

<p>{</p>

<pre><code>user: &quot;aacuser&quot;,

pwd:  passwordPrompt(),  

roles: [ { role: &quot;readWrite&quot;, db: &quot;ACC&quot; },

         { role: &quot;read&quot;, db: &quot;reporting&quot; } ]
</code></pre>

<p>}</p>

<p>)</p>

<p>mongo --authenticationDatabase &quot;user&quot; -u &quot;aacuser&quot; -p</p>

<p><em>or</em></p>

<p>mongo --username aacuser --password Dog --authenticationDatabase ACC</p>

<p>db.getUsers()</p>

<p>show dbs</p>

<p>use widgetdb </p>

<p>show collections</p>

<p>use usewidgetcollections</p>

<p><em>various terminal commands</em></p>

<p>db.collection.totalSize();</p>

<p>db.collection..find({&quot;id&quot; : &quot;10021-2015-ENFO&quot;})</p>

<p>db.collection.insertOne(</p>

<p>{ &quot;id&quot; : “20032-2020-ACME”,</p>

<pre><code> &quot;certificate_number&quot; : 9998888,

 &quot;business_name&quot; : “ACME Explosives”,

 &quot;date&quot; : Date(),

 &quot;address&quot; : { &quot;number&quot; : 1721, &quot;street&quot; : &quot;Boom Road&quot;, &quot;city&quot; : &quot;BRONX&quot;, &quot;zip&quot; : 10463} })
</code></pre>

<p>db.database.createIndex( { breed: 1 } )</p>

<p><em>Connect</em> <em>Jupiter</em> <em>to</em> <em>dbs</em> <em>with</em> <em>python.</em></p>

<p>jupyter notebook</p>

<p>brew services start mongodb-community@5.0</p>

<p>mongo --authenticationDatabase &quot;admin&quot; -u &quot;myUserAdmin&quot; -p</p>

<p><em>IN</em> <em>Jupiter</em> <em>notebook.</em></p>

<p>Choose file -&gt; new python 3. This will give you a Jupiter file to run.</p>

<p><em>IN</em> <em>Jupiter</em> <em>notebook paste this in. you needmongoclient() to connect, local host id default 27017 and the %s:%s is where the</em> <em>userId: password gets format pasted.</em></p>

<p>client=MongoClient('mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&amp;authSource=AAC' % (&quot;userId&quot;, &quot;Password&quot;))</p>

<p><em>IN</em> <em>Jupiter</em> <em>notebook here is some example code to see if you up and running.</em></p>

<p>from pymongo import MongoClient</p>

<p>from bson.objectid import ObjectId</p>

<p>import pprint</p>

<p>client = MongoClient()</p>

<p>client=MongoClient('mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&amp;authSource=AAC' % (&quot;userID&quot;, &quot;Password&quot;))</p>

<p>db = client.DatabaseName</p>

<p>db.list_collection_names()</p>

<p>collection = db.collection</p>

<h2>Installation</h2>

<p><em>First you need</em> <em>xcode</em> <em>command line tools.</em></p>

<p><em>In terminal</em> </p>

<p>xcode-select –install</p>

<p><em>Next you need homebrew.</em></p>

<p><em>In terminal</em> _type. </p>

<p>/usr/bin/ruby -e &quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)&quot;</p>

<p>brew update &amp;&amp; brew doctor</p>

<p><em>Next you need a version manager</em></p>

<p>brew install pyenv</p>

<p><em>Then</em> <em>install python 3.0.</em></p>

<p>pyenv install 3.10.0</p>

<p>pyenv versions</p>

<p><em>Next update bash profile.</em></p>

<p>echo 'eval &quot;$(pyenv init -)&quot;' &gt;&gt; ~/.bash_profile</p>

<p><em>Set python to global.</em></p>

<p>pyenv global 3.x.x</p>

<p><em>Now you need</em> <em>Jupyter</em> <em>notebook.</em></p>

<p>brew install jupyter</p>

<p><em>Start the notebook</em></p>

<p><em>In terminal type</em></p>

<p>jupyter notebook</p>

<p><em>To install mongo from command line</em></p>

<p>brew tap mongodb/brew</p>

<p>brew install mongodb-community@5.0</p>

<p>After that read the import statements in the files listed below you will see all the different libraries you need to import through command line to go with your python.</p>

<h2>Usage</h2>

<p><em>First let’s try to see if your Mongo database is connecting with something simple.</em></p>

<p><em>In this whole project you will be using</em> <em>pyMongo.</em> <a href="https://pymongo.readthedocs.io/en/stable/"><em>https://pymongo.readthedocs.io/en/stable/</em></a></p>

<p><em>MongoClient(). Is what is used to make the connection. In the below there is no authentication on a simple database with the collection named Emails. It is printing the</em> <em>key :</em> <em>value pair.</em></p>

<figure>
<img src="Screen%20Shot%202021-11-19%20at%205.17.25%20AM.png" alt="" />
</figure>

<h3></h3>

<p><em>If you have</em> <em>that working right now you can move onto a CRUD with authentication.</em> <em>After importing</em> <em>pymongo</em> <em>and BSON which reads the correct format into the</em> <em>mongoDB. A class is created called animal shelter which will be used later when called from another file which will use the methods within that class. Def <strong>init</strong> (self) initializes an object. Mongo client is what is commonly used to connect to the Mongo database. Use the format below in the code examples for authenticating with a specific user and password. After authentication has been completed there are three methods to create, locate and delete. Those methods call MongoDB JavaScript functions with “data” as a parameter; to insert, find or remove. Please note that the data parameter will be in a dictionary format, and is passed from the second file, or testing file. Another thing to note;</em> <em>this</em> <em>python script</em> <em>is working animals, a</em> <em>collection which was made during the import of the database.</em> <em>See the</em> <em>2nd</em> <em>code example below.</em></p>

<h2></h2>

<h2>Code Example</h2>

<ol>
<li><em>Importing code, making an index, and creating users-</em> <em>examples</em></li>
</ol>

<figure>
<img src="21.png" alt="" />
</figure>

<figure>
<img src="22.png" alt="" />
</figure>

<p><em>This is the CVS format you can import JSON into</em> <em>mongoDB</em></p>

<h1>Screenshots</h1>

<h2><em>Part I: Importing and Indexing a Data Set</em></h2>

<h2><strong><em>Import CSV file using mongo DB import.</em></strong> _Notice I’m using mongo compass to verify the amount of documents examined and the query time.</h2>

<figure>
<img src="23.png" alt="" />
</figure>

<figure>
<img src="24.png" alt="" />
</figure>

<figure>
<img src="25.png" alt="" />
</figure>

<figure>
<img src="26.png" alt="" />
</figure>

<figure>
<img src="27.png" alt="" />
</figure>

<figure>
<img src="28.png" alt="" />
</figure>

<h2><em>Simple index and the Explain function</em>.</h2>

<figure>
<img src="30.png" alt="" />
</figure>

<figure>
<img src="31.png" alt="" />
</figure>

<figure>
<img src="32.png" alt="" />
</figure>

<h2><em>Part II: User Authentication</em></h2>

<h2><em>Admin account –</em></h2>

<figure>
<img src="33.png" alt="" />
</figure>

<h2><em>Enable authentication</em></h2>

<figure>
<img src="34.png" alt="" />
</figure>

<h2><em>CRUD code example</em></h2>

<figure>
<img src="35.png" alt="" />
</figure>

<p>from pymongo import MongoClient</p>

<p>from bson.objectid import ObjectId</p>

<p>class AnimalShelter(object):</p>

<pre><code>&quot;&quot;&quot; CRUD operations for Animal collection in MongoDB &quot;&quot;&quot;

def __init__(self):

    # Initializing the MongoClient and access the MongoDB databases and collections. #Default is 27017

    self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&amp;authSource=AAC' % (&quot;aacuser&quot;, &quot;Dog&quot;))

    self.database = self.client['AAC']

def create(self, data):

    if data is not None:

        #self.database.animals.insert(data) # data should be dictionary

    #Store the results of the insert to variable

        insert_result = self.database.animals.insert(data) # data should be dictionary

        #If insert was successful, return True, else, return False

        if insert_result is not None:

            status = True

        else:

            status = False

        return status

    else:

        raise Exception(&quot;Nothing to save, because data parameter is empty&quot;)
</code></pre>

<h2>Method to implement the R in CRUD.</h2>

<pre><code>def locate(self, data):

#Verify that search criteria was provided, else raise an exception

    if data is not None:

        animalsCollection = self.database.animals.find(data)

        #print(search_result)

        for animals in animalsCollection:

            print(animals)

    else:

        raise Exception(&quot;No search criteria provided&quot;)
</code></pre>

<h2><em>Implementing CRUD example</em></h2>

<h2>/1.png</h2>

<p>Display the data</p>

<figure>
<img src="35.png" alt="" />
</figure>

<p><em>This case you’ll be using dash core components to display any components like buttons or radio</em>. <em>Also use the dash table from Dash to display in HTML, below is the radio button. Every component must have an ID to be called from the @app callback.</em> one callback per ID. Call back is a persistence feature that constantly updates the HTML. This is consider_ <em>the decoration for the function below it. It takes input data,</em> <em>or button</em> <em>click with a button label or value.</em></p>

<figure>
<img src="3.png" alt="" />
</figure>

<p><strong><em>https://dash.plotly.com/dash-core-components</em></strong></p>

<p><em>This is what the data looks like coming from Jason and put it into</em> <em>pandas</em> <em>format.</em></p>

<figure>
<img src="5.png" alt="" />
</figure>

<p>_You can place all the HTML elements like the logo on top with a hyperlink in the button like you were on a website. <em>https://dash.plotly.com/dash-html-components</em> </p>

<figure>
<img src="6.png" alt="" />
</figure>

<p><strong><em>Filtering</em></strong></p>

<p><strong><em>Noticed the input is the filter type what should be the name and value of that name. The output goes straight up to your data table ID in HTML. Keira making the first data frame from panda that reads the Jason format. The</em></strong> <strong><em>dfff</em></strong> <strong><em>after that is another panda state of frame that uses the location of the header in the</em></strong> <strong><em>pandas</em></strong> <strong><em>data frame. As you can</em></strong> <strong><em>see</em></strong> <strong><em>I further filter down the line until I end up with my last data frame query.</em></strong> <strong><em>The LOC is a string variable type pandas data frame, which is the header. This uses standard python operators for some reason</em></strong> <strong><em>the or</em></strong> <strong><em>brought back more data than the and operator, maybe because it does more than one iteration.</em></strong></p>

<p><strong><em>https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html</em></strong></p>

<figure>
<img src="7.png" alt="" />
</figure>

<p><em>This then gets passes Out and turns into the input for</em> <em>the viewport</em> _data take it and put it into the graph and map. </p>

<p><strong><em>Graphing in</em></strong> <strong><em>Mapping</em></strong></p>

<p><em>First</em> <em>first</em> <em>thing to keep in mind is that you’ll be using</em> <em>pandas</em> <em>data frame. To manipulate any data into graphing or mapping you need to put it into a pandas data frame do this by calling</em> _pd.Dataframe.from_dict(the data)_ <em>the data in this case is from the viewport which is already been displayed.</em> <em>From there it is converted into a</em> <em>plotly</em> <em>express graph. And</em> <em>finally</em> <em>it has to be put into a Dash core component graph method before it is returned to the viewport.</em></p>

<p><a href="https://plotly.com/python/plotly-express/"><em>https://plotly.com/python/plotly-express/</em></a></p>

<figure>
<img src="8.png" alt="" />
</figure>

<figure>
<img src="10.png" alt="" />
</figure>

<p><em>Sff</em> <em>is the pandas, dcc is dash core, px is express.</em></p>

<figure>
<img src="1.png2.png" alt="" />
</figure>

<p>Above is the map which uses dash leafly <a href="https://dash-leaflet.herokuapp.com">https://dash-leaflet.herokuapp.com</a></p>

<p><a href="https://pypi.org/project/dash-leaflet/">https://pypi.org/project/dash-leaflet/</a></p>

<p>Taking a pandas data frame and using iloc Retrieves the column number. The marker position is the point on the map that’s highlighted. The pop-up is when you hover over at the data that is shown.</p>

<p>HERE IS THE FINAL CODE</p>

<hr />

<pre><code class="python">from jupyter_plotly_dash import JupyterDash
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
username = &quot;aacuser&quot;
password = &quot;Dog&quot;
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
        persistence_type=&quot;memory&quot;, # not sure if this works with this code below, but no errors
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
             {&quot;name&quot;: i, &quot;id&quot;: i, &quot;deletable&quot;: False, &quot;selectable&quot;: True} for i in df.columns
         ],
         data=df.to_dict('records'),
        #features for your interactive data table to make it user-friendly for your client
        editable=False,
        #suppress_callback_exceptions=True
        filter_action=&quot;native&quot;,
        sort_action=&quot;native&quot;,
        sort_mode=&quot;multi&quot;,
        column_selectable=True,
        row_selectable=True,
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action=&quot;native&quot;,
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
        #pandas uses python operators,  the &amp; did not work,  The + brought a smaller list that the or operator, weird?... https://www.w3schools.com/python/python_operators.asp
        # df is a pandas dataframe type. retreived from the mongo database
        #dffff is a pandas datafram type -&gt; dfff..  and so on filtering each dataframes 
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram for strings.  iloc is for ints https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        dfff = dffff.loc[(dffff['breed'] == 'Labrador Retriever Mix') | (dffff['breed'] == 'Labrador Retriever') | (dffff['breed'] == 'Newfoundland Mix') | (dffff['breed'] == 'Newfoundland') | (dffff['breed'] == 'Chesapeake Bay Retriever')]
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Female')] 
        df = dff.query('26 &lt;= age_upon_outcome_in_weeks &lt;= 156')       #df.query('A &gt; B') https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
        
    elif filter_type == 'MWR':
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram
        dfff = dffff.loc[(dffff['breed'] == 'German Shepherd') | (dffff['breed'] == 'Alaskan Malamute') | (dffff['breed'] == 'Old English Sheepdog') | (dffff['breed'] == 'Siberian Husky')| (dffff['breed'] == 'Rottweiler')]
       
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Male')]
        df = dff.query('26 &lt;= age_upon_outcome_in_weeks &lt;= 156')  
        
    elif filter_type == 'DR':
        dffff = pd.DataFrame.from_records(shelter.read({})) # pandas loc is used in the pandas datafram
        dfff = dffff.loc[(dffff['breed'] == 'Doberman Pinscher') | (dffff['breed'] == 'German Shepherd') | (dffff['breed'] == 'Golden Retriever') | (dffff['breed'] == 'Rottweiler')| (dffff['breed'] == 'Doberman Pinscher')]
        dff = dfff.loc[(dfff['sex_upon_outcome'] == 'Intact Male')]
        df = dff.query('20 &lt;= age_upon_outcome_in_weeks &lt;= 300')  
    elif filter_type == 'RS':
        df = pd.DataFrame.from_records(shelter.read({}))
            
    columns=[{&quot;name&quot;: i, &quot;id&quot;: i, &quot;deletable&quot;: False, &quot;selectable&quot;: True} for i in df.columns]
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
    Output('graph-id', &quot;children&quot;),
    [Input('datatable-id', &quot;derived_viewport_data&quot;)])
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
    Output('map-id', &quot;children&quot;),
    [Input('datatable-id', &quot;derived_viewport_data&quot;)])
def update_map(viewData):
    dff = pd.DataFrame.from_dict(viewData)
    # Austin TX is at [30.75, -97.48]
    latitude = dff.iloc[0,13]
    longitude = dff.iloc[0,14]
    return[
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[dff.iloc[0,13],dff.iloc[0,14]], zoom=10, children=[
            dl.TileLayer(id=&quot;base-layer-id&quot;),
            # Marker with tool tip and popup
            dl.Marker(position=[dff.iloc[0,13],dff.iloc[0,14]], children=[
                dl.Tooltip(dff.iloc[0,4]),
                dl.Popup([
                    html.H1(&quot;Animal Name&quot;),
                    html.P(dff.iloc[0,9]), # row, column
                    html.P(dff.iloc[0,13]), 
                    html.P(dff.iloc[0,14]) 
                    
                    
                ])
            ])
        ])
    ]
app
</code></pre>

<hr />

<pre><code class="python">from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class AnimalShelter(object):

    &quot;&quot;&quot; CRUD operations for Animal collection in MongoDB &quot;&quot;&quot;

    def __init__(self,username,password):

        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/%s'%(username, password, 'AAC'))
        #self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&amp;authSource=AAC' %s (username, password))
        self.database = self.client['AAC']

# create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            #self.database.animals.insert(data)  # data should be dictionary            
        #Store the results of the insert to variable
            insert_result = self.database.animals.insert(data)  # data should be dictionary

            #If insert was successful, return True, else, return False
            if insert_result is not None:
                status = True
            else:
                status = False
            return status

        else:
            raise Exception(&quot;Nothing to save, because data parameter is empty&quot;)

# Method to implement the R in CRUD.
    def read(self, data):
    #Verify that search criteria was provided, else raise an exception
        #print (&quot;Read&quot;)
        if data is not None:
            animalsCollection = self.database.animals.find(data,{&quot;_id&quot;:False})
            
            return animalsCollection
            #print animalsCollection cursor
            
            #for animals in animalsCollection:
                #print(animals)
        else:
            raise Exception(&quot;No search criteria provided&quot;)
            
# Method to implement the U in CRUD
    def update(self, query, record):

        #Verify that the record exists; if so, update accordingly
        if record is not None:
            # update the documents matching the query criteria and print no. of documents updated in json format
            update_result = self.database.animals.update_many(query, record)
            result= &quot;Documents updated: &quot; + json.dumps(update_result.modified_count)
            #print(&quot;Documents updated &quot;, json.dumps(update_result.modified_count))
            return result

        else:
            raise Exception(&quot;Record not found&quot;)

# Method to implement the D in CRUD
    def delete(self, data):

        #Verify that the record to be deleted has been supplied
        if data is not None:
            # delete the documents matching data criteria and print no. of documents deleted in json format
            delete_result = self.database.animals.delete_many(data)
            result = &quot;Documents deleted: &quot;+ json.dumps(delete_result.deleted_count)
            #print(&quot;Documents deleted &quot;, json.dumps(delete_result.deleted_count))
            return result

        else:
            raise Exception(&quot;No record provided.&quot;)
</code></pre>

<hr />

<h2>Test</h2>

<figure>
<img src="13.png" alt="" />
</figure>

<p><em>There are a couple ways to test this one you can just run simple commands of create and read while looking at the output on the terminal of the IDE. You can also use the Python Unit test library. I have two examples of that below</em> <em>I have tested and ran successfully.</em> <em>The third car is a different method that I have not placed in this ReadMe.</em> <em>To test the map and graph data, it’s hard to see when somethings in the call back so you have to use your terminal in this</em> <em>case</em> <em>I adjusted the settings on Jupiter notebook to get a terminal output.</em></p>

<p><em>Here is the error for a</em> _plotly <em>exress.</em></p>

<h3>Screenshots</h3>

<figure>
<img src="14.png" alt="" />
</figure>

<p>import unittest</p>

<p>from module4 import AnimalShelter</p>

<p>class NamesTestCase(unittest.TestCase):</p>

<p>def test_create_one_dictionary(self):</p>

<pre><code>   result = AnimalShelter().create({'age_upon_outcome': '7 years', 'animal_id': '123ABC989', 'animal_type': 'Dinosaur', 'breed': 'Philosoraptor', 'color': 'Green/Blue', 'date_of_birth': '1999-01-01', 'datetime': '2000-01-01 01:00:00', 'monthyear': '2000-01-01T01:00:00', 'name': 'Chompy', 'outcome_subtype': 'SCRP', 'outcome_type': 'Transfer', 'sex_upon_outcome': 'Neutered Male', 'location_lat': '25.0000', 'location_long': '71.0000', 'age_upon_outcome_in_weeks': '366.012'})

   self.assertEqual(result, True)

def test_create_list(self):

    # data should be dictionary

   result = AnimalShelter().create(['age_upon_outcome', '7 years', 'animal_id' '123ABC989', 'animal_type' 'Dinosaur', 'breed' 'Philosoraptor', 'color' 'Green/Blue', 'date_of_birth' '1999-01-01', 'datetime' '2000-01-01 01:00:00', 'monthyear' '2000-01-01T01:00:00', 'name' 'Chompy', 'outcome_subtype' 'SCRP', 'outcome_type' 'Transfer', 'sex_upon_outcome', 'Neutered Male', 'location_lat', '25.0000', 'location_long', '71.0000', 'age_upon_outcome_in_weeks', '366.012'])

   self.assertEqual(result, False) 

 def test_create_one(self):

    # data should be dictionary

   self.assertRasies(Exception(&quot;Nothing to save, because data parameter is empty&quot;), AnimalShelter().create())
</code></pre>

<p>/14 2.png</p>

<figure>
<img src="15.png" alt="" />
</figure>

<figure>
<img src="17.png" alt="" />
</figure>

<h2>Contact</h2>

<p>My name: Shane Flaten</p>

<p>REFERENCES</p>

<p><a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/">https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/</a></p>

<p><a href="https://medium.com/@blessedmarcel1/how-to-install-jupyter-notebook-on-mac-using-homebrew-528c39fd530f">https://medium.com/@blessedmarcel1/how-to-install-jupyter-notebook-on-mac-using-homebrew-528c39fd530f</a></p>

<p>Giamas A. <em>Mastering MongoDB 4.0, Second Edition</em></p>

<p>MongoDB Documentation. <em>Enable Access Control</em></p>

<p><a href="https://docs.mongodb.com/manual/tutorial/enable-authentication/">https://docs.mongodb.com/manual/tutorial/enable-authentication/</a></p>

<p>MongoDB Documentation. <em>Import</em></p>

<p>https://docs.mongodb.com/database-tools/mongoimport/</p>

<p>unittest — Unit testing framework</p>

<p><a href="https://docs.python.org/3/library/unittest.html">https://docs.python.org/3/library/unittest.html</a></p>

<p><a href="https://medium.com/@pragya_paudyal/connecting-mongodb-to-jupyter-notebook-e3f636a85830">https://medium.com/@pragya_paudyal/connecting-mongodb-to-jupyter-notebook-e3f636a85830</a></p>

<p><a href="https://medium.com/@iamclement/how-to-install-jupyter-notebook-on-mac-using-homebrew-528c39fd530f">https://medium.com/@iamclement/how-to-install-jupyter-notebook-on-mac-using-homebrew-528c39fd530f</a></p>
</body>
</html>
