# Flask - REST API Project

[![License](https://img.shields.io/badge/License-Apache-yellow.svg)](https://opensource.org/license/apache-2-0)

This is a project of the course "Application Development using Microservices and Serverless" by IBM as part of IBM DevOps Certificate.

### Description

This project consist on create a Product's list using a Flask Server. The application executes CRUD operations (Create, Retrieve, Update, and Delete) through the REST API endpoints in the Flask server.

### Usage

In order to execute this applications install the necessaries packahes to run it:

python3 -m pip install flask flask_cors
python3 products.py # run the python server 

Use curl to serve the REST API endpoints.
curl http://localhost:5000/products

To add a product (POST request) curl also be used:
curl -X POST -H "Content-Type: application/json" \
    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
    http://localhost:5000/products

To verify the added product:
curl http://localhost:5000/products/145

Another way to use this applications, is to run the python server and use the Postman app to executes the CRUD operations on the REST API.

### License

Copyright (c) 2024, Guilherme Oliveira. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)
