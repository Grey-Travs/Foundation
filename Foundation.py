def clamp(x, low=0.0, high=100.0):
    return max(low, min(high, x))

def attendance_score(absences: int) -> float:
    # Starts at 100, -10 per absence, clamped to [0,100]
    return clamp(100 - 10 * absences, 0, 100)

def class_standing(quizzes: float, requirements: float, recitation: float) -> float:
    # 40% Quizzes + 30% Requirements + 30% Recitation
    return 0.40 * quizzes + 0.30 * requirements + 0.30 * recitation

def prelim_grade(prelim_exam: float, attendance: float, cls: float) -> float:
    # Prelim Grade = 60% Prelim Exam + 10% Attendance + 30% Class Standing
    return 0.60 * prelim_exam + 0.10 * attendance + 0.30 * cls

def needed_midterm_final_equal(prelim: float, target_overall: float) -> float:
    """
    Assuming Overall = (Prelim + Midterm + Final)/3 and Midterm = Final,
    solve for each:  each = (3*target - prelim) / 2
    """
    return (3 * target_overall - prelim) / 2

def main():
    print("=== Prelim Calculator ===")
    print("Type 'quit' anytime to exit.\n")

    while True:
        raw = input("Absences: ")
        if raw.lower() == "quit": break
        absences = int(raw)

        prelim_exam = float(input("Prelim Exam Grade: "))
        quizzes     = float(input("Quizzes Grade: "))
        requirements= float(input("Requirements Grade: "))
        recitation  = float(input("Recitation Grade: "))

        att = attendance_score(absences)
        cs  = class_standing(quizzes, requirements, recitation)
        prelim = prelim_grade(prelim_exam, att, cs)

        print("\n--- Components ---")
        print(f"Attendance Score: {att:.2f}")
        print(f"Class Standing : {cs:.2f}")

        print("\n--- Result ---")
        print(f"Prelim Grade   : {prelim:.2f}")

        # Targets
        for label, target in [("pass (75%)", 75.0), ("dean's list (90%)", 90.0)]:
            req_each = needed_midterm_final_equal(prelim, target)
            # If req_each not in [0,100], it signals impossibility under equal-mid/final assumption.
            possible = 0.0 <= req_each <= 100.0
            note = "" if possible else "  (Not possible with equal Midterm/Final in range 0–100)"
            print(f"To reach {label}: Midterm = {req_each:.2f}, Final = {req_each:.2f}{note}")

        again = input("\nEnter 'again' to compute another, or 'quit' to exit: ").lower()
        if again != "again":
            break
        print()

if __name__ == "__main__":
    main()