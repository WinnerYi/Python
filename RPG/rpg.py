def create_character(name, STR, INT, CHA):
    if not isinstance(name, str):
        return "The character name should be a string"
    if " " in name:
        return "The character name should not contain spaces"
    if len(name) > 10:
        return "The character name is too long"
    if name == "":
        return "The character should have a name"
    if not (isinstance(STR, int) and isinstance(INT, int) and isinstance(CHA, int)):
        return "All stats should be integers"
    
    if STR < 1 or INT < 1 or CHA < 1:
        return "All stats should be no less than 1"
    
    if STR > 4 or INT > 4 or CHA > 4:
        return "All stats should be no more than 4"
    
   
    if STR + INT + CHA != 7:
        return "The character should start with 7 points"

    full_dot = '●'
    empty_dot = '○'
    
    STR_dots = full_dot * STR + empty_dot * (10 - STR)
    INT_dots = full_dot * INT + empty_dot * (10 - INT)
    CHA_dots = full_dot * CHA + empty_dot * (10 - CHA)
    
    return f"{name}\nSTR {STR_dots}\nINT {INT_dots}\nCHA {CHA_dots}"