
# ========================================
# DIGITAL DETECTIVE
# CASE 001 - THE UNIVERSITY DATA BREACH
# ========================================


# ========================================
# CASE INFORMATION
# ========================================

case_name = "The University Data Breach"

case_description = (
    "At approximately 2:43 AM, the university's student "
    "information database was accessed without authorization. "
    "Confidential student records may have been exposed. "
    "Investigators identified suspicious login activity, "
    "a password reset request, and an employee account "
    "that should have been disabled months earlier. "
    "Three individuals are connected to the case. "
    "Your job is to analyze the evidence, interview the "
    "suspects, and determine who is responsible."
)


# ========================================
# SUSPECT INFORMATION
# ========================================

suspects = {

    # ------------------------------------
    # SUSPECT 1 - ALEX MORGAN
    # ------------------------------------

    "1": {
        "name": "Alex Morgan",

        "role": "Student IT Employee",

        "interviews": {

            "1": {
                "question": "Where were you during the breach?",

                "answer": (
                    "I was finishing an overnight maintenance "
                    "shift in the university IT department. "
                    "I left shortly after 3:00 AM."
                )
            },

            "2": {
                "question": "Did you access the student database?",

                "answer": (
                    "I logged into the university network "
                    "to perform routine maintenance, but "
                    "I did not access confidential records."
                )
            },

            "3": {
                "question": "Did you notice anything unusual?",

                "answer": (
                    "I noticed a failed login attempt "
                    "associated with an account I did not "
                    "recognize. I assumed it was a system error."
                )
            }
        }
    },

    # ------------------------------------
    # SUSPECT 2 - SARAH COLLINS
    # ------------------------------------

    "2": {
        "name": "Sarah Collins",

        "role": "Database Administrator",

        "interviews": {

            "1": {
                "question": "Did you access the database that night?",

                "answer": (
                    "Yes. I performed a scheduled database "
                    "backup shortly after midnight."
                )
            },

            "2": {
                "question": "Who had access to the student records?",

                "answer": (
                    "Several IT employees had different levels "
                    "of access. Some older accounts were "
                    "supposed to be disabled after employees left."
                )
            },

            "3": {
                "question": "Were you aware of any security issues?",

                "answer": (
                    "I previously reported concerns about "
                    "inactive employee accounts remaining "
                    "enabled, but I do not know whether "
                    "the issue was fully resolved."
                )
            }
        }
    },

    # ------------------------------------
    # SUSPECT 3 - RYAN BROOKS
    # ------------------------------------

    "3": {
        "name": "Ryan Brooks",

        "role": "Former University Employee",

        "interviews": {

            "1": {
                "question": "When did you leave the university?",

                "answer": (
                    "I left approximately four months ago. "
                    "I believed my university account "
                    "had been disabled."
                )
            },

            "2": {
                "question": "Did you access the university system?",

                "answer": (
                    "No. I have not needed to access the "
                    "student database since leaving."
                )
            },

            "3": {
                "question": "Do you recognize the suspicious login?",

                "answer": (
                    "I received an unexpected password reset "
                    "notification recently, but I did not "
                    "request it. I ignored the message."
                )
            }
        }
    }
}


# ========================================
# DIGITAL EVIDENCE
# ========================================

evidence = {

    # ------------------------------------
    # EVIDENCE 1 - SERVER ACCESS LOGS
    # ------------------------------------

    "1": {
        "name": "Server Access Logs",

        "description": (
            "University server logs show a successful "
            "database login at 2:43 AM using credentials "
            "associated with a former employee account. "
            "The logs identify the account but not "
            "the physical person operating the device."
        ),

        "points": 10
    },

    # ------------------------------------
    # EVIDENCE 2 - SUSPICIOUS EMAIL
    # ------------------------------------

    "2": {
        "name": "Suspicious Email",

        "description": (
            "A password reset notification was sent "
            "to a former employee's email address "
            "approximately 30 minutes before the breach. "
            "Investigators have not confirmed who "
            "initiated the request."
        ),

        "points": 10
    },

    # ------------------------------------
    # EVIDENCE 3 - EMPLOYEE ACCESS RECORDS
    # ------------------------------------

    "3": {
        "name": "Employee Access Records",

        "description": (
            "Employee access records show that "
            "a former employee's university account "
            "remained active after their departure. "
            "The account retained permissions "
            "to access student information."
        ),

        "points": 15
    },

    # ------------------------------------
    # EVIDENCE 4 - IP ADDRESS RECORDS
    # ------------------------------------

    "4": {
        "name": "IP Address Records",

        "description": (
            "The unauthorized login originated "
            "from an external network rather than "
            "the university's internal network. "
            "The IP address has not yet been "
            "linked to a specific individual."
        ),

        "points": 15
    },

    # ------------------------------------
    # EVIDENCE 5 - SECURITY REPORT
    # ------------------------------------

    "5": {
        "name": "Security Report",

        "description": (
            "The university security team identified "
            "an outdated account belonging to Ryan Brooks. "
            "The account was used during the breach, "
            "but investigators have not determined "
            "whether Ryan personally accessed the system "
            "or whether another individual obtained "
            "his credentials."
        ),

        "points": 20
    },

    # ------------------------------------
    # EVIDENCE 6 - RECOVERED DEVICE
    # ------------------------------------

    "6": {
        "name": "Recovered Device Forensics",

        "description": (
            "Investigators recovered a university-issued "
            "laptop that Ryan Brooks had retained after "
            "leaving employment. A forensic examination "
            "found the browser session used during the "
            "2:43 AM breach, along with a locally saved "
            "copy of the exported student records. "
            "A recovered message sent from the device "
            "before the breach described a plan to "
            "retrieve those records. These findings "
            "provide stronger evidence linking Ryan "
            "to the incident, although investigators "
            "must still consider whether the device "
            "could have been used by someone else."
        ),

        "points": 20
    }
}


# ========================================
# CASE ANSWER KEY
# ========================================

correct_suspect = "3"


# ========================================
# OPTIONAL CASE INFORMATION
# ========================================

case_number = "001"

case_status = "ACTIVE INVESTIGATION"

case_category = "Unauthorized Database Access"

case_difficulty = "Intermediate"


