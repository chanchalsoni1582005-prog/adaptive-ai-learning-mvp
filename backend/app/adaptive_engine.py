import json
import random

class AdaptiveEngine:
    def __init__(self, question_file="app/question_bank.json"):
        with open(question_file, "r") as f:
            self.questions = json.load(f)
        self.level = 2
        self.history = []
        self.skills = {"listening": [], "grasping": [], "retention": [], "application": []}

    def get_question(self):
        qs = [q for q in self.questions if q["difficulty"] == self.level]
        return random.choice(qs) if qs else random.choice(self.questions)

    def submit_answer(self, qid, option):
        q = next(q for q in self.questions if q["id"] == qid)
        correct = (option == q["answer"])
        if correct:
            self.level = min(5, self.level + 1)
        else:
            self.level = max(1, self.level - 1)
        self.skills[q["skill"]].append(1 if correct else 0)
        self.history.append({"qid": qid, "correct": correct})
        return correct

    def report(self):
        report = {}
        for skill, results in self.skills.items():
            if results:
                report[skill] = round(sum(results) / len(results) * 100, 2)
            else:
                report[skill] = 0
        return report
