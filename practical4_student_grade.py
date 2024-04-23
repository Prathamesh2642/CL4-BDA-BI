#this program runs on terminal
#this program requires an extra file - practical4.txt 
#open the terminal in the path where this file is stored 
#in the terminal write the following command
#  python practical4_student_grade.py practical4.txt

from mrjob.job import MRJob #module for map-reduce

class GradeCalculator(MRJob):

    def mapper(self, _, line):
        # Split the input line into name and score
        name, score = line.split(',')
        score = int(score)

        # Emit the name and score
        yield name, score

    def reducer(self, key, values):
        # Calculate the average score
        total_score = 0
        num_scores = 0
        for score in values:
            total_score += score
            num_scores += 1
        average_score = total_score / num_scores

        # Determine the grade based on the average score
        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        # Emit the name and grade
        yield key, grade

if __name__ == '__main__':
    GradeCalculator.run()
