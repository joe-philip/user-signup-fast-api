## User Signup APP
#### Setup
1. Create virtual environment `python -m venv env`
2. Activate virtual environment `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Setup `.env`
```
DATABASE_URL=postgresql://{user}:{password}@{host}:{port}/{db}
```
5. Run app `uvicorn main:app`