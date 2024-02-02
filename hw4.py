# TASK 1

fh = open("C:/Users/HP/Desktop/goit/My repo/goit-algo-hw-04/salary.txt", "w")
fh.write(
    "Jonathan Johnson,1086\nLinda Wells,3989\nLaura Nelson,3738\nJeffrey Rodriguez,2193\nMonica Miller,2405\nAllison Smith,3647\nJasmine Wright,1749\nTyler Brown,2404\nJames Dean,3297\nCody Hess,3691"
)
fh.close()


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            total = 0
            for line in lines:
                salary = int(line.split(",")[1].strip())
                total += salary

            average = total / len(lines) if len(lines) > 0 else 0

            return total, average

    except FileNotFoundError:
        print(f"File with {path} is not found.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


result = total_salary("C:/Users/HP/Desktop/goit/My repo/goit-algo-hw-04/salary.txt")
if result:
    total, average = result
    print(f"Total sum of salary is: {total}, Average salary is: {average}")
else:
    print("Failed to calculate salary.")


# TASK 2
import json


def get_cats_info(path):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(",")

                cat_info = {"id": cat_id, "name": cat_name, "age": int(cat_age)}

                cats_list.append(cat_info)

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_list


# Example usage:
cats_info = get_cats_info(
    "C:/Users/HP/Desktop/goit/My repo/goit-algo-hw-04/cat_info.txt"
)
print(json.dumps(cats_info, indent=4))
