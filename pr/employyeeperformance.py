def evaluate_performance():
    print("=== Employee Performance Evaluation Expert System ===\n")

    # Collecting performance data
    punctuality = input("Was the employee punctual? (yes/no): ").lower()
    task_completion = input("Did the employee complete assigned tasks on time? (yes/no): ").lower()
    teamwork = input("Did the employee collaborate well in a team? (yes/no): ").lower()
    initiative = input("Did the employee take initiative? (yes/no): ").lower()
    communication = input("Is the employee's communication effective? (yes/no): ").lower()

    score = 0
    total = 5

    # Rule-based scoring
    if punctuality == "yes":
        score += 1
    if task_completion == "yes":
        score += 1
    if teamwork == "yes":
        score += 1
    if initiative == "yes":
        score += 1
    if communication == "yes":
        score += 1

    # Evaluation rules
    print("\nEvaluation Result:")
    if score == 5:
        print("Performance: ⭐ Excellent")
    elif score >= 3:
        print("Performance: 👍 Good")
    elif score >= 1:
        print("Performance: ⚠️ Needs Improvement")
    else:
        print("Performance: ❌ Poor")

if __name__ == "__main__":
    evaluate_performance()
