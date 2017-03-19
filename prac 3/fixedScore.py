def main():
    print(get_result())

def get_result():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()