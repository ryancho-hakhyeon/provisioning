# Python application for the final exam (ACIT4640)

This application requires the following pip modules installed:
* Flask
* gunicorn
* requests

The application runs with gunicorn and Flask: `/path/to/gunicorn web:app`.
To make the application listen on all interfaces on port 7000, use: `/path/to/gunicorn web:app -b 0.0.0.0:7000`.

The application was created to serve requests on the `/final` endpoints: `/final/json` and `/final/image`. Make sure you forward them to the Python application if you are using a separate web service to serve the static content.

