def hello():
    return "Hello!"

def greet(name):
    return "Hello, " + name +  "!"

def calc(num1, num2, operation="multiply"):
    try:
        if operation == "add":
            result = num1 + num2
            return result
        elif operation =="subtract":
            result = num1 - num2
            return result
        elif operation == "multiply":
            result = num1 * num2  
            return result
        elif operation == "divide":
            if num2 == 0:  
                return "You can't divide by 0!"
            result = num1 / num2  
            return result
        elif operation == "int_divide":
            if num2 == 0:
                return "You can't divide by 0!"
            return num1 // num2
        elif operation == "power":
            return num1 ** num2
        elif operation == "modulo":
            result = num1 % num2  
            return result
        else:
            result = num1 * num2  
            return result
        
    except:
        message = "You can't " + operation + " those values!"
        return message


def data_type_conversion(value, target_type):
    try:
        if target_type =="int":
            converted_value = int(value)
            return converted_value
        elif target_type == "float":
            converted_value = float(value)
            return converted_value
        elif target_type == "str":
            converted_value = str(value)
            return converted_value
    except:
        error_message = "You can't convert " + str(value) + " into a " + target_type + "."
        return error_message    
    
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."
    
def repeat(string, times):
    result = ""
    for i in range(times):
        result = result + string
    return result

def student_scores(operation, *args, **kwargs):
    if operation == "mean":
        total = 0
        count = 0
        for key, value in kwargs.items():
            total += value
            count += 1
        average = total / count
        return average
    elif operation == "best":
        best_student = ""
        highest_score = 0
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key
        return best_student

def titleize(text):
    small_words = ["and", "or", "the", "a", "an", "of", "is", "in"]
    words = text.split()
    result_words =[]

    for i in range(len(words)):
        word = words[i]
        if i == 0 or word.lower() not in small_words:
            first_letter = word[0].upper()
            rest_of_word = word[1:].lower()
            titled_word = first_letter + rest_of_word
            result_words.append(titled_word)
        else:
            titled_word = word.lower()
            result_words.append(titled_word)

    result = " ".join(result_words)
    return result

def hangman(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters: 
            result = result + letter  
        else:
            result = result + "_"
    return result


def pig_latin(text):
    words = text.split()
    pig_words = []
    
    for word in words:
        word = word.lower()
        first_letter = word[0]
        
        if first_letter in "aeiou":
            pig_word = word + "ay" 
        else:
            vowel_position = -1
            for i in range(len(word)):
                if word[i] in "aeiou":
                    vowel_position = i
                    break

            if word.startswith("qu"):
                vowel_position = 2
            elif vowel_position > 0 and word[vowel_position-1:vowel_position+1] == "qu":
                vowel_position = vowel_position + 1
            
            if vowel_position == -1:
                pig_word=word+"ay"
            else:
                consonants = word[:vowel_position]
                rest = word[vowel_position:]
                pig_word = rest + consonants + "ay"  
        
        pig_words.append(pig_word)

    result = " ".join(pig_words)
    return result
