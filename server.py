from flask import Flask, request, jsonify
from wiki import WikipediaHelper

class DisneyChatbot:
    def __init__(self):
        self.wiki_helper = WikipediaHelper()

    def respond(self, user_input):
        user_input = user_input.lower()
        if "film" in user_input:
            movie_name = user_input.split("om")[-1].strip()
            return self.wiki_helper.get_summary(movie_name)
        elif "företagsinfo" in user_input or "företagshistoria" in user_input:
            return self.wiki_helper.get_summary("The Walt Disney Company")
        else:
            return "Jag är inte säker på hur jag ska svara på det. Försök fråga om en Disney-film eller om företagsinfo."

# Create Flask app
app = Flask(__name__)
chatbot = DisneyChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
