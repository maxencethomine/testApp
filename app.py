from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    # Exemple de script Python
    time.sleep(2)  # Simuler un délai
    return jsonify({"message": "Script exécuté avec succès!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)