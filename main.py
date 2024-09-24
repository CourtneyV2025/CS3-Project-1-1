trivia = { "q": "question", "a": "correct answer", "options": ["choice a", "choice b", "choice c", "choice d", "choice e", "choice f"]},

trivia = [
    {"question": ["How many presidents were born in Virginia?"],
        "answer": "eight",
        "options": ["one", "two", "four", "five", "seven", "eight", "eleven"]
     },
    { "question": "How many presidents were born in New York?",
        "answer": "five",
        "options": ["one", "two", "four", "five", "six", "ten"]
     },
    { "question": "How many presidents were born in Ohio?",
        "answer": "seven",
        "options": ["one", "two", "four", "five", "seven", "eight"]
     },
    { "question": "How many presidents were born in Texas?",
        "answer": "two",
        "options": ["one", "two", "four", "five", "seven", "eight"]
     },
    { "question": "How many presidents were born in Pennsylvania?",
        "answer": "two",
        "options": ["zero", "one", "two", "five", "seven", "eight"]
     },
    { "question": "How many presidents were born in Vermont?",
        "answer": "two",
        "options": ["zero", "two", "four", "five", "seven", "eight", ]
     },
    { "question": "How many presidents were born in Iowa?",
        "answer": "one",
        "options": ["zero", "one", "four", "five", "seven", "nine"]
     },
    { "question": "How many presidents were born in Illinois?",
        "answer": "one",
        "options": ["one", "three", "four", "six", "seven", "eight"]
     },
    { "question": "How many presidents were born in Massachussets?",
        "answer": "four",
        "options": ["one", "two", "four", "five", "seven", "nine"]
     },
    { "question": "How many presidents were born in North Carolina?",
        "answer": "two",
        "options": ["one", "two", "three", "six", "seven", "eight"]
     }
]

def ask_question(question, answer, options):
    # 1. Print out a question from the trivia list
    print(question)
    # 2. Print out the options (list)
    for option in options: 
            print(f" {option}")
    # 2. Get user input
    choice = input ("Enter answer: ")
    if choice.lower() == answer.lower():
         return True
    return False
    # 3. Check if choice matches correct answer 
       

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
    print(is_correct)
 
    # Update score accordingly
    if is_correct:
         score+=1
    print()


if __name__ == "__main__":
    main()
