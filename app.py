from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = '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'

# Route for the Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for Ask StudyBuddy
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # Get the question from the request
        data = request.json
        question = data.get('question')

        # Call OpenAI API to generate the answer
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can change this to a different model if needed
                prompt=question,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
        except Exception as e:
            answer = "Sorry, something went wrong while processing your question."

        # Return the answer as JSON
        return jsonify({'answer': answer})
    
    return render_template('ask.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
