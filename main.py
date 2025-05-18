# main.py

# Attachee class
class Attachee:
    def __init__(self, name, division):
        self.name = name
        self.division = division
        self.tasks = []
        self.feedback = []
        self.score = 0

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' assigned to {self.name} in {self.division} division.")

    def give_feedback(self, feedback):
        self.feedback.append(feedback)

    def add_score(self, marks):
        if 0 <= marks <= 100:
            self.score += marks
        else:
            print("Score must be between 0 and 100.")

    def performance_summary(self):
        return {
            'Name': self.name,
            'Division': self.division,
            'Tasks': self.tasks,
            'Feedback': self.feedback,
            'Score': self.score
        }


# Task Manager class
class TaskManager:
    def __init__(self):
        self.divisions = {
            'Engineering': [],
            'Tech Programs': [],
            'Radio Support': [],
            'Hub Support': []
        }

    def add_attachee(self, attachee):
        if attachee.division in self.divisions:
            self.divisions[attachee.division].append(attachee)
        else:
            print(f"Division '{attachee.division}' does not exist.")

    def assign_task(self, attachee_name, task):
        for division in self.divisions.values():
            for att in division:
                if att.name == attachee_name:
                    att.add_task(task)
                    return
        print(f"Attachee '{attachee_name}' not found.")

    def give_feedback_and_score(self, attachee_name, feedback, score):
        for division in self.divisions.values():
            for att in division:
                if att.name == attachee_name:
                    att.give_feedback(feedback)
                    att.add_score(score)
                    return
        print(f"Attachee '{attachee_name}' not found.")

    def display_performance(self):
        print("\n--- Performance Report ---")
        for division, attachees in self.divisions.items():
            print(f"\nDivision: {division}")
            for att in attachees:
                summary = att.performance_summary()
                print(f"  - {summary['Name']}: Tasks={len(summary['Tasks'])}, Score={summary['Score']}, Feedback={summary['Feedback']}")


# main program
def main():
    manager = TaskManager()

    # Create attachees
    a1 = Attachee("Mutanu", "Engineering")
    a2 = Attachee("Zippy", "Tech Programs")
    a3 = Attachee("Kimathi", "Radio Support")
    a4 = Attachee("Zawadi", "Hub Support")

    # Add attachees to manager
    manager.add_attachee(a1)
    manager.add_attachee(a2)
    manager.add_attachee(a3)
    manager.add_attachee(a4)

    # Assign tasks and give feedback
    manager.assign_task("Mutanu", "Design circuit")
    manager.assign_task("Zippy", "Develop web app")
    manager.assign_task("Kimathi", "Manage radio inventory")
    manager.assign_task("Zawadi", "Coordinate logistics")

    manager.give_feedback_and_score("Mutanu", "Great design!", 97)
    manager.give_feedback_and_score("Zippy", "Clean code.", 81)
    manager.give_feedback_and_score("Kimathi", "Efficient handling.", 90)
    manager.give_feedback_and_score("Zawadi", "Well organized.", 71)

    # Display all performance
    manager.display_performance()


if __name__ == "__main__":
    main()
