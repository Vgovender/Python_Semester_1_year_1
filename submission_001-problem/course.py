

def create_outline():
    print("Course Topics:")
    topic = sorted(set(["Introduction to Python","Tools of the Trade","How to make decisions","How to repeat code","How to structure data","Functions","Modules"]))
    
    for x in sorted(topic):
        print('* '+ x)

    print("Problems:")
    problem = 'Problem 1, Problem 2, Problem 3'
    problems = {topic[0]:problem, topic[1]:problem, topic[2]:problem, topic[3]:problem, topic[4]:problem,
                topic[5]:problem, topic[6]:problem}
    for x,y in problems.items():
        print('* '+x+' : '+y)

    print("Student Progress:")
    student_data = ('Nyari','[STARTED]','Adam','[GRADED]','Edd','[COMPLETED]')
    print('1. '+student_data[0]+' - '+topic[0]+' - '+'Problem 1'+' - '+student_data[1])
    print('2. '+student_data[2]+' - '+topic[1]+' - '+'Problem 2'+' - '+student_data[3])
    print('3. '+student_data[4]+' - '+topic[2]+' - '+'Problem 3'+' - '+student_data[5])
    pass

if __name__ == "__main__":
    create_outline()
