from flask import Flask, request, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)  # allow frontend to call backend

# Temporary storage (later we can use DB)
contact_requests = []

@app.route("/api/contact", methods=["POST"])
def save_contact():
    data = request.json

    contact_requests.append({
        "name": data.get("name"),
        "mobile": data.get("mobile"),
        "email": data.get("email"),
        "message": data.get("message")
    })

    return jsonify({
        "status": "success",
        "message": "Contact request saved successfully"
    })


@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    return jsonify(contact_requests)


# 🔹 ADD THIS NEW ADMIN TABLE ROUTE HERE
@app.route("/admin/contacts", methods=["GET"])
def admin_contacts():
    html = """
    <html>
    <head>
        <title>Contact Requests</title>
        <style>
            body { font-family: Arial; padding: 40px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 10px; }
            th { background: #0f172a; color: white; }
            tr:nth-child(even) { background: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2>Contact Requests</h2>
        <table>
            <tr>
                <th>Row</th>
                <th>Name</th>
                <th>Mobile</th>
                <th>Email</th>
                <th>Message</th>
            </tr>
    """

    for index, req in enumerate(contact_requests, start=1):
        html += f"""
        <tr>
            <td>{index}</td>
            <td>{req['name']}</td>
            <td>{req['mobile']}</td>
            <td>{req['email']}</td>
            <td>{req['message']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html


if __name__ == "__master__":
    port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
