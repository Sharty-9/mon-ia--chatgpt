from flask import Flask, request, render_template_string
from groq import Groq

app = Flask(__name__)
client = Groq(api_key="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")

# Design simple pour ton site
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Mon IA Perso</title></head>
<body style="font-family:sans-serif; padding:20px; background:#f4f4f4;">
    <h2>Chat avec mon IA</h2>
    <div id="chatbox" style="background:white; padding:15px; height:300px; overflow-y:scroll; border:1px solid #ccc;">
        {{ response }}
    </div>
    <form method="POST" style="margin-top:10px;">
        <input type="text" name="msg" style="width:70%; padding:10px;" placeholder="Posez une question...">
        <button type="submit" style="padding:10px;">Envoyer</button>
    </form>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    response = "Posez-moi n'importe quoi !"
    if request.method == "POST":
        user_msg = request.form.get("msg")
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_msg}]
        )
        response = chat_completion.choices[0].message.content
    return render_template_string(HTML_PAGE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
