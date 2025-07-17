def total_salary(path):
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Видаляємо зайві пробіли та символи нових рядків
                if line:  # Якщо рядок не порожній
                    name, salary = line.split(',')
                    total += float(salary)  # Додаємо заробітну плату до загальної суми
                    count += 1  # Збільшуємо лічильник розробників
        
        if count == 0:
            return (0, 0)  # Якщо в файлі немає даних

        average = total / count  # Обчислюємо середню зарплату
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except ValueError:
        print("Невірний формат даних у файлі.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Приклад використання
total, average = total_salary("D:/Таня/Projects/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
