
import streamlit as st

from cases import (
    case_name,
    case_description,
    suspects,
    evidence,
    correct_suspect
)

from forensics import (
    login_records,
    analyze_logins,
    count_login_attempts,
    identify_suspicious_users
)

from connections import (
    check_connection,
    get_total_connections,
    get_discovered_connections
)

from challenges import (
    challenges,
    check_answer,
    get_total_challenges
)

from report import generate_investigation_report


# ========================================
# WEBSITE CONFIGURATION
# ========================================

st.set_page_config(
    page_title="Digital Detective",
    page_icon="🕵️",
    layout="wide"
)


# ========================================
# WEBSITE DESIGN
# ========================================

st.markdown("""
<style>

/* MAIN APPLICATION */

.stApp {
    background: linear-gradient(
        135deg,
        #0B1422 0%,
        #111F32 100%
    );
    color: #E8F0F7;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADINGS AND TEXT */

h1, h2, h3 {
    color: #F3F8FC !important;
    letter-spacing: 0.3px;
}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    color: #E8F0F7;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #101D2E;
    border-right: 1px solid #2A4157;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    padding: 8px 10px;
    border-radius: 8px;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #1B3349;
}

/* BUTTONS */

div.stButton > button,
div.stDownloadButton > button {
    background: linear-gradient(
        90deg,
        #164A58,
        #176D72
    );
    color: #FFFFFF !important;
    border: 1px solid #2B8C8D;
    border-radius: 9px;
    padding: 0.55rem 1rem;
    font-weight: 600;
    transition: all 0.2s ease;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover {
    background: #21868B;
    border-color: #55D6BD;
    color: #FFFFFF !important;
}

/* INPUT LABELS */

[data-testid="stWidgetLabel"] p {
    color: #E8F0F7 !important;
    font-weight: 500;
}

[data-testid="stSelectbox"] label p,
[data-testid="stMultiSelect"] label p,
[data-testid="stTextArea"] label p,
[data-testid="stRadio"] label p {
    color: #E8F0F7 !important;
}

/* SELECTBOX AND MULTISELECT */

[data-baseweb="select"] > div {
    background-color: #1B2B40 !important;
    border: 1px solid #35536C !important;
    border-radius: 9px !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;
}

[data-baseweb="select"] span {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #E8F0F7 !important;
}

/* DROPDOWN MENU */

[data-baseweb="popover"] {
    background-color: #1B2B40 !important;
}

[data-baseweb="menu"] {
    background-color: #1B2B40 !important;
}

[data-baseweb="menu"] li {
    color: #FFFFFF !important;
}

[data-baseweb="menu"] li:hover {
    background-color: #26445C !important;
}

/* TEXT AREA */

[data-testid="stTextArea"] textarea {
    background-color: #1B2B40 !important;
    color: #FFFFFF !important;
    border: 1px solid #35536C !important;
    border-radius: 9px !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #A5B9C9 !important;
}

/* METRIC CARDS */

[data-testid="stMetric"] {
    background: #1B2B40;
    border: 1px solid #2A4258;
    border-radius: 12px;
    padding: 18px;
}

[data-testid="stMetricValue"] {
    color: #55D6BD !important;
}

[data-testid="stMetricLabel"] {
    color: #B5C9D8 !important;
}

/* EXPANDERS */

[data-testid="stExpander"] {
    background: #17273B;
    border: 1px solid #2A4258;
    border-radius: 10px;
}

/* PROGRESS BARS */

[data-testid="stProgress"] [role="progressbar"] {
    background-color: #26394D !important;
    border-radius: 10px;
    overflow: hidden;
}

[data-testid="stProgress"] [role="progressbar"] > div {
    background-color: #55D6BD !important;
    border-radius: 10px;
}

/* ALERTS */

[data-testid="stAlert"] {
    border-radius: 10px;
    border: 1px solid #35536C;
}

[data-testid="stAlert"] p {
    color: #E8F0F7 !important;
}

/* DATA TABLES */

[data-testid="stDataFrame"] {
    border: 1px solid #2A4258;
    border-radius: 10px;
}

/* DIVIDERS */

hr {
    border-color: #2A4258;
}

[data-testid="stExpander"] {
    background-color: #17273B !important;
    border: 1px solid #35536C !important;
    border-radius: 10px !important;
    overflow: hidden;
}

[data-testid="stExpander"] details > summary {
    background-color: #1B2B40 !important;
    color: #E8F0F7 !important;
    border-radius: 9px !important;
}

[data-testid="stExpander"] details[open] > summary {
    background-color: #213A52 !important;
}

[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary div {
    color: #E8F0F7 !important;
}

[data-testid="stExpander"] summary svg {
    color: #55D6BD !important;
    fill: #55D6BD !important;
}

[data-testid="stExpander"] details > summary:hover {
    background-color: #29445E !important;
}

[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    background-color: #17273B !important;
    color: #E8F0F7 !important;
}

</style>
""", unsafe_allow_html=True)



# ========================================
# SESSION STATE
# ========================================

def initialize_state():

    defaults = {
        "collected_evidence": [],
        "completed_interviews": [],
        "collected_connections": [],
        "completed_challenges": [],
        "challenge_attempts": {},
        "score": 0,
        "case_completed": False,
        "accusation_correct": False,
        "analysis_complete": False,
        "accused_suspect": None,
        "accusation_evidence": [],
        "accusation_reasoning": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


initialize_state()


# ========================================
# HELPER FUNCTIONS
# ========================================

def total_interviews():

    return sum(
        len(suspect["interviews"])
        for suspect in suspects.values()
    )


def maximum_score():

    evidence_points = sum(
        item["points"]
        for item in evidence.values()
    )

    interview_points = total_interviews() * 5

    connection_points = get_total_connections() * 10

    challenge_points = sum(
        item["points"]
        for item in challenges.values()
    )

    accusation_points = 30

    return (
        evidence_points
        + interview_points
        + connection_points
        + challenge_points
        + accusation_points
    )


def collect_evidence(evidence_id):

    if st.session_state.case_completed:
        return False

    if evidence_id not in st.session_state.collected_evidence:

        st.session_state.collected_evidence.append(evidence_id)

        st.session_state.score += evidence[evidence_id]["points"]

        return True

    return False


def complete_interview(suspect_id, question_id):

    if st.session_state.case_completed:
        return False

    interview_key = (suspect_id, question_id)

    if interview_key not in st.session_state.completed_interviews:

        st.session_state.completed_interviews.append(interview_key)

        st.session_state.score += 5

        return True

    return False


def calculate_progress():

    total_actions = (
        len(evidence)
        + total_interviews()
        + get_total_connections()
        + get_total_challenges()
    )

    completed_actions = (
        len(st.session_state.collected_evidence)
        + len(st.session_state.completed_interviews)
        + len(st.session_state.collected_connections)
        + len(st.session_state.completed_challenges)
    )

    if total_actions == 0:
        return 0.0

    return min(completed_actions / total_actions, 1.0)


def get_detective_rank(score, accusation_correct):

    if not accusation_correct:
        return "CASE UNSOLVED"

    maximum = maximum_score()

    if score >= maximum * 0.93:
        return "MASTER DETECTIVE"

    elif score >= maximum * 0.71:
        return "SENIOR INVESTIGATOR"

    elif score >= maximum * 0.44:
        return "JUNIOR DETECTIVE"

    else:
        return "ROOKIE INVESTIGATOR"


def reset_game():

    st.session_state.collected_evidence = []
    st.session_state.completed_interviews = []
    st.session_state.collected_connections = []
    st.session_state.completed_challenges = []
    st.session_state.challenge_attempts = {}

    st.session_state.score = 0
    st.session_state.case_completed = False
    st.session_state.accusation_correct = False
    st.session_state.analysis_complete = False
    st.session_state.accused_suspect = None

    st.session_state.accusation_evidence = []
    st.session_state.accusation_reasoning = ""

    # Clear saved form selections
    for key in list(st.session_state.keys()):

        if key.startswith("challenge_answer_"):
            del st.session_state[key]

        elif key in [
            "final_suspect",
            "supporting_evidence",
            "investigator_reasoning",
            "first_evidence",
            "second_evidence"
        ]:
            del st.session_state[key]


# ========================================
# SIDEBAR NAVIGATION
# ========================================

st.sidebar.title("🕵️ DIGITAL DETECTIVE")
st.sidebar.caption("CYBERCRIME INVESTIGATION UNIT")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Evidence Locker",
        "Suspect Interviews",
        "Digital Forensics Lab",
        "Evidence Connections",
        "Detective Challenges",
        "Investigation Progress",
        "Final Accusation"
    ]
)

st.sidebar.divider()

st.sidebar.metric(
    "Investigation Score",
    f"{st.session_state.score}/{maximum_score()}"
)

st.sidebar.progress(calculate_progress())

st.sidebar.caption(
    f"{calculate_progress() * 100:.0f}% investigation complete"
)

if st.sidebar.button("Restart Investigation"):

    reset_game()

    st.rerun()


# ========================================
# DASHBOARD
# ========================================

if page == "Dashboard":

    st.title("🛡️ DIGITAL DETECTIVE")

    st.caption("CYBERCRIME INVESTIGATION COMMAND CENTER")

    st.divider()

    if st.session_state.case_completed:

        if st.session_state.accusation_correct:
            status = "CASE SOLVED"

        else:
            status = "CASE UNSOLVED"

    else:
        status = "ACTIVE INVESTIGATION"

    st.subheader("📂 CASE FILE #001")

    st.info(f"{case_name} | {status}")

    st.write(case_description)

    st.divider()

    st.subheader("Investigation Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Evidence Collected",
            f"{len(st.session_state.collected_evidence)}/{len(evidence)}"
        )

    with col2:

        st.metric(
            "Suspect Interviews",
            f"{len(st.session_state.completed_interviews)}/{total_interviews()}"
        )

    with col3:

        st.metric(
            "Evidence Connections",
            f"{len(st.session_state.collected_connections)}/{get_total_connections()}"
        )

    with col4:

        st.metric(
            "Challenges Solved",
            f"{len(st.session_state.completed_challenges)}/{get_total_challenges()}"
        )

    st.divider()

    st.subheader("Investigation Progress")

    progress = calculate_progress()

    st.progress(progress)

    st.write(f"**{progress * 100:.0f}% Complete**")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("🎯 Mission Objectives")

        st.markdown("""
- Examine digital evidence
- Interview the three suspects
- Analyze suspicious login records
- Discover evidence connections
- Complete detective challenges
- Build an evidence-based accusation
        """)

    with right:

        st.subheader("📡 Investigation Intelligence")

        st.metric(
            "Current Score",
            f"{st.session_state.score}/{maximum_score()}"
        )

        st.write(
            "Forensic Analysis:",
            "Complete" if st.session_state.analysis_complete else "Pending"
        )

        st.write(
            "Final Accusation:",
            "Submitted" if st.session_state.case_completed else "Pending"
        )

    st.divider()

    if st.session_state.case_completed:

        if st.session_state.accusation_correct:
            st.success("Investigation completed successfully.")

        else:
            st.error("Investigation closed with an incorrect accusation.")

    else:

        st.info(
            "Your investigation is active. Continue gathering "
            "evidence before submitting your accusation."
        )


# ========================================
# EVIDENCE LOCKER
# ========================================

elif page == "Evidence Locker":

    st.title("📁 Evidence Locker")

    st.write(
        "Examine digital evidence from the university data breach."
    )

    st.divider()

    for evidence_id, item in evidence.items():

        with st.expander(item["name"]):

            st.write(item["description"])

            st.write(
                f"Evidence Value: {item['points']} points"
            )

            if evidence_id in st.session_state.collected_evidence:

                st.success("Evidence Collected")

            elif st.session_state.case_completed:

                st.info("Investigation completed.")

            else:

                if st.button(
                    "Collect Evidence",
                    key=f"evidence_{evidence_id}"
                ):

                    if collect_evidence(evidence_id):
                        st.rerun()


# ========================================
# SUSPECT INTERVIEWS
# ========================================

elif page == "Suspect Interviews":

    st.title("👤 Suspect Interviews")

    st.write(
        "Interview suspects to learn more about the breach."
    )

    st.divider()

    suspect_id = st.selectbox(
        "Select a suspect",
        options=list(suspects.keys()),
        format_func=lambda key: suspects[key]["name"]
    )

    selected_suspect = suspects[suspect_id]

    st.subheader(selected_suspect["name"])

    st.write(
        "Role:",
        selected_suspect["role"]
    )

    st.divider()

    for question_id, interview in selected_suspect["interviews"].items():

        with st.expander(interview["question"]):

            interview_key = (suspect_id, question_id)

            if interview_key in st.session_state.completed_interviews:

                st.write(
                    "**Answer:**",
                    interview["answer"]
                )

                st.success("Interview completed")

            else:

                if st.button(
                    "Ask Question",
                    key=f"interview_{suspect_id}_{question_id}",
                    disabled=st.session_state.case_completed
                ):

                    if complete_interview(
                        suspect_id,
                        question_id
                    ):
                        st.rerun()


# ========================================
# DIGITAL FORENSICS LAB
# ========================================

elif page == "Digital Forensics Lab":

    st.title("💻 Digital Forensics Lab")

    st.write(
        "Analyze login records and identify suspicious activity."
    )

    st.divider()

    st.subheader("University Login Records")

    st.dataframe(
        login_records,
        use_container_width=True
    )

    st.divider()

    if st.button(
        "Analyze Login Activity",
        disabled=st.session_state.case_completed
    ):

        st.session_state.analysis_complete = True

    if st.session_state.analysis_complete:

        st.subheader("Suspicious Login Records")

        st.dataframe(
            analyze_logins(),
            use_container_width=True
        )

        st.divider()

        st.subheader("Login Attempts by User")

        st.bar_chart(
            count_login_attempts()
        )

        st.divider()

        st.subheader("Suspicious Activity Scores")

        st.bar_chart(
            identify_suspicious_users()
        )

        st.info(
            "Risk scores identify suspicious activity, "
            "but do not independently prove who committed the breach."
        )


# ========================================
# EVIDENCE CONNECTIONS
# ========================================

elif page == "Evidence Connections":

    st.title("🔗 Evidence Connections")

    st.write(
        "Connect evidence files to discover relationships."
    )

    st.divider()

    collected = st.session_state.collected_evidence

    if len(collected) < 2:

        st.warning(
            "Collect at least two evidence files first."
        )

    else:

        col1, col2 = st.columns(2)

        with col1:

            first_id = st.selectbox(
                "First Evidence File",
                options=collected,
                format_func=lambda key: evidence[key]["name"],
                key="first_evidence"
            )

        with col2:

            second_id = st.selectbox(
                "Second Evidence File",
                options=collected,
                format_func=lambda key: evidence[key]["name"],
                key="second_evidence"
            )

        if st.button(
            "Analyze Connection",
            disabled=st.session_state.case_completed
        ):

            if first_id == second_id:

                st.warning(
                    "Select two different evidence files."
                )

            else:

                result = check_connection(
                    first_id,
                    second_id
                )

                if result is None:

                    st.error(
                        "No significant connection found."
                    )

                else:

                    connection_key = tuple(
                        sorted([first_id, second_id])
                    )

                    if connection_key not in st.session_state.collected_connections:

                        st.session_state.collected_connections.append(
                            connection_key
                        )

                        st.session_state.score += result["points"]

                        st.success(
                            f"Connection discovered! "
                            f"+{result['points']} points"
                        )

                    else:

                        st.info(
                            "Connection already discovered."
                        )

                    st.subheader(result["name"])

                    st.write(
                        result["explanation"]
                    )

    st.divider()

    st.subheader("Discovered Connections")

    discovered = get_discovered_connections(
        st.session_state.collected_connections
    )

    st.metric(
        "Connections Discovered",
        f"{len(discovered)}/{get_total_connections()}"
    )

    for connection in discovered:

        with st.expander(connection["name"]):

            st.write(
                connection["explanation"]
            )


# ========================================
# DETECTIVE CHALLENGES
# ========================================

elif page == "Detective Challenges":

    st.title("🧠 Detective Challenges")

    st.write(
        "Test your cybersecurity investigation skills."
    )

    st.divider()

    st.metric(
        "Challenges Solved",
        f"{len(st.session_state.completed_challenges)}/{get_total_challenges()}"
    )

    st.caption(
        "Each challenge can only be attempted once."
    )

    st.divider()

    for challenge_id, challenge in challenges.items():

        with st.expander(
            f"Challenge {challenge_id}: {challenge['title']}"
        ):

            st.write(
                challenge["question"]
            )

            if challenge_id in st.session_state.challenge_attempts:

                correct = st.session_state.challenge_attempts[
                    challenge_id
                ]

                if correct:

                    st.success(
                        "Correct! Points awarded."
                    )

                else:

                    st.error(
                        "Incorrect answer. No points awarded."
                    )

                st.info(
                    challenge["explanation"]
                )

            elif st.session_state.case_completed:

                st.info(
                    "Investigation completed."
                )

            else:

                selected_answer = st.radio(
                    "Choose your answer:",
                    options=list(range(len(challenge["options"]))),
                    format_func=lambda index, c=challenge: c["options"][index],
                    index=None,
                    key=f"challenge_answer_{challenge_id}"
                )

                if st.button(
                    "Submit Answer",
                    key=f"submit_challenge_{challenge_id}"
                ):

                    if selected_answer is None:

                        st.warning(
                            "Select an answer first."
                        )

                    else:

                        correct = check_answer(
                            challenge_id,
                            selected_answer
                        )

                        st.session_state.challenge_attempts[
                            challenge_id
                        ] = correct

                        if correct:

                            st.session_state.completed_challenges.append(
                                challenge_id
                            )

                            st.session_state.score += challenge["points"]

                        st.rerun()


# ========================================
# INVESTIGATION PROGRESS
# ========================================

elif page == "Investigation Progress":

    st.title("📊 Investigation Progress")

    st.write(
        "Track your investigation and overall score."
    )

    st.divider()

    progress = calculate_progress()

    st.progress(progress)

    st.write(
        f"Overall Completion: {progress * 100:.1f}%"
    )

    st.divider()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Evidence",
        f"{len(st.session_state.collected_evidence)}/{len(evidence)}"
    )

    col2.metric(
        "Interviews",
        f"{len(st.session_state.completed_interviews)}/{total_interviews()}"
    )

    col3.metric(
        "Connections",
        f"{len(st.session_state.collected_connections)}/{get_total_connections()}"
    )

    col4.metric(
        "Challenges",
        f"{len(st.session_state.completed_challenges)}/{get_total_challenges()}"
    )

    col5.metric(
        "Score",
        f"{st.session_state.score}/{maximum_score()}"
    )

    st.divider()

    st.subheader("Suspect Interview Progress")

    for suspect_id, suspect in suspects.items():

        completed_count = 0

        for question_id in suspect["interviews"]:

            if (suspect_id, question_id) in st.session_state.completed_interviews:

                completed_count += 1

        count = len(suspect["interviews"])

        st.write(suspect["name"])

        st.progress(
            completed_count / count if count else 0.0
        )

        st.caption(
            f"{completed_count}/{count} questions completed"
        )

    st.divider()

    st.subheader("Evidence Connection Progress")

    connection_total = get_total_connections()

    st.progress(
        len(st.session_state.collected_connections) / connection_total
        if connection_total else 0.0
    )

    st.caption(
        f"{len(st.session_state.collected_connections)}/{connection_total} "
        "connections discovered"
    )

    st.divider()

    st.subheader("Detective Challenge Progress")

    challenge_total = get_total_challenges()

    st.progress(
        len(st.session_state.completed_challenges) / challenge_total
        if challenge_total else 0.0
    )

    st.caption(
        f"{len(st.session_state.completed_challenges)}/{challenge_total} "
        "challenges solved"
    )


# ========================================
# FINAL ACCUSATION AND REPORT
# ========================================

elif page == "Final Accusation":

    st.title("⚖️ Final Accusation")

    st.caption(
        "CYBERCRIME INVESTIGATION UNIT | CASE #001"
    )

    st.write(
        "Present your findings, identify the suspect, "
        "and explain the evidence supporting your conclusion."
    )

    st.divider()

    evidence_count = len(st.session_state.collected_evidence)
    interview_count = len(st.session_state.completed_interviews)
    connection_count = len(st.session_state.collected_connections)
    challenge_count = len(st.session_state.completed_challenges)

    # ------------------------------------
    # COMPLETED CASE
    # ------------------------------------

    if st.session_state.case_completed:

        st.subheader("📄 Final Investigation Report")

        if st.session_state.accusation_correct:

            st.success("CASE SOLVED!")

            st.write(
                "Your accusation matched the case answer key."
            )

        else:

            st.error("CASE UNSOLVED!")

            st.write(
                "Your accusation did not match the case answer key."
            )

            st.write(
                "Correct Suspect:",
                suspects[correct_suspect]["name"]
            )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Final Score",
                f"{st.session_state.score}/{maximum_score()}"
            )

        with col2:

            st.metric(
                "Evidence Collected",
                f"{evidence_count}/{len(evidence)}"
            )

        with col3:

            st.metric(
                "Connections",
                f"{connection_count}/{get_total_connections()}"
            )

        st.subheader(
            get_detective_rank(
                st.session_state.score,
                st.session_state.accusation_correct
            )
        )

        st.divider()

        st.subheader("Investigation Summary")

        st.write(
            f"Interviews Completed: {interview_count}/{total_interviews()}"
        )

        st.write(
            f"Evidence Connections: {connection_count}/{get_total_connections()}"
        )

        st.write(
            f"Detective Challenges: {challenge_count}/{get_total_challenges()}"
        )

        st.write(
            "Forensics Analysis:",
            "Completed" if st.session_state.analysis_complete else "Not Completed"
        )

        accused_id = st.session_state.accused_suspect

        if accused_id is not None:

            st.write(
                "**Accused Suspect:**",
                suspects[accused_id]["name"]
            )

        st.divider()

        # --------------------------------
        # INVESTIGATOR REASONING
        # --------------------------------

        st.subheader("🧠 Investigator's Reasoning")

        saved_evidence = st.session_state.accusation_evidence

        saved_reasoning = st.session_state.accusation_reasoning

        if saved_evidence:

            st.write("**Evidence Cited:**")

            for evidence_id in saved_evidence:

                st.write(
                    f"- {evidence[evidence_id]['name']}"
                )

        st.write("**Investigator's Explanation:**")

        st.write(saved_reasoning)

        st.divider()

        # --------------------------------
        # DOWNLOAD FINAL REPORT
        # --------------------------------

        st.subheader("📥 Download Investigation Report")

        if accused_id is not None:

            report_text = generate_investigation_report(
                collected_evidence=st.session_state.collected_evidence,
                completed_interviews=st.session_state.completed_interviews,
                collected_connections=st.session_state.collected_connections,
                completed_challenges=st.session_state.completed_challenges,
                challenge_attempts=st.session_state.challenge_attempts,
                score=st.session_state.score,
                max_score=maximum_score(),
                accused_suspect=accused_id,
                accusation_correct=st.session_state.accusation_correct,
                detective_rank=get_detective_rank(
                    st.session_state.score,
                    st.session_state.accusation_correct
                ),
                analysis_complete=st.session_state.analysis_complete
            )

            report_text += "\n\n"
            report_text += "=" * 55 + "\n"
            report_text += "INVESTIGATOR'S FINAL REASONING\n"
            report_text += "=" * 55 + "\n\n"

            report_text += "EVIDENCE CITED:\n"

            for evidence_id in saved_evidence:

                report_text += (
                    f"- {evidence[evidence_id]['name']}\n"
                )

            report_text += "\nEXPLANATION:\n"

            report_text += saved_reasoning + "\n"

            st.download_button(
                label="📥 Download Final Case Report",
                data=report_text,
                file_name="digital_detective_case_001_report.txt",
                mime="text/plain",
                use_container_width=True
            )

        else:

            st.warning(
                "No saved accusation was found."
            )

        st.info(
            "Investigation complete. Restart using the sidebar to play again."
        )

    # ------------------------------------
    # INVESTIGATION REQUIREMENTS
    # ------------------------------------

    else:

        st.subheader("Investigation Requirements")

        requirements = {
            "Collect at least 3 evidence files":
                evidence_count >= 3,

            "Complete at least 3 interview questions":
                interview_count >= 3,

            "Complete digital forensics analysis":
                st.session_state.analysis_complete,

            "Discover at least 2 evidence connections":
                connection_count >= 2,

            "Collect the recovered device evidence":
                "6" in st.session_state.collected_evidence
        }

        for requirement, completed in requirements.items():

            if completed:

                st.success(
                    f"✓ {requirement}"
                )

            else:

                st.warning(
                    f"○ {requirement}"
                )

        ready = all(requirements.values())

        st.divider()

        if not ready:

            st.info(
                "Complete all investigation requirements "
                "before submitting your final accusation."
            )

        else:

            st.success(
                "All investigation requirements completed!"
            )

            st.subheader("Build Your Case")

            # ----------------------------
            # SELECT SUSPECT
            # ----------------------------

            accusation = st.selectbox(
                "Who committed the cybercrime?",
                options=list(suspects.keys()),
                format_func=lambda key: suspects[key]["name"],
                key="final_suspect"
            )

            # ----------------------------
            # SUPPORTING EVIDENCE
            # ----------------------------

            st.subheader("Supporting Evidence")

            supporting_evidence = st.multiselect(
                "Select at least 2 evidence files supporting your accusation",
                options=st.session_state.collected_evidence,
                format_func=lambda key: evidence[key]["name"],
                key="supporting_evidence"
            )

            # ----------------------------
            # WRITTEN EXPLANATION
            # ----------------------------

            st.subheader("Investigator's Explanation")

            reasoning = st.text_area(
                "Explain why you believe this suspect is responsible.",
                placeholder=(
                    "Explain which clues support your accusation, "
                    "how the evidence connects, and why alternative "
                    "explanations are less convincing."
                ),
                height=160,
                key="investigator_reasoning"
            )

            st.caption(
                "Your explanation must contain at least 100 characters."
            )

            st.divider()

            # ----------------------------
            # SUBMIT ACCUSATION
            # ----------------------------

            if st.button(
                "Submit Final Accusation",
                use_container_width=True
            ):

                if len(supporting_evidence) < 2:

                    st.error(
                        "Select at least 2 supporting evidence files."
                    )

                elif len(reasoning.strip()) < 100:

                    st.error(
                        "Your explanation must contain at least 100 characters."
                    )

                else:

                    st.session_state.accused_suspect = accusation

                    st.session_state.accusation_evidence = (
                        supporting_evidence.copy()
                    )

                    st.session_state.accusation_reasoning = (
                        reasoning.strip()
                    )

                    st.session_state.accusation_correct = (
                        accusation == correct_suspect
                    )

                    if st.session_state.accusation_correct:

                        st.session_state.score += 30

                    st.session_state.case_completed = True

                    st.rerun()

