# Capstone Casting Agency Project

## Motivation for project
I integrate my following skills through this capstone project. 

- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications

## Heroku Link
https://casting-agency-2020.herokuapp.com/

## Getting Started
### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

First ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
export FLASK_ENV=debug;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Casting Agency Specification
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Data Models
- Movie with attributes title and release date
- Actor with attributes name, age and gender
- Casting with attributes actor_id and movie_id

### Endpoints
- GET /actors, /movies and /casting
- POST /actors, /movies and /casting
- PATCH /actors, /movies/ and /casting
- DELETE /actors, /movies/ and /casting

### Roles
Casting Assistant
- has following permissions for actions. 
    - `get:movies`, `get:actors`, `get:casting`

Casting Director
- has following permissions for actions. 
    - `get:movies`, `get:actors`, `get:casting`
    - `post:actors`, `post:casting`
    - `patch:movies`, `patch:actors`, `patch:casting`
    - `delete:actors`, `delete:casting`

Executive Producer
- has following permissions for actions. 
    - `get:movies`, `get:actors`, `get:casting`
    - `post:movies`, `post:actors`, `post:casting`
    - `patch:movies`, `patch:actors`, `patch:casting`
    - `delete:actors`, `delete:actors`, `delete:casting`

### Authentication (bearer tokens)
Casting Assistant
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9Ea3pRVVV5UlRReE9UVTVNa1pFUkRNNE5ETXhNVE0xT1VWQk5Ua3hNVVF6UmpkRVJUTkNNQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1oZXVyaXN0aWMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmMyNGY5MTA4ODViMGNhNmE3MDgwZSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4ODc1OTI4NCwiZXhwIjoxNTg4NzY2NDg0LCJhenAiOiJ4N3ZYdzBZY1Z1a3VqeHRyZk9oblQzWTA0cnFaRENUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDpjYXN0aW5nIiwiZ2V0Om1vdmllcyJdfQ.heFxFPKRTQqH_Rv5YfuwwJbq-nIk7l2INfh3e9G9w_75jn8yJpQrBX4ApVLKXgEc0v4R-6sxNPDJX3oEe6w1AC8A5SgOXJCBEpg8S_UZOmvQD-aF7l3h2ybotYBRy9rSYQCwuKPR-Z_4guNtTVM3qWwR8Lppg78KJbfrNowbiK-kwCR9zmLrT5WLc0cj6rqsYzrQid49rxdVgd1Ds96uxdypU68r4NYfOKhgEbTgbh4wtARypDtcNEXJ4gvNqBEVtURhvI2x0mPBNgwe2eAHaQUCphUstCy6rKo4TIUVGNfE3teD9f4EXNNUfoId87w6K_YEIaDxrls_iw6e9e2q5g
```

Casting Director
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9Ea3pRVVV5UlRReE9UVTVNa1pFUkRNNE5ETXhNVE0xT1VWQk5Ua3hNVVF6UmpkRVJUTkNNQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1oZXVyaXN0aWMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYWQyMDdmNTRiMTRjMGMxMjZlNmU2MSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4ODc1OTQ0NSwiZXhwIjoxNTg4NzY2NjQ1LCJhenAiOiJ4N3ZYdzBZY1Z1a3VqeHRyZk9oblQzWTA0cnFaRENUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTpjYXN0aW5nIiwiZ2V0OmFjdG9ycyIsImdldDpjYXN0aW5nIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOmNhc3RpbmciLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6Y2FzdGluZyJdfQ.ZhWJ5-HZraGw7EVldjk0KklzHQT7x_zWs7u7g0JY-JD17UKd_pqASwDYZhFddvCgftt-gi_QaB2-Ek_jQHSvF5bj8neuDgPc-chkGwW5vY2h-ONNlkncyIlGMzNaFnKqBmRwIGw_8024lFyh2tjjDy0NpKIqSQCYF24ZpM-yddhh3uOVhN2rBgUnj2emB_ei2Mg63iM_Q4drQurxSR35ipSQnxsFXB9JZJTNaJss5COVA0a-ndL4aia0y4Jxqoe6fTDk14Apw9vikM5UR3s8m5qwPnC_JnNjlqZMjnd7pMfq9HAq2cBGXp_PlSXy-m_uiaoLSXp-8zoVpG-LpjralQ
```

Executive Producer
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9Ea3pRVVV5UlRReE9UVTVNa1pFUkRNNE5ETXhNVE0xT1VWQk5Ua3hNVVF6UmpkRVJUTkNNQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1oZXVyaXN0aWMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNTQzNzEwYjIzOTQzMTAxYTdjYWMyMiIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4ODc1OTU5MSwiZXhwIjoxNTg4NzY2NzkxLCJhenAiOiJ4N3ZYdzBZY1Z1a3VqeHRyZk9oblQzWTA0cnFaRENUaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTpjYXN0aW5nIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6Y2FzdGluZyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDpjYXN0aW5nIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmNhc3RpbmciLCJwb3N0Om1vdmllcyJdfQ.J5F8-Kp7-5UXpki3Ugqi2952BAMzDb1Ca9Z-jKiEtjvETpGqWaDFYlOBEZSz2Tr9pBANO4IgcAwXE8DDI747VT5HreCQSA1KTyiDzL7c4TwLuuG_VhMlaZTXTZEegbQ8bNKRP_o-CGd86OshRJYCY9fj_P0N7IZgoLTJILj1CdR3V-7gdLSsAln_74viX6p9ifD3y3gn7nxLDm7Vu7KiJ7oBNy1cXkU5RL_-yWz2MbK_SWJBjyPmY9NMSFBn3d02qQsNiK-UkfoirQ_wS2V0gSSBe8-xlRtMmgdzLBo7-XExMI7x1zAnd4d54IyylRjnMjnPyCv6XM2VmHX7lrYVzw
```

## Error Handling

Errors are returned as JSON objects in the following formats:

```
{
    'success': False,
    'error': 400,
    'message': "bad request"
}

or

{
    'code': 'unauthorized',
    'description': 'Permission not found.'
}
```

The API will return seven error types when requests fail:

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Sever Error

## Endpoints

### GET /movies

- General: Retrieve all movies.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of movies.
- Sample: `{{host}}/movies`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 29 Jan 2018 00:00:00 GMT",
            "title": "Black Panther"
        },
        {
            "id": 2,
            "release_date": "Wed, 28 Jun 2017 00:00:00 GMT",
            "title": "Spider-Man: Homecoming"
        },
        {
            "id": 3,
            "release_date": "Mon, 23 Apr 2018 00:00:00 GMT",
            "title": "Avengers: Infinity War"
        },
        {
            "id": 4,
            "release_date": "Wed, 27 Feb 2019 00:00:00 GMT",
            "title": "Captain Marvel"
        },
        {
            "id": 5,
            "release_date": "Sun, 14 Apr 2013 00:00:00 GMT",
            "title": "Iron Man 3"
        }
    ],
    "success": true
}
```

### GET /actors

- General: Retrieve all actors.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of actors.
- Sample: `{{host}}/actors`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "actors": [
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "name": "Chadwick Boseman"
        },
        {
            "age": 23,
            "gender": "male",
            "id": 2,
            "name": "Tom Holland"
        },
        {
            "age": 55,
            "gender": "male",
            "id": 3,
            "name": "Robert Downey Jr."
        },
        {
            "age": 35,
            "gender": "female",
            "id": 4,
            "name": "Scarlett Johansson"
        },
        {
            "age": 30,
            "gender": "female",
            "id": 5,
            "name": "Brie Larson"
        },
        {
            "age": 47,
            "gender": "female",
            "id": 6,
            "name": "Gwyneth Paltrow"
        },
        {
            "age": 53,
            "gender": "male",
            "id": 7,
            "name": "Jon Favreau"
        }
    ],
    "success": true
}
```

### GET /casting

- General: Retrieve all casting.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of casting.
- Sample: `{{host}}/casting`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "casting": [
        {
            "actor_id": 1,
            "id": 1,
            "movie_id": 1
        },
        {
            "actor_id": 2,
            "id": 2,
            "movie_id": 2
        },
        {
            "actor_id": 3,
            "id": 3,
            "movie_id": 3
        },
        {
            "actor_id": 4,
            "id": 4,
            "movie_id": 3
        },
        {
            "actor_id": 5,
            "id": 5,
            "movie_id": 4
        },
        {
            "actor_id": 6,
            "id": 6,
            "movie_id": 3
        },
        {
            "actor_id": 6,
            "id": 7,
            "movie_id": 5
        },
        {
            "actor_id": 7,
            "id": 8,
            "movie_id": 5
        }
    ],
    "success": true
}
```

### POST /movies

- General: Create a new movie.
    - Permission: Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created movie.
- Sample: `{{host}}/movies`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "new_movie": {
        "id": 6,
        "release_date": null,
        "title": "The Incredible Hulk"
    },
    "success": true
}
```

### POST /actors

- General: Create a new actor.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created actor.
- Sample: `{{host}}/actors`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "new_actor": {
        "age": 50,
        "gender": "male",
        "id": 8,
        "name": "Edward Norton"
    },
    "success": true
}
```

### POST /casting

- General: Create a new casting.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created casting.
- Sample: `{{host}}/casting`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "new_casting": {
        "actor_id": 8,
        "id": 9,
        "movie_id": 1
    },
    "success": true
}
```

### PATCH /movies/{movie_id}

- General: Update a movie using a movie ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a movie to update.
    - Return: success value and a dictionary of the updated movie.
- Sample: `{{host}}/movies/5`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "success": true,
    "updated_movie": {
        "id": 5,
        "release_date": null,
        "title": "The Incredible Hulk2"
    }
}
```

### PATCH /actors/{actor_id}

- General: Update an actor using an actor ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of an actor to update.
    - Return: success value and a dictionary of the updated actor.
- Sample: `{{host}}/actors/5`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "success": true,
    "updated_actor": {
        "age": 100,
        "gender": "male",
        "id": 5,
        "name": "Edward Norton"
    }
}
```

### PATCH /casting/{casting_id}

- General: Update a casting using a casting ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a casting to update.
    - Return: success value and a dictionary of the updated casting.
- Sample: `{{host}}/casting/5`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "success": true,
    "updated_casting": {
        "actor_id": 1,
        "id": 5,
        "movie_id": 2
    }
}
```

### DELETE /movies/{movie_id}

- General: Delete a movie using a movie ID.
    - Permission: Executive Producer
    - Request Arguments: JWT token and an ID of a movie to delete.
    - Return: success value and the ID of a deleted movie.
- Sample: `{{host}}/movies/4`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "deleted_movie": 4,
    "success": true
}
```

### DELETE /actors/{actor_id}

- General: Delete an actor using an actor ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of an actor to delete.
    - Return: success value and the ID of a deleted actor.
- Sample: `{{host}}/actors/4`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "deleted_actor": 4,
    "success": true
}
```

### DELETE /casting/{casting_id}

- General: Delete a casting using a casting ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a casting to delete.
    - Return: success value and the ID of a deleted casting.
- Sample: `{{host}}/casting/4`
    - Please use postman collection `./casting-agency-2020.postman_collection.json`
```
{
    "deleted_casting": 4,
    "success": true
}
```

## Test on heroku
- Test the endpoints with Postman. 
    - Import the postman collection `./casting-agency-2020.postman_collection.json`
    - Run the collection.

- Database on heroku can be recreated by the following steps.
    - Run `heroku pg:psql`
    - Execute `TRUNCATE "Casting";`, `TRUNCATE "Movies" CASCADE;`, and `TRUNCATE "Actor" CASCADE;`
    - Exit heroku psql
    - Import data with `heroku pg:psql --app casting-agency-2020 postgresql-triangular-64018 < data.dump`

## Test on local
- Database on local can be created by the following steps.
    - Run `CREATE DATABASE agency_test;` to create a database for test.
    - Import data and database schema with `psql -U postgres agency_test < db.dump`

- Database on local can be recreated by the following steps.
    - Execute `TRUNCATE "Casting";`, `TRUNCATE "Movies" CASCADE;`, and `TRUNCATE "Actor" CASCADE;`
    - Import data and database schema with `psql -U postgres agency_test < data.dump`
    
- Test the endpoints by running `test_app.py`
    - Execute `source setup.sh`
    - Execute `py test_app.py`