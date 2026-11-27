
assignments = []

def add_assignment(name):
    assignments.append(name)
    return assignments

if __name__ == "__main__":
    add_assignment("ASE Lab")
    print(assignments)
def view_assignments():
    return assignments