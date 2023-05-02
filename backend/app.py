from flask import Flask ,request
from flask_cors import CORS, cross_origin
import requests
import pandas as pd
import duckdb
import os
import datamart_profiler

app = Flask(__name__)


def download_and_save(id):
    filename=id.replace(".","_").replace("-","_")+".parquet"
    response=requests.get('https://auctus.vida-nyu.org/api/v1/download/'+id)
    if response.status_code==200:
        data=response.content.decode()
        list=[x.split(',') for x in data.split('\n')]
        df=pd.DataFrame(list[1:],columns=list[0])

        profiles=datamart_profiler.process_dataset(df)
        for c in profiles['columns']:
            dtypes=[]
            dtypes.append(c['structural_type'].split('/')[-1])
            for s in c['semantic_types']:
                dtypes.append(s.split('/')[-1])
            try:
                if "DateTime" in dtypes:
                    df[c['name']] = pd.to_datetime(df[c['name']], format='%Y-%m-%d')
                elif "Integer" in dtypes:
                    df[c['name']]=df[c['name']].fillna(0).astype(float).astype(int)
                elif "Float" in dtypes:
                    df[c['name']]=df[c['name']].fillna(0).astype(float)
                elif "Text" in dtypes:
                    df[c['name']]=df[c['name']].fillna("null").astype(str)
            except:
                pass

        df.to_parquet(filename)
        print("parquet file profiled and saved")
        

        return True
    return False
    


@app.route('/query')
@cross_origin()
def query():

    id = request.args.get('id')
    query=request.args.get('query')

    filename=id.replace(".","_").replace("-","_")+".parquet"

    if not os.path.isfile(filename):
        if not download_and_save(id):
            return {"data":"[]","error":True,"message":"Dataset is not downloadable"}

    con=duckdb.connect("flask.db")
    query_result=[]
    if not query:
        query_result=con.sql(" from "+filename).fetchdf().to_json(orient='records')
    else:
        try:
            query=query.replace("TABLE",filename)
            query_result=con.sql(query).fetchdf().to_json(orient='records')
        except:
            return {"data":"[]","error":True,"message":"Error in query"}

    return {"data":query_result,"error":False,"message":"success"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000 ,debug=True)
