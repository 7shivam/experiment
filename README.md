# Galaxy_BigFilms_Backend

1) This is Python fastapi backend for Galaxy_Bigfilms_backend project.
2) Below is the docker command to up a container for this project image 
3) docker run -p 8000:8000 -itd --network=my_network -e BUCKET_NAME="galaxy_bigfilms_movies_db" -e USER_NAME="shivam" -e PASSWORD="Qwerty@123456" -e IP_ADDRESS="http://172.18.0.2:8091" zabakar/galaxy_bigfilms_backend:latest
4) Before running this Back container You need to up CouchBase servers Belows are the details
5) docker network create my_network
6) Download the official image of Couchbase from dockerhub.
7) docker pull couchbase
8) up the couchbase container by following command
9) docker run -d --name db -p 8091-8094:8091-8094 -p 11210:11210 --network=my_network couchbase
10) Open the couchbase dashboard by `ip:8091`
11) click on setup new cluster
12) type cluster name `galaxy_bigfilms` and create a user and password
13) accept terms and conditions and click on configure Disk, Memory, services
14) configure according to you and click on save
15) Main dashboard will be open
16) now click on buckets -> Add bucket 
17) Type bucket name `galaxy_bigfilms_movies_db` click on add bucket
18) From the same page click on `documents -> Add document` 
19) type `id = 1`  and past the following json data
```
{
"id":1,
"Name":"wanted",
"Actors":"Salman Khan",
"Release":"2018-07-01",
"Rating":5,
"Image":"https://social-filmytadka-movies-images.s3.amazonaws.com/avengers.jpeg"
}
```
19) now go to qurey
20) now type the following to create primary index on that bucket
21) `create primary index on galaxy_bigfilms_movies_db;`
22) type the following query to check if every thing is good
23) `select * from galaxy_bigfilms_movies_db`
24) You should see the above json data
25) <h1> Creating a new couchbase user
26) click on security -> add user -> Type details and can give different permissions
27) Now you are ready to start your backend python fastapi container.
