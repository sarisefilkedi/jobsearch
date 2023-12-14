from flask import Blueprint, render_template, request, jsonify
import requests

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/search', methods=['GET'])
def search_jobs():
    industry = request.args.get('industry')
    country = request.args.get('country')
    updated_since = request.args.get('updated_since')

    # CoreSignal API endpoint for LinkedIn company search with filters
    api_url = 'https://api.coresignal.com/cdapi/v1/linkedin/company/search/filter'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJFZERTQSIsImtpZCI6ImM2MGY3NmIzLTBlOTYtMzM2NS1iN2UxLTdmYzBlYjUzYzk0OSJ9.eyJhdWQiOiJxbXVsIiwiZXhwIjoxNzM0MTA5MDE3LCJpYXQiOjE3MDI1NTIwNjUsI>
    }

    # Prepare the payload with filters
    payload = {
        "filter": {
            "industry": industry,
            "country": country,
            "updated_at": {"gte": updated_since}
        },
        "size": 4  # Limiting the number of results to 4
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        companies_data = response.json()
        top_companies = companies_data.get('data', [])  # Extract the data
        return render_template('search_results.html', companies=top_companies)
    else:
        return jsonify({"error": "API request failed"}), response.status_code


