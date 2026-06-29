import duckdb
import os

#connect
con = duckdb.connect("warehouse.duckdb")

#create staging schema
con.execute("CREATE SCHEMA IF NOT EXISTS raw;")


def ingestion_query(source_path,table_name="raw.yellow_tripdata",first_load=False):
    #func to build query command
    main_command=f"CREATE OR REPLACE TABLE  {table_name} AS " if first_load else f"INSERT INTO {table_name} "

    query=f"""
    {main_command} 
    SELECT * 
    FROM read_csv_auto('{source_path}');
     """
    return query
    
for root,folders,files in os.walk('datalake'):
    if len(files )!=0: 
        
        for id,file in enumerate( sorted(files)):
            print('processing: ',root,file)
            #prepare query
            first_load= True if id ==0 else False
            table_name=f"raw.{os.path.basename(root)}_tripdata"
            source_path=os.path.join(root,file) 
            query=ingestion_query(source_path,table_name,first_load)
            
            #execute
            con.execute(query)

#disconnect
con.close()