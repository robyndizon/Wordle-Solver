import random

# list of possible words (5 letters) for AI guesses
word_list = ["about", "alert", "argue", "beach", "above", "alike", "arise", "began", "abuse", "alive", "array", "begin", 
             "actor", "allow", "aside", "begun", "acute", "alone", "asset", "being", "admit", "along", "audio", "below", 
             "adopt", "alter", "audit", "bench", "adult", "among", "avoid", "billy", "after", "anger", "award", "birth", 
             "again", "angle", "aware", "black", "agent", "angry", "badly", "blame", "agree", "apart", "baker", "blind", 
             "ahead", "apple", "bases", "block", "alarm", "apply", "basic", "blood", "album", "arena", "basis", "board", 
             "boost", "buyer", "china", "cover", "booth", "cable", "chose", "craft", "bound", "calif", "civil", "crash", 
             "brain", "carry", "claim", "cream", "brand", "catch", "class", "crime", "bread", "cause", "clean", "cross", 
             "break", "chain", "clear", "crowd", "breed", "cause", "chair", "click", "crown", "brief", "chart", "clock", 
             "curve", "bring", "chase", "close", "cycle", "broad", "cheap", "coach", "daily", "broke", "check", "coast", 
             "dance", "brown", "chest", "could", "dated", "build", "chief", "count", "dealt", "built", "child", "court", 
             "death", "debut", "entry", "forth", "group", "delay", "equal", "forty", "grown", "depth", "error", "forum", 
             "guard", "doing", "event", "found", "guess", "doubt", "every", "frame", "guest", "dozen", "exact", "frank", 
             "guide", "draft", "exist", "fraud", "happy", "drama", "extra", "fresh", "harry", "drawn", "faith", "front", 
             "dream", "false", "fruit", "heavy", "dress", "fault", "fully", "hence", "drill", "fibre", "funny", "night", 
             "drink", "field", "giant", "horse", "drive", "fifth", "given", "hotel", "drove", "fifty", "glass", "house", 
             "dying", "fight", "globe", "human", "eager", "final", "going", "ideal", "early", "first", "grace", "image", 
             "earth", "fixed", "grade", "index", "eight", "flash", "grand", "inner", "elite", "fleet", "grant", "input", 
             "empty", "floor", "grass", "issue", "enemy", "fluid", "great", "irony", "enjoy", "focus", "green", "juice", 
             "enter", "force", "gross", "joint", "judge", "metal", "media", "newly", "known", "local", "might", "noise", 
             "label", "logic", "minor", "north", "large", "loose", "minus", "noted", "laser", "lower", "mixed", "novel", 
             "later", "lucky", "model", "nurse", "laugh", "lunch", "money", "occur", "layer", "lying", "month", "ocean", 
             "learn", "magic", "moral", "offer", "lease", "major", "motor", "often", "least", "maker", "mouse", "other", 
             "legal", "music", "mouth", "ought", "level", "match", "movie", "paint", "light", "mayor", "needs", "paper", 
             "limit", "meant", "never", "party", "peace", "power", "radio", "round", "panel", "press", "raise", "route", 
             "phase", "price", "range", "royal", "phone", "pride", "rapid", "rural", "photo", "prime", "ratio", "scale", 
             "piece", "print", "reach", "scene", "pilot", "prior", "ready", "scope", "pitch", "prize", "refer", "score", 
             "place", "proof", "right", "sense", "plain", "proud", "rival", "serve", "plane", "prove", "river", "seven", 
             "plant", "queen", "quick", "shall", "plate", "sixth", "stand", "shape", "point", "quiet", "roman", "share", 
             "pound", "quite", "rough", "sharp", "sheet", "spare", "style", "times", "shelf", "speak", "sugar", "tired", 
             "shell", "speed", "suite", "title", "shift", "spend", "super", "today", "shirt", "spent", "sweet", "topic", 
             "shock", "split", "table", "total", "shoot", "spoke", "taken", "touch", "short", "sport", "taste", "tough", 
             "shown", "staff", "taxes", "tower", "sight", "stage", "teach", "track", "since", "stake", "teeth", "trade", 
             "sixty", "start", "texas", "treat", "sized", "state", "thank", "trend", "sleep", "steel", "their", "tried", 
             "slide", "stick", "theme", "tries", "small", "still", "there", "truck", "smart", "stock", "these", "truly", 
             "smile", "stone", "thick", "trust", "smith", "stood", "thing", "truth", "smoke", "store", "think", "twice", 
             "solid", "storm", "third", "under", "solve", "story", "those", "undue", "sorry", "strip", "three", "union", 
             "whose", "watch", "write", "usage", "woman", "water", "wrong", "usual", "train", "wheel", "wrote", "valid", 
             "world", "where", "yield", "value", "worry", "which", "young", "video", "worse", "while", "youth", "virus", 
             "worst", "white", "worth", "visit", "would", "vital", "voice"]

# Function to give feedback based on AI guess
def give_feedback(secret_word, guess):
    feedback = []
    secret_word_list = list(secret_word)
    guess_list = list(guess)

    # First, mark correct letters in the correct position (green)
    for i in range(5):
        if guess_list[i] == secret_word_list[i]:
            feedback.append("🟩")  # Green
            secret_word_list[i] = None  # Mark as used
            guess_list[i] = None  # Mark as used
        else:
            feedback.append("⬛️")  # Blank for now

   # Check for correct letters in the wrong position (yellow)
    for i in range(5):
        # Check if the letter in guess_list is not None and is in the secret word
        if guess_list[i] is not None:
            # Check if the letter is in the secret word
            for letter in secret_word_list:
                if letter == guess_list[i]:
                    feedback[i] = "🟨"  # Set feedback to "Y" for yellow
                    # Replace that letter in secret_word_list with None to mark it as used
                    secret_word_list[secret_word_list.index(letter)] = None
                    break  # Stop searching after we replace the letter

    # Return the feedback as a string instead of list
    return feedback[0] + feedback[1] + feedback[2] + feedback[3] + feedback[4]



# Function to provide a hint (letter and its position in the word)
def give_hint(secret_word):
    index = random.choice(range(5))  # Randomly choose a letter position          
    return secret_word[index], index  # Return the letter and its index

# Function for AI to make smarter guesses
def ai_guess_word(secret_word):
    possible_words = word_list[:]  # Start with all words in the word_list
    guesses = 0
    feedback_history = []

    print("AI's Guessing Process:")

    while guesses < 6:
        # AI selects the next word by maximizing feedback elimination
        guess = random.choice(possible_words)  # Initial random guess           
        
        # Get feedback from the guess
        feedback = give_feedback(secret_word, guess)
        feedback_history.append((guess, feedback))

        print("AI Guess #" + str(guesses + 1) + ": " + guess + " | Feedback: " + feedback)
        
        # If AI guesses correctly
        if feedback == "🟩🟩🟩🟩🟩":
            print("AI guessed the word: " + guess)
            return

        # Narrow down possible words based on feedback
        new_possible_words = []
        for word in possible_words:
            match = True
            for guess, feedback in feedback_history:
                if give_feedback(word, guess) != feedback:
                    match = False
                    break
            if match:
                new_possible_words.append(word)
        possible_words = new_possible_words
        
        print("Possible words remaining: " + str(len(possible_words)))

        guesses += 1

    print("AI couldn't guess the word in 6 attempts. The word was: " + secret_word)

# Main game loop
def play_wordle():
    mode = input("Choose your mode: 1 for Player vs Wordle, 2 for Wordle vs AI: ")

    if mode == '1' or mode == '2':
        print("Mode " + str(mode) + " selected.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
    secret_word = random.choice(word_list)  # Select a secret word at random           

    if mode == "1":
        print("You are guessing the word.")
        attempts = 6
        hint_used = False

        for attempt in range(attempts):
            guess = input("Attempt " + str(attempt+1) + ": Enter your 5-letter guess: ").lower()
            
            # Check if the guess is exactly 5 letters
            while len(guess) != 5:
                guess = input("Invalid guess! Please enter a valid 5-letter word: ").lower()

            feedback = give_feedback(secret_word, guess)
            print("Feedback: ", feedback)

            if feedback == "🟩🟩🟩🟩🟩":
                print("Congratulations! You've guessed the word.")
                break

            if not hint_used and input("Do you want a hint? (y/n): ").lower() == "y":
                hint = give_hint(secret_word)
                print("Hint: The letter '" + hint[0] + "' is at position " + str(hint[1] + 1))
                hint_used = True

        else:  # This else corresponds to the for-loop and will execute if the loop ends without a break (i.e., player didn't guess the word)
            print("Sorry, you've used all your attempts. The word was: " + secret_word + ". You can try again next time!")

    elif mode == "2":
        print("AI is guessing the word.")
        ai_guess_word(secret_word)





play_wordle()
