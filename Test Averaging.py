# ---------------------------------------
# Function 1: Collect Scores
# ---------------------------------------
def get_scores():
    scores = []

    # Ask for number of students
    num = int(input("Enter number of students: "))

    for i in range(1, num + 1):
        score = int(input(f"Enter score for student {i}: "))
        scores.append(score)

    return scores


# ---------------------------------------
# Function 2: Analyze Scores
# ---------------------------------------
def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    passed = 0
    failed = 0

    for score in scores:
        if score >= 60:
            passed += 1
        else:
            failed += 1

    return highest, lowest, average, passed, failed


# ---------------------------------------
# Function 3: Display Results
# ---------------------------------------
def display_results(high, low, avg, passed, failed):
    print("--- Score Report ---")
    print(f"Highest score: {high}")
    print(f"Lowest score: {low}")
    print(f"Average score: {avg:.1f}")
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")


# ---------------------------------------
# Main Program
# ---------------------------------------
def main():
    scores = get_scores()
    high, low, avg, passed, failed = analyze_scores(scores)
    display_results(high, low, avg, passed, failed)


# Run program
main()
