# COMP 3005 Assignment 3 Question 1

## Files

* `.gitignore` - ignores local repository preferences.
* `README.md` - readme.
* `requirements.md` - the assignment requirements, in markdown.
* `setup.sql` - sql file to create and insert into database
  * It doesn't seem as though this has to be as part of my application (Python script), so I kept it as an SQL file.
* `script.py` - the Python script file containing all the instructions.

## Run Instructions

### 1. Prequisites

1. `Python3`
2. `Pip3`

### 2. Setup Database

1. run the `setup.sql` in a Postgres DB.

### 3. Run

```bash
git clone https://www.github.com/HamzaAlsarakbi/comp3005a3q1
cd comp3005a3q1
pip3 install psycopg
python3 script.py
```
