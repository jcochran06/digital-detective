

# ========================================
# DIGITAL DETECTIVE
# EVIDENCE CONNECTION SYSTEM
# PHASE 7 - FINAL VERSION
# ========================================


# ========================================
# EVIDENCE CONNECTION DATABASE
# ========================================

evidence_connections = {

    # ------------------------------------
    # CONNECTION 1
    # SERVER LOGS + EMPLOYEE RECORDS
    # ------------------------------------

    ("1", "3"): {
        "name": "Unauthorized Account Access",

        "explanation": (
            "Server logs show an unauthorized login at "
            "2:43 AM. Employee records reveal that a "
            "former employee account remained active. "
            "This explains how outdated credentials "
            "could have been used during the breach."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 2
    # SERVER LOGS + IP ADDRESS RECORDS
    # ------------------------------------

    ("1", "4"): {
        "name": "Remote Database Access",

        "explanation": (
            "Server logs identify the time of the breach, "
            "while IP address records show that the login "
            "originated outside the university network. "
            "This indicates the database was accessed remotely."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 3
    # SUSPICIOUS EMAIL + EMPLOYEE RECORDS
    # ------------------------------------

    ("2", "3"): {
        "name": "Password Reset Vulnerability",

        "explanation": (
            "A password reset notification was sent "
            "shortly before the breach, and employee "
            "records show that an outdated account "
            "remained active. Together, these clues "
            "suggest a possible account security weakness."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 4
    # EMPLOYEE RECORDS + SECURITY REPORT
    # ------------------------------------

    ("3", "5"): {
        "name": "Former Employee Account Identified",

        "explanation": (
            "Employee records and the security report "
            "identify Ryan Brooks' old account as the "
            "account used during the breach. However, "
            "account activity alone does not establish "
            "who was physically operating the system."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 5
    # SERVER LOGS + RECOVERED DEVICE
    # ------------------------------------

    ("1", "6"): {
        "name": "Recovered Breach Session",

        "explanation": (
            "Server logs record unauthorized access "
            "at 2:43 AM. Forensic examination of the "
            "recovered laptop identified the browser "
            "session used during that breach. "
            "This connects the device directly "
            "to the unauthorized database activity."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 6
    # IP ADDRESS RECORDS + RECOVERED DEVICE
    # ------------------------------------

    ("4", "6"): {
        "name": "Remote Access Investigation",

        "explanation": (
            "IP address records show that the breach "
            "originated from an external network. "
            "The recovered laptop contains the browser "
            "session associated with the breach. "
            "Together, these findings support further "
            "investigation of the device's network activity, "
            "although the available evidence does not "
            "establish an exact IP-to-device match."
        ),

        "points": 10
    },

    # ------------------------------------
    # CONNECTION 7
    # SECURITY REPORT + RECOVERED DEVICE
    # ------------------------------------

    ("5", "6"): {
        "name": "Ryan Brooks Device Connection",

        "explanation": (
            "The security report identifies Ryan Brooks' "
            "former university account as the account "
            "used during the breach. Investigators also "
            "recovered a university-issued laptop retained "
            "by Ryan that contained the breach browser "
            "session, exported student records, and a "
            "message describing a plan to retrieve those "
            "records. These findings provide substantially "
            "stronger evidence connecting Ryan to the incident, "
            "although device access by another person "
            "remains a possibility."
        ),

        "points": 10
    }
}


# ========================================
# CHECK WHETHER TWO EVIDENCE FILES CONNECT
# ========================================

def check_connection(first_id, second_id):

    connection_key = tuple(
        sorted([first_id, second_id])
    )

    if connection_key in evidence_connections:

        return evidence_connections[connection_key]

    return None


# ========================================
# COUNT TOTAL AVAILABLE CONNECTIONS
# ========================================

def get_total_connections():

    return len(evidence_connections)


# ========================================
# GET DISCOVERED CONNECTIONS
# ========================================

def get_discovered_connections(collected_connections):

    discovered = []

    normalized_connections = {
        tuple(sorted(connection))
        for connection in collected_connections
    }

    for connection_key, connection in evidence_connections.items():

        if connection_key in normalized_connections:

            discovered.append(connection)

    return discovered
