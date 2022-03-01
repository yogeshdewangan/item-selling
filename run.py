from market import app
import os

# Checks if the run.py file has executed directly and not imported
# Run below commands to run the application in debug mode
#docker build . -t flask_app_dev
#docker run -p 5070:5000 -e DEBUG=1 flask_app_dev
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5070, debug=os.environ.get('DEBUG') == '1')
