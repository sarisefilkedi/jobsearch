from flask import Flask, Blueprint, render_template, request, jsonify, json
import requests

# Create a Flask application
app = Flask(__name__)

# Define your search Blueprint
search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/search', methods=['GET', 'POST'])
def search_companies():
    companies = []
    if request.method == 'GET':
        industry = request.args.get('industry')
        country = request.args.get('country')
        last_updated_gte = request.args.get('last_updated_gte')

        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = "eyJhbGciOiJFZERTQSIsImtpZCI6ImM2MGY3NmIzLTBlOTYtMzM2NS1iN2U1LTdmYzBlYjUzYzk0OSJ9.eyJhdWQiOiJxbXVsI..."

        # Replace 'API_ENDPOINT' with the actual API URL
        api_url = 'https://api.coresignal.com/cdapi/v1/linkedin/company/search/filter'

        # Set up headers with the API key
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        params = {
            'industry': industry,
            'country': country,
            'last_updated_gte': last_updated_gte
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.ok:
            companies = response.json()  # Parse the response data

    return render_template('search.html', companies=companies)

# Register the search Blueprint
app.register_blueprint(search_blueprint)


