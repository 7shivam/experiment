from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import APIRouter
movie = APIRouter()
import json
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import QueryOptions
bucket_name = os.environ.get('BUCKET_NAME')
cluster = Cluster(os.environ.get('IP_ADDRESS'), ClusterOptions(
  PasswordAuthenticator(os.environ.get('USER_NAME'), os.environ.get('PASSWORD'))))
cb = cluster.bucket(bucket_name)
# get a reference to the default collection, required for older Couchbase server versions
cb_coll_default = cb.default_collection()
# get document function
def get_movie_by_key(key):
  try:
    result = cb_coll_default.get(key)
    return(result.content_as[str])
  except Exception as e:
    return(e)
    
def lookup_by_callsign(cs):
  try:
    mov_list=[]
    sql_query = f"select * from {bucket_name}"
    row_iter = cluster.query(sql_query,QueryOptions(positional_parameters=[cs]))
      
    for row in row_iter:
        mov_list.append(row.get(bucket_name))
    return mov_list
  except Exception as e:
    return(e)

@movie.get('/')
async def fetch_movies():
    return lookup_by_callsign("CBS")



@movie.get('/{id}')
async def fetch_movie(id: int):
    movie_list=[]
    movie_list.append(eval(get_movie_by_key(f"{id}")))
    return movie_list

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

app.include_router(movie)
