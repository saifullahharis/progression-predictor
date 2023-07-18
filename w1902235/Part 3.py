# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20212163 / w1902235
# Date: 15_07_2023


count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0

file = open("Datafile.txt", 'w')


def outcome():
    global count_progress, count_trailer, count_retriever, count_exclude  
    if pass_credit == 120:
        file.write("Progress - "+str(pass_credit)+", "+str(defer_credit)+", "+str(fail_credit))
        count_progress += 1
        print("Progress")                               # progress
    elif pass_credit == 100:
        file.write("Progress (module trailer) - " + str(pass_credit)+", " + str(defer_credit)+", " + str(fail_credit))
        count_trailer += 1
        print("Progress (module trailer)")              # module Trailer
    elif pass_credit <= 80 and defer_credit <= 120 and fail_credit <= 60:
        file.write("module retriever - " + str(pass_credit)+", " + str(defer_credit)+", " + str(fail_credit))
        count_retriever += 1
        print("Do not progress – module retriever")     # Module retriever
    elif pass_credit <= 40 and defer_credit <= 40 and fail_credit <= 120:
        file.write("Exclude - " + str(pass_credit)+", " + str(defer_credit)+", " + str(fail_credit))
        count_exclude += 1
        print("Exclude")                                # Exclude

    file.write('\n')     # new line

    print()


def histogram():
    print("-" * 80) 

    print(f"""
Histogram
Progress {count_progress}  : {count_progress*"*"}
Trailer {count_trailer} : {count_trailer*"*"}          
Retriever {count_retriever} : {count_retriever*"*"}          
Excluded {count_exclude} : {count_exclude*"*"}

{count_progress + count_trailer + count_retriever + count_exclude} outcomes in total. 
    """)
          
    print("-" * 80)


while True:
    while True:
        try:
            pass_credit = int(input("Enter your total PASS credits : "))
            if pass_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")
    while True:
        try:
            defer_credit = int(input("Enter your total DEFER credits : "))
            if defer_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")
    while True:
        try:
            fail_credit = int(input("Enter your total FAIL credits : "))
            if fail_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")
    if pass_credit + defer_credit + fail_credit == 120:
        outcome()

        answer = input("""
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and display final outcome :""")
        if answer == "q":       # click q this will break from this part
            histogram()
            file.close()
            
            file = open("Datafile.txt", 'r')
            print(file.read())
            
            break
        elif answer == "y":
            continue
        else:
            print("Please enter a valid input")
        
    else:
        print("Total Incorrect")
