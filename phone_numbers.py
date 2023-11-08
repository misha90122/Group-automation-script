def extract_operators(phone_numbers):
    life_numbers = []
    kyivstar_numbers = []
    other_numbers = []

    for number in phone_numbers:
        # Враховуємо номери без ком і знаку "+"
        number = number.replace(",", "").replace("+", "")

        if number.startswith("38063") or number.startswith("38093") or number.startswith("38073"):
            life_numbers.append(number)
        elif number.startswith("38067") or number.startswith("38068") or number.startswith("38096") or number.startswith("38097") or number.startswith("38098") or number.startswith("38039"):
            kyivstar_numbers.append(number)
        else:
            other_numbers.append(number)

    return life_numbers, kyivstar_numbers, other_numbers


def read_phone_numbers_from_file(file_path):
    with open(file_path, "r") as file:
        phone_numbers = file.readlines()
    return [number.strip() for number in phone_numbers]


def save_numbers_to_file(numbers, file_path):
    with open(file_path, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")


if __name__ == "__main__":
    input_file_path = "input.txt"  # Шлях до вхідного файлу з номерами
    life_file_path = "life_numbers.txt"  # Шлях до файлу для зберігання номерів Life
    kyivstar_file_path = "kyivstar_numbers.txt"  # Шлях до файлу для зберігання номерів Kyivstar
    other_file_path = "other_numbers.txt"  # Шлях до файлу для зберігання інших номерів

    phone_numbers = read_phone_numbers_from_file(input_file_path)
    life_numbers, kyivstar_numbers, other_numbers = extract_operators(phone_numbers)

    save_numbers_to_file(life_numbers, life_file_path)
    save_numbers_to_file(kyivstar_numbers, kyivstar_file_path)
    save_numbers_to_file(other_numbers, other_file_path)

    print("Операція завершена. Номери розділені та збережені у відповідні файли.")