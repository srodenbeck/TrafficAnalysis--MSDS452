#%%
### Import libraries
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import pandas as pd
#%%
class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.uri = uri
        self.user = user
        self.pwd = pwd
        self.driver = None
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.driver is not None:
            self.driver.close()
        
    def query(self, query, db=None):
        assert self.driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.driver.session(database=db) if db is not None else self.driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response



# %%
uri = '<uri>'
user = '<usr>'
pwd = '<pwd>'
# %%
conn = Neo4jConnection(uri = uri,
                        user = user,
                        pwd = pwd)

#%%
query_engine = conn.driver.session()
query = "MATCH (n:From_Node) RETURN n.node, n.X, n.Y LIMIT 25"
out = query_engine.run(query).to_df()
# %%
## OR
data = pd.DataFrame([dict(_) for _ in conn.query(query)])
# %%
