**Flask Micro-API**
A small Flask API that returns JSON data and demonstrates GET and POST requests

*Endpoints*
- GET /hello -- returns a welcom message
- GET /data -- returns sample course and topic data
- POST /data -- accepts JSON and returns the submitted data

*Run the app*
activate your virtual environment, install the requirements, and start Flask:

- python -m pip install -r requirements.txt
- python app.py

the API runs at http://127.0.0.1:5000

*Test the API*
with the server running, open a second terminal and run:
- python test_api.py

the script checks both GET endpoints and sends a POST request with sample JSON

*Agile Process*
I built the API in small steps: first setting up the base of the project, second I added and checked the GET routes, third I added POST handling, and finally I ran the requests script and fixed errors I found during testing