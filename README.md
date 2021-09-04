# Martin Test

Test environment to use Django, PostGIS and Marting, running on docker.

[Martin](https://github.com/urbica/martin) is a [PostGIS](https://github.com/postgis/postgis) [vector tiles](https://github.com/mapbox/vector-tile-spec) server suitable for large databases.

## Set up

#### Databases

In a command line window, run the following command to set up Martin and PostGIS:
```
docker-compose up
```
> Martin will be running on port 3000 by default


#### Django

Set the env vars on your environment defined in `local.env` and then run:
```
python manage.py runserver 0.0.0.0:8000
```


## How to use

1. Start the project and access to the django admin dashboard (localhost:8000)

2. Create a Country instance

3. Navigate to `http://localhost:8000/test/leaflet/`


## Import data
```
python manage.py import world
```