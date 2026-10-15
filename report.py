
# ----------------------------------------
# DIGITAL DETECTIVE
# FINAL INVESTIGATION REPORT GENERATOR
# ----------------------------------------

from datetime import datetime

from cases import (
    case_name,
    suspects,
    evidence
)

from challenges import challenges

from connections import get_discovered_connections


def generate_investigation_report(
    collected_evidence,
    completed_interviews,
    collected_connections,
    completed_challenges,
    challenge_attempts,
    score,
    max_score,
    accused_suspect,
    accusation_correct,
    detective_rank,
    analysis_complete
):
    """
    Generate a downloadable text report
    summarizing the player's investigation.
    """

    lines = []

    lines.append("=" * 55)
    lines.append("DIGITAL DETECTIVE")
    lines.append("CYBERCRIME INVESTIGATION UNIT")
    lines.append("FINAL INVESTIGATION REPORT")
    lines.append("=" * 55)

    lines.append("")
    lines.append("CASE NUMBER: 001")
    lines.append(f"CASE NAME: {case_name}")
    lines.append(
        f"REPORT DATE: {datetime.now().strftime('%B %d, %Y')}"
    )

    lines.append("")
    lines.append("-" * 55)
    lines.append("CASE DISPOSITION")
    lines.append("-" * 55)

    if accusation_correct:
        lines.append("STATUS: CASE SOLVED")
    else:
        lines.append("STATUS: CASE UNSOLVED")

    lines.append(f"FINAL SCORE: {score}/{max_score}")
    lines.append(f"DETECTIVE RANK: {detective_rank}")

    lines.append("")
    lines.append("-" * 55)
    lines.append("FINAL ACCUSATION")
    lines.append("-" * 55)

    accused_name = suspects[accused_suspect]["name"]
    lines.append(f"ACCUSED SUSPECT: {accused_name}")

    if accusation_correct:
        lines.append("RESULT: Correct accusation")
    else:
        lines.append("RESULT: Incorrect accusation")

    lines.append("")
    lines.append("-" * 55)
    lines.append("COLLECTED DIGITAL EVIDENCE")
    lines.append("-" * 55)

    if collected_evidence:
        for evidence_id in collected_evidence:
            item = evidence[evidence_id]
            lines.append(f"Evidence: {item['name']}")
            lines.append(f"Description: {item['description']}")
            lines.append("")
    else:
        lines.append("No evidence collected.")

    lines.append("")
    lines.append("-" * 55)
    lines.append("SUSPECT INTERVIEW RECORDS")
    lines.append("-" * 55)

    if completed_interviews:
        for suspect_id, question_id in completed_interviews:
            suspect = suspects[suspect_id]
            interview = suspect["interviews"][question_id]

            lines.append(f"Suspect: {suspect['name']}")
            lines.append(f"Question: {interview['question']}")
            lines.append(f"Answer: {interview['answer']}")
            lines.append("")
    else:
        lines.append("No interviews completed.")

    lines.append("")
    lines.append("-" * 55)
    lines.append("EVIDENCE CONNECTIONS")
    lines.append("-" * 55)

    discovered = get_discovered_connections(
        collected_connections
    )

    if discovered:
        for connection in discovered:
            lines.append(
                f"Connection: {connection['name']}"
            )
            lines.append(connection["explanation"])
            lines.append("")
    else:
        lines.append("No connections discovered.")

    lines.append("")
    lines.append("-" * 55)
    lines.append("DIGITAL FORENSICS ANALYSIS")
    lines.append("-" * 55)

    if analysis_complete:
        lines.append(
            "Login activity analysis was completed."
        )
        lines.append(
            "The investigator reviewed suspicious "
            "login records and activity scores."
        )
    else:
        lines.append(
            "Digital forensics analysis was not completed."
        )

    lines.append("")
    lines.append("-" * 55)
    lines.append("DETECTIVE CHALLENGE RESULTS")
    lines.append("-" * 55)

    if challenge_attempts:
        for challenge_id, was_correct in challenge_attempts.items():
            challenge = challenges[challenge_id]

            lines.append(
                f"Challenge: {challenge['title']}"
            )

            if was_correct:
                lines.append("Result: Correct")
            else:
                lines.append("Result: Incorrect")

            lines.append(
                f"Explanation: {challenge['explanation']}"
            )
            lines.append("")
    else:
        lines.append("No challenges attempted.")

    lines.append("")
    lines.append(
        f"CHALLENGES SOLVED: {len(completed_challenges)}"
    )

    lines.append("")
    lines.append("=" * 55)
    lines.append("END OF INVESTIGATION REPORT")
    lines.append("=" * 55)

    return "\n".join(lines)
