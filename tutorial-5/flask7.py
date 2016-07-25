
# coding: utf-8

# In[1]:

import os
import sqlite3
from models.user import User


# In[2]:

from flask import Flask, request, render_template, g


# In[3]:

app = Flask(__name__)
app.config.from_object(__name__)


# In[4]:

app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flask_test.db')
    ))


# In[5]:

def connect_db():
    if not hasattr(g, 'db_con'):
        g.db_con = sqlite3.connect(app.config['DATABASE'])
        g.db_con.row_factory = sqlite3.Row
    return g.db_con


# In[6]:

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db_con'):
        g.db_con.close()


# In[7]:

@app.route('/list')
def list():
    db = connect_db()
    u = User(db)
    usernames = u.get_list()
    return render_template('list2.html', users=usernames)


# In[8]:

app.run()


# In[ ]:



