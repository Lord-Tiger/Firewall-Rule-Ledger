# Firewall-Rule-Ledger - Summary Statement

Decided to do this specific web application as the deliverable because a big part of my job is to design and manage security policies, such as firewall policies. A lot of times we get requests with incomplete information, such as a source IP, destination IP but no specified services or applications, no description of the connection or its purpose and so on.
This application allows a requester (such as a system admin or an app owner) to submit a firewall rule request for review before implementation. The form has all the fields in place to make a proper request, the request can’t be completed without the required information, if the request comes complete the first time, there’s limited back and forth, limits delays and allows projects to proceed with less friction. 

This application features users and assigned roles:
- Requester
- Admin/Reviewer (implementer/approver/user manager)
- auditor (log viewer for compliance)

This application is based on Django, and I have used the dogapi lab as a guide for this application. It also allows for each rule request to be tracked, logged and audited. The requester can track his/her request, each request would have status attached to it such as:
- Submitted
- Under Review
- Requester Action Required
- Approved
- Rejected

# Installation & Getting Started
# Prerequisites:
- [Git / Github for Desktop](https://github.com/apps/desktop)
- [Python 3](https://www.python.org/downloads/)

# Installation:

1. Clone the repository:

Once the GitHub Desktop app has been installed, launch it then go to:
File >> Clone repository... >> URL >> https://github.com/Lord-Tiger/Firewall-Rule-Ledger.git (As the URL) >> Choose a Local path on your machine >> Clone
```bash
cd <The path where you cloned the repo to>
```
2. Install Django and the other dependencies:
```bash
pip install -r requirements.txt
```
3. Create the database tables:
```bash
python manage.py migrate
```

# Getting Started
```bash
python manage.py runserver
```
Then open http://127.0.0.1:8000/api/requests/ in a browser or Postman.

Note: I'll be updating these instructions later once I get this dockerized in the final release, doing so might even make the installation process even easier since you can have the Docker installation install Django too. I already have some docker files here but still not yet ready for that stage.

AI use:
Helped me in changing text format to md format since I wrote the text for the installation stories, mockups etc. on my local machine in a Word document (Word formatting such as bold, bullet points, etc.).

Citation(s):
https://pydevtools.com/handbook/reference/requirements/ (For the requirements.txt use)
