﻿# Your name: Violetta Wang
# Your student id: 24666655
# Your email: zhiyew@umich.edu
# List who you have worked with on this homework: 


# import the random module for use in this program
import random

# Create the class Magic8Ball
class Magic8Ball():

    # Create the constructor (__init__) method
    # Argument: A set of possible answers (a list)
    # Return: None
    #
    # The method (1) sets this object's answer_list (instance variable) to the passed list of possible answers (the argument of the method),
    # (2) sets this object's question_history_list (instance variable) to an empty list,
    # (3) and sets this object's answer_history_list (instance variable) to an empty list.

    # YOUR ANSWER HERE
    def __init__(self, answer_set):
        self.answer_list = answer_set
        self.question_history_list = []
        self.answer_history_list = []



    # Create the __str__ method
    # Argument: None
    # Return: a string, with all the answers in the answer_list separated by commas
    #
    # For example: 
    # for answer list ['Yes', 'No', 'Maybe'], it should return a string, "['Yes', 'No', 'Maybe']"

    # YOUR ANSWER HERE
    def __str__(self):
        all_answer = ""
        for answer in self.answer_list:
            all_answer = all_answer + answer + ", "
        return all_answer


    # Create the get_random_answer method
    # Argument: None
    # Return: an answer (string) in the answer_list
    #
    # This method randomly picks an answer from the answer list.
    # It first randomly chooses an index and appends that index to the answer_history_list.
    # Then it returns the answer at the randomly picked index.

    # YOUR ANSWER HERE
    def get_random_answer(self):
        num = random.randint(0, len(self.answer_list)-1)
        self.answer_history_list.append(self.answer_list[num])
        return self.answer_list[num]


    # Create the shake method 
    # Argument: A question (string)
    # Return: An answer (string)
    #
    # The method takes a question and first checks if the question is already in the question_history_list.
    # If so, it returns a string, "I've already answered that question”
    # Otherwise, it adds the question to the question_history_list and
    #               returns the answer from get_random_answer.

    # YOUR ANSWER HERE
    def shake(self, question):
        for questions in self.question_history_list:
            if questions == question:
                return "I've already answered that question"

        self.question_history_list.append(question)
        return self.get_random_answer()
            


    # Create the print_question_history method
    # Argument: None
    # Return: None
    #
    # If there are no items in the answer_history_list, it prints "None yet"
    # Otherwise, 
    # the method prints "[answer index] question - answer" for each of the indices in the answer_history_list,
    #  each on a separate line.

    # YOUR ANSWER HERE
    def print_question_history(self):
        if answer_history_list == []:
            print("None yet")
        else:
            for answers in answer_history_list:
                number = self.answer_history_list.index(answers)
                print(f"[{number}] {self.question_history_list[number]} - {self.answer_history_list[number]} \n")


    # EXTRA POINTS
    # Create the answer_frequency method.
    # It takes as an argument: n, an integer
    # 
    # (1) It calls get_random_answer an 'n' number of times and records the random answer in a list.
    # (2) It then prints the frequency of each answer in each line.
    #   For example, it will print
    # Definitely: 27
    # Most likely: 32
    # It is certain: 25
    #   ... and so on.
    # (3) It prints whether the most common answer was "affirmative", "negative", or "neither affirmative nor negative".
    #    Please feel free to use the pre-defined lists of 
    #           affirmative = ["Definitely", "Most likely", "It is certain"]
    #           nagative = ["Very doubtful", "Don't count on it", "No"]

    def answer_frequency(self, n):
        # YOUR ANSWER BELOW

        # affirmative = ["Definitely", "Most likely", "It is certain"]
        # nagative = ["Very doubtful", "Don't count on it", "No"]

        print()
        # if [SOME_CONDITION]:
        #     print("The most common answer was affirmative.")
        # elif [SOME_CONDITION]:
        #     print("The most common answer was negative.")
        # else:
        #     print("The most common answer was neither affirmative nor negative.")




def main():
    answer_list = ["Definitely",
    "Most likely", 
    "It is certain", 
    "Maybe", 
    "Cannot predict now",
    "Very doubtful",
    "Don't count on it", 
    "No",
    ]
    magic8ball = Magic8Ball(answer_list)

    # Get the first question or quit
    prompt = "Ask a question or type quit:"
    ans = input(prompt)


    # Loop while question is not "quit"
    while ans != "quit":
        random_answer = magic8ball.shake(ans)
        
        print(f"{ans} - {random_answer}")

        ans = input("Ask a question or type quit:")
        # shake the ball and get an answer

        # print question - answer

        # get the next question or quit 


def test():
    answer_list = ["Definitely",
    "Most likely", 
    "It is certain", 
    "Maybe",
    "Cannot predict now",
    "Very doubtful",
    "Don't count on it", 
    "No",
    ]

    print("================================")
    print("Testing Magic 8 Ball:")
    bot = Magic8Ball(answer_list)

    print("* Testing the __str__ method")
    print(bot)
    print()

    print("* Printing the history when no answers have been generated yet")
    bot.print_question_history()
    print()

    print("* Asking the Question: Will I pass this semester?")
    print(bot.shake("Will I pass this semester?"))
    print()

    print("* Asking the Question: Should I study today?")
    print(bot.shake("Should I study today?"))
    print()

    print("* Asking the Question: Should I study today? (again)")
    print(bot.shake("Should I study today?"))
    print()

    print("* Asking the Question: Is SI 206 the best class ever?")
    print(bot.shake("Is SI 206 the best class ever?"))
    print()

    print("================================")
    print("* Printing the history")
    bot.print_question_history()
    print()

    # EXTRA POINTS
    # Uncomment the lines below if you attempt the extra credit!
    # print("* Testing answer_frequency method with 200 responses")
    # bot.answer_frequency(200)


# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    # test() #TODO: Uncomment when you are ready to test your Magic8Ball class