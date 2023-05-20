# Fetching function from ___init__.py hwich is inside the website(package) folder
from website import create_app

app = create_app()

if __name__ == '__main__': # Website will run ONLY if you run this file(main.py)
  app.run(host = '0.0.0.0', debug=True) 
# Host = '0.0.0.0' ensure that the programe runs locally 
# debug=true should be on during development only. When webiste is live this should be off as chnage to the code will restart the web server