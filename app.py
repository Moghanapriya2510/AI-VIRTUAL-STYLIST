from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data for Kurti Sets and Black Shirts
with open('kurti_sets.json', 'r') as file:
    kurti_sets = json.load(file)["kurtiSets"]

with open('black_shirt.json', 'r') as file:
    black_shirts = json.load(file)["BlackShirt"]
with open('saree.json','r') as file:
    saree =json.load(file)["Saree"]
with open('lehenga.json','r') as file:
    lehenga = json.load(file)["Lehenga"]
with open('casual_wear_for_women.json','r') as file:
    casual_wear_for_women=json.load(file)["Casual_wear_for_women"]
with open('pink_kurti.json','r') as file:
    pink_kurti=json.load(file)["pink_kurti"]
with open('blue_kurti.json','r') as file:
    blue_kurti=json.load(file)["blue_kurti"]
with open('skirt.json','r') as file:
    skirt=json.load(file)["skirt"]
with open('chiffon.json','r') as file:
    chiffon=json.load(file)["chiffon"]
with open('shoes_for_women.json','r') as file:
    shoes_for_women=json.load(file)["shoes_for_women"]
with open('accessories_for_women.json','r') as file:
    accessories_for_women=json.load(file)["accessories_for_women"]

@app.route('/')
def home():
    # This will render an HTML file, make sure you have a 'home.html' in the 'templates' folder.
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query', '').lower()

    if 'normal kurti' in user_query or 'kurta set' in user_query:
        response = {"suggestions": kurti_sets}
    elif 'black shirt' in user_query or 'shirt' in user_query:
        response = {"suggestions": black_shirts}
    elif 'saree' in user_query or 'give me saree' in user_query:
        response = {"suggestions": saree}
    elif 'lehenga' in user_query or 'give me lehenga' in user_query:
        response={"suggestions": lehenga}
    elif 'casual wear for women' in user_query:
        response={"suggestions":casual_wear_for_women}
    elif 'pink kurti' in user_query or 'give me pink kurti' in user_query:
        response = {"suggestions":pink_kurti}
    elif 'blue kurti' in user_query or 'give me blue kurti' in user_query:
        response={"suggestions":blue_kurti}
    elif 'skirt' in user_query or 'give me long skirt' in user_query:
        response={"suggestions":skirt}
    elif 'chiffon' in user_query or 'give me chiffon' in user_query:
        response={"suggestions":chiffon}
    elif 'shoes for women' in user_query or 'women shoes' in user_query:
        response={"suggestions":shoes_for_women}
    elif 'accessories for women' in user_query :
        response={"suggestions":accessories_for_women}
    else:
        response = {"suggestions": "Sorry, I don't have any suggestions for your query."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
