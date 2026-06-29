import requests
import os

#create dir 
def check_dir(_dir='datalake'):
    if os.path.exists(_dir)==False:
        os.mkdir(_dir)
list_check_dir=['datalake','./datalake/green','./datalake/yellow']
[check_dir(i) for i in list_check_dir]

#execute download
def download_file(file_id='2020-01',dataset='yellow'):
    print('Processing: ', dataset, file_id)
 
    file_url = lambda file_id: f"https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/{dataset}/{dataset}_tripdata_{file_id}.csv.gz"
    file_name=lambda file_id:f'.//datalake//{dataset}//{dataset}_tripdata_{file_id}.csv'
  
    response = requests.get(file_url(file_id))
    response.raise_for_status()  

    with open(file_name(file_id), "wb") as f:
        f.write(response.content)

selected_files={
    'green':['2021-01','2021-02','2021-03','2021-04','2021-05','2021-06','2021-07'],
    'yellow':['2021-01','2021-02','2021-03','2021-04','2021-05','2021-06','2021-07']
}

if __name__=='__main__':
    for dataset,list_files_id in selected_files.items():
        for file_id in list_files_id:
            download_file(file_id,dataset)
     