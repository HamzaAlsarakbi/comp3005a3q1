# COMP 3005 Assignment 3 Question 1

## Demo

- [Demo](https://youtu.be/FaBMOyZv0p4)

## Files

* `.gitignore` - ignores local repository preferences.
* `README.md` - readme.
* `requirements.md` - the assignment requirements, in markdown.
* `setup.sql` - sql file to create and insert into database
  * It doesn't seem as though this has to be as part of my application (Python script), so I kept it as an SQL file.
* `script.py` - the Python script file containing all the instructions.

## Run Instructions

### 1. Prerequisites

1. `python3`
2. `pip3`

### 2. Setup Database

1. Open pgAdmin4
2. Create a new database named 'comp3005a3q1'
3. Run the `setup.sql` in a Postgres DB.

### 3. Run

```bash
git clone https://www.github.com/HamzaAlsarakbi/comp3005a3q1
cd comp3005a3q1
pip3 install psycopg2 tabulate
python3 script.py
```

## Troubleshooting

If your database username and password are not 'postgres', then update them in `script.py`