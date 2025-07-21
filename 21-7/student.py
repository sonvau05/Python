class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
    
    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

def find_top_student(students):
    return max(students, key=lambda x: x.average_score(), default=None)

def filter_high_achievers(students, threshold=8):
    return [s for s in students if s.average_score() > threshold]