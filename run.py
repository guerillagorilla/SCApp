#!/usr/bin/python
from app import app

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=int("8080"))

