
# coding: utf-8

# In[1]:

class User(object):
    
    def __init__(self, db):
        self.db = db
        
    def save(self, name):
        self.db.execute('insert into entries (username) values (?)', [name])
        self.db.commit()
        return True
    
    def get_list(self):
        cur = self.db.execute('select username from entries')
        return cur.fetchall()


# In[ ]:



