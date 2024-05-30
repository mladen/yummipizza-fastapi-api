# API for Yummi Pizza test project (done 4 years ago in Laravel) redone using FastAPI

## Installation

1. Clone the repository

```bash
$ git clone <repo-url> # clones this repository
$ cd <repo-dir> # change to the repository directory
```

3. Create a virtual environment

```bash
$ python3 -m venv venv # creates a virtual environment
$ source venv/bin/activate # starts the virtual environment on Unix
# on Windows, use `venv\Scripts\activate` to start the virtual environment
```

4. Install the requirements

```bash
$ pip install -r requirements.txt # installs the requirements
```

5. Run the server

```bash
$ uvicorn main:app --reload --port 5000 # starts the server
# or
# $ uvicorn main:app --reload
```

## API Endpoints

1. `/api/meals` - GET - Fetches all the meals

### Usage

Open your browser and navigate to `http://localhost:5000/api/meals` ` to view the list of meals

## Frontend

The frontend for this project is available at [yummipizza-front](https://github.com/mladen/yummipizza-front)
