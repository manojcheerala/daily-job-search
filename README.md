# 💼 Daily Job Search Automation

A personal Python automation project that helps me stay updated with new **internships** and **entry-level roles** every day 🚀  

Instead of manually visiting job portals, this script automatically collects openings from selected **company career pages** and **job boards**, filters the relevant ones, and sends me a **daily email summary**.

---

## ⚙️ Tech Stack
- **Language:** Python  
- **Libraries:** BeautifulSoup, Requests, smtplib, schedule, email  
- **Automation:** GitHub Actions (CRON schedule)  
- **IDE:** VS Code  
- **Output:** Daily email with job listings  

---

## 🧩 How It Works
1. Fetches job data from predefined portals and company pages.  
2. Filters results for “Intern”, “Apprentice”, and “Entry Level” roles.  
3. Formats the data into an email-friendly layout.  
4. Sends the results to my inbox via Gmail SMTP.  
5. Runs automatically every day through GitHub Actions.

---

## 🗂️ Folder Structure
daily-job-search/
├── daily_job_search_automation.py # Main script
├── .github/
│ └── workflows/
│ └── job_search.yml # Automation workflow
└── README.md

yaml
Copy code

---

## ▶️ How to Run

**Run manually**
```bash
python daily_job_search_automation.py
Run automatically (GitHub Actions)

Push the repo to GitHub.

Add secrets:

EMAIL_USER

EMAIL_PASS

RECEIVER_EMAIL

Confirm CRON timing inside .github/workflows/job_search.yml.

GitHub Actions will trigger the script daily and email the results.

💡 Why I Built This
I made this project to automate my job search while preparing for placements.
It helps me get notified about new openings across top MNCs and startups without spending hours searching every day.

🚀 Future Ideas
Add LinkedIn & Internshala integration

Telegram or Discord notifications

Simple job analytics dashboard

👨‍💻 Author
Manoj Cheerala
📧 manojcheerala23@gmail.com
🔗 GitHub | LinkedIn

⭐ If you find this useful, feel free to star or fork this repo!
