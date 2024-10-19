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
        elif "when was disney founded?" in user_input:
            return "The Walt Disney Company was founded on October 16, 1923."
        elif "lion king" in user_input:
            return "The Lion King was released on June 15, 1994."
        elif "mulan 2" in user_input:
            return "Mulan 2 was released on December 28, 2004."
        elif "mulan" in user_input:
            return "Mulan was released on June 5, 1998."
        elif "aladdin 1" in user_input:
            return "Aladdin was released on November 25, 1992."
        elif "aladdin 2" in user_input:
            return "Aladdin 2 was released on May 20, 1994."
        elif "aladdin 3" in user_input:
            return "Aladdin 3 was released on August 13, 1996."
        elif "founder" in user_input:
            return "The Walt Disney Company was founded by Walt Disney and Roy O. Disney."
        elif "ceo" in user_input:
            return "The current CEO of The Walt Disney Company is Bob Iger."
       
# Create Flask app
app = Flask(__name__)
chatbot = DisneyChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
