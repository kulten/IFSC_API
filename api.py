from flask import Flask, request, jsonify, make_response, abort
from flask_restful import Resource, Api
import psycopg2
import logging
import datetime
import jwt

logging.basicConfig(level=logging.WARNING,
                    filename="api_log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecret"
api = Api(app)
try:
    logging.info("Connecting to database")
    connection = psycopg2.connect(host="localhost",
                                  database="ifsc_db",
                                  port=5432,
                                  user="postgres",
                                  password="test1")
    cursor = connection.cursor()
except Exception as db_connection_error:
    logging.error(db_connection_error)


def _retrieve_data(city, bank_name, limit, offset):
    """
    Pick the correct select query based on the provided parameters
    :param city:
    :param bank_name:
    :param limit:
    :param offset:
    :return:
    """
    if limit is None and offset is None:
        cursor.execute("Select * from bank_branches where city = %s and bank_name = %s", (city, bank_name))
    elif limit is None and offset is not None:
        cursor.execute("Select * from bank_branches where city = %s and bank_name = %s offset %s",
                       (city, bank_name, offset))
    elif limit is not None and offset is None:
        cursor.execute("Select * from bank_branches where city = %s and bank_name = %s limit %s",
                       (city, bank_name, limit))
    else:
        cursor.execute("Select * from bank_branches where city = %s and bank_name = %s limit %s offset %s",
                       (city, bank_name, limit, offset))
    bank_data = cursor.fetchall()
    return bank_data


def _validate_numeric_values(limit, offset):
    error_str = "The following fields have invalid values: "
    valid = True
    if limit is not None:
        try:
            int(limit)
        except:
            error_str += "limit, "
            valid = False
    if offset is not None:
        try:
            int(offset)
        except:
            error_str += "offset"
            valid = False
    return valid, error_str


def validate_token():
    token = request.args.get("token", None)
    if token is None:
        abort(401)
    try:
        data = jwt.decode(token, app.config["SECRET_KEY"])
    except:
        abort(401)
    return


class BankAPI(Resource):
    """
    URI to select a bank's details based on the provided IFSC code
    Parameters: ifsc_code
    """
    def get(self):
        validate_token()
        ifsc_code = request.args.get("ifsc_code", None)
        if ifsc_code is None:
            logging.warning("parameter ifsc_code is not provided or is invalid")
            return abort(401)
        ifsc_code = ifsc_code.upper()
        try:
            cursor.execute("Select * from bank_branches where ifsc = %s", (ifsc_code, ))
            bank_data = cursor.fetchall()
            if bank_data:
                return jsonify(bank_data)
            else:
                return jsonify({"Message: ": "No data found for the given parameters"})
        except Exception as ifsc_query_error:
            logging.error(ifsc_query_error)
            return abort(500)


class BranchAPI(Resource):
    """
    URI to select details of all branches of a bank in a given city.
    Parameters: limit, offset, city, bank_name.
    """
    def get(self):
        validate_token()
        city = request.args.get("city", None)
        bank_name = request.args.get("bank_name", None)
        limit = request.args.get("limit", None)
        offset = request.args.get("offset", None)
        if city is None or bank_name is None:
            logging.warning("One or more provided parameters is missing or invalid")
            return make_response({"Message: ": "One or more provided parameters is missing or invalid"}, 401)
        valid, error_str = _validate_numeric_values(limit, offset)
        if not valid:
            logging.warning(error_str)
            return make_response({"Message: ": error_str}, 401)
        city = city.upper()
        bank_name = bank_name.upper()
        try:
            bank_data = _retrieve_data(city, bank_name, limit, offset)
            if bank_data:
                return jsonify(bank_data)
            else:
                return jsonify({"Message: ": "No data found for the given parameters"})
        except Exception as branch_query_error:
            logging.error(branch_query_error)
            return abort(500)


class Login(Resource):
    """
    URI to get the authentication token, choose any username but password must be 1234asdf.
    """
    def get(self):
        auth = request.authorization
        if not auth:
            return jsonify({"Message: ":
                            "You need to send username and password in a curl command to get the authentication token from this URI"})
        if auth and auth.password == "1234asdf":
            token = jwt.encode({"username": auth.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=5)},
                                app.config["SECRET_KEY"])
            return jsonify({"Token: ": token.decode("UTF-8")})
        else:
            return make_response("Verification failed! :)", 401)


api.add_resource(BankAPI, "/bank_detail")
api.add_resource(BranchAPI, "/branch_detail")
api.add_resource(Login, "/")

if __name__ == "__main__":
    app.run(debug=True)
