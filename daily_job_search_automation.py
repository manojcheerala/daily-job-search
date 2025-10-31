"""
Daily Job Search Automation Script
----------------------------------
This script searches the web every day for internship / apprenticeship / entry-level
Software and Data jobs at top companies and emails you the results.
"""

import os
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime

# ============ CONFIGURATION ============
BING_API_KEY = os.environ.get("BING_API_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL_TO = os.environ.get("EMAIL_TO") or EMAIL_USER

# Top companies/startups to look for
COMPANIES = [
    "Google", "Microsoft", "Amazon", "Meta", "Apple", "Zoho",
    "Flipkart", "Swiggy", "Zomato", "Razorpay", "Infosys",
    "TCS", "Wipro", "HCL", "Cognizant", "Paytm", "Freshworks"
]

# ============ MAIN LOGIC ============
def search_jobs():
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    results = []

    for company in COMPANIES:
        query = f"{company} internship OR apprentice OR entry level software OR data site:linkedin.com OR site:internshala.com"
        url = "https://api.bing.microsoft.com/v7.0/search"
        params = {"q": query, "count": 5}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=15)
            data = response.json()
            for item in data.get("webPages", {}).get("value", []):
                results.append({
                    "company": company,
                    "title": item.get("name"),
                    "link": item.get("url"),
                    "desc": item.get("snippet")
                })
        except Exception as e:
            print(f"Error fetching for {company}: {e}")

    return results


def send_email(jobs):
    if not EMAIL_USER or not EMAIL_PASS:
        raise ValueError("Please set EMAIL_USER and EMAIL_PASS as environment variables.")

    msg = EmailMessage()
    msg["Subject"] = f"Daily Job Search Results - {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    if not jobs:
        msg.set_content("No jobs found today.")
    else:
        lines = []
        for j in jobs:
            lines.append(f"[{j['company']}] {j['title']}\n{j['link']}\n{j['desc']}\n")
        msg.set_content("\n\n".join(lines))

    # Send email via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        print("Email sent successfully.")


if __name__ == "__main__":
    print("Fetching daily job listings...")
    jobs = search_jobs()
    send_email(jobs)
