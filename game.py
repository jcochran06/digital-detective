
from cases import case_name, case_description
from cases import suspects, evidence, correct_suspect

# Display the main menu
def display_menu():
    print("\n===== DIGITAL DETECTIVE =====")
    print("1. View Case Details")
    print("2. Review Evidence")
    print("3. Interview Suspects")
    print("4. Submit Final Accusation")
    print("5. View Investigation Progress")
    print("6. Exit Game")

# Display information about the current case
def view_case():
    print("\n===== CASE DETAILS =====")
    print("CASE:", case_name)
    print(case_description)

# Allow players to examine and collect evidence
def review_evidence(collected_evidence, score):

    print("\n===== EVIDENCE LOCKER =====")

    for evidence_id, item in evidence.items():
        print(evidence_id + ". " + item["name"])

    choice = input("\nSelect evidence to examine (1-5): ")

    # Check if the selected evidence exists
    if choice not in evidence:
        print("Invalid evidence selection.")
        return score

    selected = evidence[choice]

    print("\nEvidence:", selected["name"])
    print("Findings:", selected["description"])

    # Prevent players from earning duplicate points
    if choice not in collected_evidence:
        collected_evidence.append(choice)
        score += selected["points"]

        print("\nEvidence collected!")
        print("Points earned:", selected["points"])

    else:
        print("\nYou have already collected this evidence.")

    return score

# Allow players to interview suspects
def interview_suspects(completed_interviews, score):

    print("\n===== SUSPECT INTERVIEWS =====")

    for suspect_id, suspect in suspects.items():
        print(suspect_id + ". " + suspect["name"])

    choice = input("\nSelect a suspect (1-3): ")

    # Validate the suspect selection
    if choice not in suspects:
        print("Invalid suspect selection.")
        return score

    selected = suspects[choice]

    print("\nInterviewing:", selected["name"])
    print("Role:", selected["role"])

    # Display available interview questions
    for question_id, interview in selected["interviews"].items():
        print(question_id + ". " + interview["question"])

    question_choice = input("\nChoose a question (1-3): ")

    # Validate the interview question
    if question_choice not in selected["interviews"]:
        print("Invalid question.")
        return score

    interview = selected["interviews"][question_choice]

    print("\nQuestion:", interview["question"])
    print("Answer:", interview["answer"])

    # Store both the suspect and question ID
    interview_key = (choice, question_choice)

    # Award points only for new interview questions
    if interview_key not in completed_interviews:
        completed_interviews.append(interview_key)
        score += 5

        print("\nInterview completed! +5 points")

    else:
        print("\nYou have already asked this question.")

    return score

# Display the player's investigation progress
def show_progress(collected_evidence, completed_interviews, score):

    print("\n===== INVESTIGATION PROGRESS =====")

    print("Evidence collected:", len(collected_evidence), "/ 5")
    print("Interviews completed:", len(completed_interviews), "/ 9")
    print("Current score:", score)

    print("\n===== SUSPECT INTERVIEW STATUS =====")

    # Outer loop goes through each suspect
    for suspect_id, suspect in suspects.items():

        completed_count = 0

        # Inner loop checks each interview question
        for question_id in suspect["interviews"]:

            interview_key = (suspect_id, question_id)

            if interview_key in completed_interviews:
                completed_count += 1

        print(
            suspect["name"],
            "-",
            completed_count,
            "/ 3 questions"
        )

    # Calculate overall investigation progress
    total_actions = len(evidence) + sum(
        len(suspect["interviews"]) for suspect in suspects.values()
    )

    completed_actions = (
        len(collected_evidence) + len(completed_interviews)
    )

    progress = (completed_actions / total_actions) * 100

    print("\nOverall Investigation Progress:", round(progress, 1), "%")

# Allow players to submit their final accusation
def submit_accusation(collected_evidence, completed_interviews, score):

    print("\n===== FINAL ACCUSATION =====")

    # Require at least 3 pieces of evidence
    if len(collected_evidence) < 3:
        print("You need at least 3 pieces of evidence.")
        print("Continue investigating before making an accusation.")
        return False

    # Require at least 3 completed interview questions
    if len(completed_interviews) < 3:
        print("You must complete at least 3 interview questions.")
        print("Continue interviewing suspects.")
        return False

    print("\nWho do you believe committed the cybercrime?")

    for suspect_id, suspect in suspects.items():
        print(suspect_id + ". " + suspect["name"])

    choice = input("\nEnter the suspect number (1-3): ")

    # Validate the accusation
    if choice not in suspects:
        print("Invalid suspect selection.")
        return False

    # Determine whether the accusation is correct
    if choice == correct_suspect:
        score += 30

        print("\n===== CASE SOLVED =====")
        print("You correctly identified the suspect!")
        print("Congratulations, Detective!")

    else:
        print("\n===== CASE UNSOLVED =====")
        print("Your accusation was incorrect.")
        print("The evidence does not support your conclusion.")
        print("The correct suspect was:", suspects[correct_suspect]["name"])

    # Display the final score
    print("\n===== FINAL INVESTIGATION REPORT =====")
    print("Evidence collected:", len(collected_evidence), "/ 5")
    print("Interviews completed:", len(completed_interviews), "/ 9")
    print("Final Score:", score, "/ 145")

    # Assign a detective rank based on performance
    if score >= 140:
        print("Rank: MASTER DETECTIVE")

    elif score >= 100:
        print("Rank: SENIOR INVESTIGATOR")

    elif score >= 60:
        print("Rank: JUNIOR DETECTIVE")

    else:
        print("Rank: ROOKIE INVESTIGATOR")

    print("\nInvestigation complete!")

    return True

# Main function that controls the game
def main():

    print("Welcome to Digital Detective!")
    print("Cybercrime Investigation Simulator")

    # Variables used to track player progress
    collected_evidence = []
    completed_interviews = []
    score = 0

    # Continue running until the player exits
    while True:

        display_menu()

        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            view_case()

        elif choice == "2":
            score = review_evidence(
                collected_evidence,
                score
            )

        elif choice == "3":
            score = interview_suspects(
                completed_interviews,
                score
            )

        elif choice == "4":
            if submit_accusation(
                collected_evidence,
                completed_interviews,
                score
            ):
                break

        elif choice == "5":
            show_progress(
                collected_evidence,
                completed_interviews,
                score
            )

        elif choice == "6":
            print("\nThanks for playing Digital Detective!")
            break

        else:
            print("Invalid option. Please choose 1-6.")

# Start the game
if __name__ == "__main__":
    main()
