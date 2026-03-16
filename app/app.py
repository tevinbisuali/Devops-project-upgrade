from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Production Flask App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            color: white;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
            padding: 40px 20px;
        }

        .hero {
            text-align: center;
            padding: 70px 20px 40px;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 15px;
            color: #f8fafc;
        }

        .hero p {
            font-size: 1.2rem;
            color: #cbd5e1;
            max-width: 700px;
            margin: auto;
            line-height: 1.7;
        }

        .badge {
            display: inline-block;
            margin-bottom: 20px;
            background: #22c55e;
            color: #0f172a;
            padding: 8px 16px;
            border-radius: 999px;
            font-weight: bold;
            font-size: 0.9rem;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 50px;
        }

        .card {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 25px;
            backdrop-filter: blur(8px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35);
        }

        .card h3 {
            margin-bottom: 12px;
            color: #38bdf8;
        }

        .card p {
            color: #e2e8f0;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .footer {
            text-align: center;
            margin-top: 60px;
            color: #94a3b8;
            font-size: 0.95rem;
        }

        .highlight {
            color: #22c55e;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.2rem;
            }

            .hero p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <section class="hero">
            <div class="badge">Live on Azure</div>
            <h1>Production-Style Flask DevOps Project by Tevin Bis</h1>
            <p>
                This Flask application is deployed on a Linux virtual machine using
                <span class="highlight">Gunicorn</span>,
                <span class="highlight">Nginx</span>,
                <span class="highlight">systemd</span>,
                <span class="highlight">Terraform</span>,
                and <span class="highlight">GitHub Actions</span>.
            </p>
        </section>

        <section class="cards">
            <div class="card">
                <h3>Infrastructure</h3>
                <p>
                    Azure resources are provisioned using Terraform with reusable variables
                    and a cleaner production-style project structure.
                </p>
            </div>

            <div class="card">
                <h3>Deployment</h3>
                <p>
                    The app runs with Gunicorn behind Nginx, giving you a more realistic
                    setup than the default Flask development server.
                </p>
            </div>

            <div class="card">
                <h3>Automation</h3>
                <p>
                    GitHub Actions helps automate testing and deployment so every push
                    can move your project closer to production readiness.
                </p>
            </div>

            <div class="card">
                <h3>Security</h3>
                <p>
                    Basic security practices include SSH keys, controlled ports, service
                    management with systemd, and better handling of secrets.
                </p>
            </div>
        </section>

        <div class="footer">
            Built with Flask • Styled for your DevOps portfolio • Ready for improvement
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
