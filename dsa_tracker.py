import json


def load_problems():
    try:
        with open("problems.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_problems():
    with open("problems.json", "w") as file:
        json.dump(problems, file, indent=4)


problems = load_problems()


print("================================")
print("       DSA PRACTICE TRACKER")
print("================================")

while True:
    print("\n1. Add Problem")
    print("2. View Problems")
    print("3. Mark Problem as Solved")
    print("4. Search by Topic")
    print("5. Show Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter problem name: ")
        platform = input("Enter platform (LeetCode/GFG/HackerRank): ")
        topic = input("Enter topic: ")
        difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

        problem = {
            "name": name,
            "platform": platform,
            "topic": topic,
            "difficulty": difficulty,
            "status": "Pending"
        }

        problems.append(problem)
        save_problems()

        print("Problem added successfully!")

    elif choice == "2":
        if len(problems) == 0:
            print("No problems added yet.")
        else:
            print("\n========== YOUR DSA PROBLEMS ==========")

            for i, problem in enumerate(problems, start=1):
                print(f"\nProblem {i}")
                print(f"Name: {problem['name']}")
                print(f"Platform: {problem['platform']}")
                print(f"Topic: {problem['topic']}")
                print(f"Difficulty: {problem['difficulty']}")
                print(f"Status: {problem['status']}")

    elif choice == "3":
        if len(problems) == 0:
            print("No problems available.")
        else:
            print("\n========== YOUR DSA PROBLEMS ==========")

            for i, problem in enumerate(problems, start=1):
                print(f"{i}. {problem['name']} - {problem['status']}")

            try:
                number = int(input("\nEnter the problem number to mark as solved: "))

                if 1 <= number <= len(problems):
                    problems[number - 1]["status"] = "Solved"
                    save_problems()

                    print("Problem marked as solved! ✅")
                else:
                    print("Invalid problem number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Search by Topic selected")

    elif choice == "5":
        print("Show Statistics selected")

    elif choice == "6":
        print("Thank you for using DSA Practice Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")