from market import app
import os

# Checks if the run.py file has executed directly and not imported
# Run below commands to run the application in debug mode
#docker build . -t flask_app_dev
#docker run -p 5070:5000 -e DEBUG=1 flask_app_dev
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5070, debug=os.environ.get('DEBUG') == '1')
    
    
'''
# item-selling

This project is to demostrate how to create a docker image of a flask web application and push the docker image to docker hub

add requirements.txt file in your project directory

flask
flask-sqlalchemy
flask_wtf
wtforms
email-validator
flask_bcrypt
flask_login
psycopg2


docker build . -t flask_app_dev
docker run -p 5070:5000 -e DEBUG=1 flask_app_dev

Try localhost:5000 in your browser


docker image
docker container commit <image_id> flask_app_dev:latest
docker image tag <image_id> <docker_hub_username>/flask_app_dev:latest
docker push docker_hub_username>/flask_app_dev

'''
