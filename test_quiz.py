import random
import os
import hashlib

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def generate_hex_number(length):
    """Generál egy hexadecimális számot a megadott hosszal."""
    hex_digits = "0123456789ABCDEF"
    return ''.join(random.choice(hex_digits) for _ in range(length))

def generate_quiz(num_questions=30):
    questions = []
    for i in range(num_questions):
        length = random.choice([2, 3, 4])  # Véletlenszerűen 2, 3 vagy 4 karakter
        hex_num = generate_hex_number(length)
        questions.append((i + 1, hex_num, hex_to_dec(hex_num)))  # (sorszám, hex szám, dec válasz)
    return questions

def calculate_checksum(content):
    """Kiszámolja a tartalom SHA-256 checksum-ját."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def save_quiz_to_file(questions, filename='quiz.txt'):
    content = ""
    for i, hex_num, _ in questions:
        content += f"{i}. 0x{hex_num} = \n"
    
    # Hozzáadjuk a teljes elérési utat a tartalomhoz
    full_path = os.path.abspath(__file__)
    content += f"Full path: {full_path}\n"
    
    # Kiszámoljuk a checksum-ot (csak a hexadecimális számokra és az elérési útvonalra)
    checksum_content = ""
    for _, hex_num, _ in questions:
        checksum_content += hex_num + "\n"
    checksum_content += full_path + "\n"
    
    checksum = calculate_checksum(checksum_content)
    content += f"Checksum: {checksum}\n"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

pwd = os.getcwd()

if not os.path.exists('quiz.txt'):
    quiz_questions = generate_quiz()
    save_quiz_to_file(quiz_questions)

def load_quiz(filename='quiz.txt'):
    """
    Beolvassa a quiz.txt fájlt, és visszaadja a hexadecimális számokat és a diák által megadott válaszokat.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    questions = []
    checksum_content = ""
    for line in lines:
        if not line.strip():  # Üres sorok kihagyása
            continue
        
        # Feladat sor feldolgozása (pl. "1. 0xFF11 = 123")
        if line.startswith("Checksum:") or line.startswith("Full path:"):
            continue
        
        parts = line.split("=")
        question_part = parts[0].strip()  # "1. 0xFF11"
        student_answer = parts[1].strip() if len(parts) > 1 else ""  # Diák válasza
        
        # Hexadecimális szám kinyerése
        hex_num = question_part.split("0x")[1].strip()
        checksum_content += hex_num + "\n"
        
        questions.append((hex_num, student_answer))
    
    # Beolvassuk az elérési utat
    full_path_line = [line for line in lines if line.startswith("Full path:")]
    if full_path_line:
        full_path = full_path_line[0].split(":")[1].strip()
        checksum_content += full_path + "\n"
    
    # Beolvassuk a checksum-ot
    checksum_line = [line for line in lines if line.startswith("Checksum:")]
    if checksum_line:
        stored_checksum = checksum_line[0].split(":")[1].strip()
    else:
        stored_checksum = None
    
    # Újraszámoljuk a checksum-ot
    calculated_checksum = calculate_checksum(checksum_content)
    
    # Ellenőrizzük a checksum-ot
    if stored_checksum != calculated_checksum:
        raise ValueError("Checksum mismatch! A fájl tartalma megváltozott!")
    
    return questions

# Beolvassuk a kérdéseket és válaszokat
questions = load_quiz()

# Manuálisan definiáljuk a 30 tesztfüggvényt
def test_question_1():
    hex_num, student_answer = questions[0]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_2():
    hex_num, student_answer = questions[1]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_3():
    hex_num, student_answer = questions[2]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

# Folytasd a tesztfüggvények definiálását...
def test_question_4():
    hex_num, student_answer = questions[3]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_5():
    hex_num, student_answer = questions[4]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_6():
    hex_num, student_answer = questions[5]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_7():
    hex_num, student_answer = questions[6]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_8():
    hex_num, student_answer = questions[7]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_9():
    hex_num, student_answer = questions[8]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_10():
    hex_num, student_answer = questions[9]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_11():
    hex_num, student_answer = questions[10]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_12():
    hex_num, student_answer = questions[11]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_13():
    hex_num, student_answer = questions[12]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_14():
    hex_num, student_answer = questions[13]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_15():
    hex_num, student_answer = questions[14]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_16():
    hex_num, student_answer = questions[15]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_17():
    hex_num, student_answer = questions[16]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_18():
    hex_num, student_answer = questions[17]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_19():
    hex_num, student_answer = questions[18]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_20():
    hex_num, student_answer = questions[19]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_21():
    hex_num, student_answer = questions[20]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_22():
    hex_num, student_answer = questions[21]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_23():
    hex_num, student_answer = questions[22]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_24():
    hex_num, student_answer = questions[23]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_25():
    hex_num, student_answer = questions[24]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_26():
    hex_num, student_answer = questions[25]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_27():
    hex_num, student_answer = questions[26]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_28():
    hex_num, student_answer = questions[27]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_29():
    hex_num, student_answer = questions[28]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"

def test_question_30():
    hex_num, student_answer = questions[29]
    correct_answer = hex_to_dec(hex_num)
    assert student_answer.isdigit(), "A válasz nem szám!"
    assert int(student_answer) == correct_answer, "Hibás válasz!"