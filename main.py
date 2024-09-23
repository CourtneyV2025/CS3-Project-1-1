trivia = { "q": "question", "a": "correct answer", "options": ["choice a", "choice b", "choice c", "choice d", "choice e", "choice f"]},

trivia = [
    {"question": ["How many presidents were born in Virginia?"],
        "answer": 8,
        "options": [1, 2, 4, 5, 7, 8, 11]
     },
    { "question": "How many presidents were born in New York?",
        "answer": 5,
        "options": [1, 2, 4, 5, 6, 10]
     },
    { "question": "How many presidents were born in Ohio?",
        "answer": 7,
        "options": [1, 2, 4, 5, 7, 8]
     },
    { "question": "How many presidents were born in Texas?",
        "answer": 2,
        "options": [1, 2, 4, 5, 7, 8]
     },
    { "question": "How many presidents were born in Pennsylvania?",
        "answer": 2,
        "options": [0, 1, 2, 5, 7, 8]
     },
    { "question": "How many presidents were born in Vermont?",
        "answer": 2,
        "options": [0, 2, 4, 5, 7, 8, 9]
     },
    { "question": "How many presidents were born in Iowa?",
        "answer": 1,
        "options": [0, 1, 4, 5, 7, 9]
     },
    { "question": "How many presidents were born in Illinois?",
        "answer": 1,
        "options": [1, 3, 4, 6, 7, 8]
     },
    { "question": "How many presidents were born in Massachussets?",
        "answer": 4,
        "options": [1, 2, 4, 5, 7, 9]
     },
    { "question": "How many presidents were born in North Carolina?",
        "answer": 2,
        "options": [1, 2, 3, 6, 7, 8]
     }
]


def ask_question(question, answer, options):
    # 1. Print out a question from the trivia list

    # 2. Print out the options (list)

    # 2. Get user input
        #choice = input("Your answer:")
        #print(choice)

    # 3. Check if choice matches correct answer 
    return False

# Main method for game loop 
def main():
    print("Let's play 🇺🇸 US Presidents 🇺🇸 Trivia!! ")
    score = 0

    current = trivia[0] #dictionary
    # Get data from that item
    q = current["question"]
    a = current["answer"]
    ops = current["options"]
    # Pass in q, a, and options into ask_question
    is_correct = ask_question(q, a, ops)
    print(q, a, ops)

    # Update score accordingly



if __name__ == "__main__":
    main()
