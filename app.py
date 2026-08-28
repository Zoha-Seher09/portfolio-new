from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    skills_list = [
        "Python", "Flask", "JavaScript", "HTML/CSS",
        "Git & GitHub", "SQL", "REST APIs", "Problem Solving"
    ]
    
    education_list = [
        {
            "level": "Graduation (BS/BSc)",
            "institute": "Your University Name",
            "years": "2022 – 2026",
            "details": "Major subject, notable coursework, or achievements."
        },
        {
            "level": "Intermediate (FSc/ICS)",
            "institute": "Your College Name",
            "years": "2020 – 2022",
            "details": "Pre-Engineering / ICS / whichever group you studied."
        }
    ]
    
    experience_list = [
        {
            "role": "Your Job Title",
            "company": "Company Name",
            "years": "2025 – Present",
            "details": "What you did, technologies used, key achievement."
        }
    ]
    
    certifications_list = [
        {"name": "Certification Name", "issuer": "Issuing Platform", "year": "2025", "link": "https://credential-link.com"}
    ]
    
    services_list = [
        {"title": "Web Development", "description": "Building websites and web apps with Flask/Python."},
        {"title": "API Integration", "description": "Connecting apps to third-party services and APIs."},
        {"title": "Bug Fixing & Maintenance", "description": "Debugging and improving existing codebases."}
    ]

    return render_template(
        "home.html", 
        skills=skills_list, 
        education=education_list, 
        experience=experience_list, 
        certifications=certifications_list, 
        services=services_list
    )

@app.route("/projects")
def projects():
    projects_list = [
        {"title": "Project One", "description": "What it does.", "link": "https://github.com/you/project1"},
        {"title": "Project Two", "description": "What it does.", "link": "https://github.com/you/project2"}
    ]
    return render_template("projects.html", projects=projects_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"New message from {name} ({email}): {message}")[cite: 1, 2]
        return render_template("contact.html", submitted=True, name=name)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)[cite: 1, 2]