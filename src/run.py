from src.app import app

__author='Dartaku'

app.run(port=5000, debug=app.config['DEBUG'])