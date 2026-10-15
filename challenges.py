
# ----------------------------------------
# DIGITAL DETECTIVE
# PHASE 6 - INVESTIGATION CHALLENGES
# ----------------------------------------

# Each challenge contains a question,
# possible answers, the correct answer,
# an explanation, and points.

challenges = {

    "1": {
        "title": "Suspicious Login Activity",

        "question": (
            "A successful login occurred at 2:43 AM "
            "from an external network. What does "
            "this suggest?"
        ),

        "options": [
            "The account owner definitely committed the breach",
            "Someone may have accessed the account without authorization",
            "The database administrator deleted the records",
            "The university network was operating normally"
        ],

        "correct_answer": 1,

        "explanation": (
            "An unusual external login can indicate "
            "unauthorized access. However, it does not "
            "prove who was using the account."
        ),

        "points": 10
    },

    "2": {
        "title": "Compromised Employee Account",

        "question": (
            "The security report identifies a former "
            "employee account as compromised. "
            "What should investigators do next?"
        ),

        "options": [
            "Immediately arrest the former employee",
            "Ignore the report",
            "Compare account records with login activity",
            "Delete the compromised account records"
        ],

        "correct_answer": 2,

        "explanation": (
            "Investigators should compare independent "
            "sources of evidence before determining "
            "who was responsible."
        ),

        "points": 10
    },

    "3": {
        "title": "Digital Evidence Integrity",

        "question": (
            "Why is preserving digital evidence "
            "important during a cybercrime investigation?"
        ),

        "options": [
            "To ensure the evidence remains reliable",
            "To make the investigation more complicated",
            "To prevent investigators from reviewing logs",
            "To increase the number of suspects"
        ],

        "correct_answer": 0,

        "explanation": (
            "Digital evidence must be preserved to "
            "maintain its reliability and support "
            "the investigation."
        ),

        "points": 10
    },

    "4": {
        "title": "Identifying the Strongest Evidence",

        "question": (
            "Which combination of evidence would "
            "best help investigators understand "
            "the unauthorized login?"
        ),

        "options": [
            "A suspect's job title alone",
            "Only the suspicious email",
            "Only the employee's name",
            "Server logs, IP records, and account records"
        ],

        "correct_answer": 3,

        "explanation": (
            "Comparing server logs, IP addresses, "
            "and employee account records provides "
            "a more complete picture of the incident."
        ),

        "points": 10
    }
}


# ----------------------------------------
# CHECK A CHALLENGE ANSWER
# ----------------------------------------

def check_answer(challenge_id, selected_answer):

    challenge = challenges[challenge_id]

    if selected_answer == challenge["correct_answer"]:
        return True

    return False


# ----------------------------------------
# COUNT CHALLENGES
# ----------------------------------------

def get_total_challenges():

    return len(challenges)


# ----------------------------------------
# CALCULATE CHALLENGE POINTS
# ----------------------------------------

def calculate_challenge_points(completed_challenges):

    total_points = 0

    for challenge_id in completed_challenges:

        total_points += challenges[challenge_id]["points"]

    return total_points
