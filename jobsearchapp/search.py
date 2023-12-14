from flask import Blueprint, render_template, request
import requests

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/search', methods=['GET', 'POST'])
def search_jobs():
    jobs = []
    if request.method == 'POST':
        job_title = request.form.get('job_title')
        # Replace 'API_ENDPOINT' with the actual API URL and add necessary parameters
        response = requests.get('API_ENDPOINT', params={'title': job_title})
        if response.ok:
            jobs = response.json()  # Parse the response data
    return render_template('search.html', jobs=jobs)
