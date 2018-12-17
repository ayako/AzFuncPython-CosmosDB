import logging

import azure.functions as func
from ..SharedScripts import cosmos


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    database = req.params.get('database')
    container = req.params.get('container')
    if not database:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            database = req_body.get('database')
    if not container:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            container = req_body.get('container')

    if database is not None and container is not None:
        msg = cosmos.CountDocuments(database,container)
        return func.HttpResponse(
            msg,
            status_code=200
        )
    else:
        return func.HttpResponse(
             "Please pass database and container name on the query string or in the request body",
             status_code=400
        )
