from flask import Flask, request, make_response, jsonify
from requests_yaml_parser import sim
import operator
import time
import random
import logging
logging.basicConfig(level='WARNING')


class NotDefinedRequest(Exception):
    pass


app = Flask(__name__)


i = 0
for path in sim.requests:
    def func_t():
        req = sim.requests[path]
        t_reqs = req[request.method]
        for t_req in t_reqs:
            if request.method == 'GET':
                body = request.args.to_dict()
            elif request.method == 'POST':
                if request.headers.get('Content-Type') == 'application/json':
                    body = request.get_json()
                else:
                    body = request.get_data()
            req_body = t_req.get('req_body', None)
            if req_body is None:
                req_body = {}
            if operator.eq(body, req_body):
                time.sleep(random.uniform(t_req.get('latency_min', 0), t_req.get('latency_max', 0)))
                response = jsonify(t_req.get('res_body', None))
                for h in t_req.get('res_headers'):
                    response.headers[h] = t_req['res_headers'][h]
                return response
        error_str = 'Request Path: {}, Request Method: {}, Request Body: {}'
        raise NotDefinedRequest(error_str.format(path, request.method, request.args if request.method == "GET"
                                else request.get_json() if request.method == "POST"
                                and request.headers.get("Content-Type") == "application/json"
                                else request.get_data()))

    func_t.__name__ += str(i)
    methods = [method for method in sim.requests[path]]
    app.route(path, methods=methods)(func_t)
    i += 1


@app.before_request
def f():
    logging.info(request.get_json())


@app.after_request
def p(response):
    logging.info(response.get_json())
    return response


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
