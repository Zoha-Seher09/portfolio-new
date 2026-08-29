from flask import Flask, render_template, request
import requests

GITHUB_USERNAME = "Zoha-Seher09"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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

    interests_list = [
        "Open Source Contribution",
        "Competitive Programming",
        "Reading Tech Blogs",
        "UI/UX Design"
    ]

    achievements_list = [
        {"title": "Hackathon Winner", "description": "1st place in university-level hackathon, 2025.", "year": "2025"},
        {"title": "Dean's List", "description": "Recognized for academic excellence across two semesters.", "year": "2024"},
    ]

    try:
        response = requests.get(
            f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
            params={"sort": "updated", "per_page": 6}
        )
        response.raise_for_status()
        repos = response.json()
        projects_list = [
            {
                "title": repo["name"],
                "description": repo["description"] or "No description provided.",
                "link": repo["html_url"],
                "stars": repo["stargazers_count"],
            }
            for repo in repos
            if repo["name"] != "portfolio-new"
        ]
    except requests.RequestException:
        projects_list = []

    submitted = False
    contact_name = None

    if request.method == "POST":
        contact_name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"New message from {contact_name} ({email}): {message}")
        submitted = True

    return render_template(
        "home.html",
        skills=skills_list,
        education=education_list,
        experience=experience_list,
        certifications=certifications_list,
        projects=projects_list,
        services=services_list,
        interests=interests_list,
        achievements=achievements_list,
        submitted=submitted,
        name=contact_name,
    )

if __name__ == "__main__":
    app.run(debug=True)