
# DIGITAL DETECTIVE
# Digital Forensics Lab


# Simulated university login records
login_records = [
    {
        "user": "Alex Morgan",
        "time": "11:45 PM",
        "location": "University Network",
        "status": "Successful"
    },
    {
        "user": "Sarah Collins",
        "time": "12:15 AM",
        "location": "University Network",
        "status": "Successful"
    },
    {
        "user": "Ryan Brooks",
        "time": "2:35 AM",
        "location": "External Network",
        "status": "Failed"
    },
    {
        "user": "Ryan Brooks",
        "time": "2:43 AM",
        "location": "External Network",
        "status": "Successful"
    },
    {
        "user": "Alex Morgan",
        "time": "3:10 AM",
        "location": "University Network",
        "status": "Failed"
    }
]

# Identify suspicious login activity
def analyze_logins():

    suspicious_records = []

    for record in login_records:

        if record["location"] == "External Network":

            suspicious_records.append(record)

        elif record["status"] == "Failed":

            suspicious_records.append(record)

    return suspicious_records

# Count login attempts for each user
def count_login_attempts():

    attempts = {}

    for record in login_records:

        username = record["user"]

        if username not in attempts:
            attempts[username] = 0

        attempts[username] += 1

    return attempts

# Determine which users have suspicious activity
def identify_suspicious_users():

    suspicious_users = {}

    for record in login_records:

        username = record["user"]

        if username not in suspicious_users:
            suspicious_users[username] = 0

        if record["location"] == "External Network":
            suspicious_users[username] += 2

        if record["status"] == "Failed":
            suspicious_users[username] += 1

    return suspicious_users
