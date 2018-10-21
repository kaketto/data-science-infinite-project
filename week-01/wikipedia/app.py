import requests as requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

url = 'https://en.wikipedia.org/w/api.php'
# contentUrl = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=';

@app.route("/", methods= ['GET'])
@app.route("/search", methods= ['POST'])
def wiki():
    if request.method == 'POST':
        search_for = request.form['search-term']
        # parameters = {"action": "query", "list": "search", "format": "json", "srsearch": search_for, "prop": "extract"}
        parameters = {"action": "opensearch", "format": "json", "search": search_for}
        response = requests.get(url, params = parameters)
        search_result = response.json() #['query']['search']
        number_of_results = len(search_result[1])
        # print(search_result)
    else:
        search_result = ''
        number_of_results = 0
    return render_template('wiki.html', result=search_result, number=number_of_results)

if __name__ == '__main__':
    app.run(debug=True)
