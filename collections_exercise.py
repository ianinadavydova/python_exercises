def return_day_or_index(day_or_index):
    days = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7}

    if day_or_index in days.values():
        for i in days.keys():
            if days[i] == day_or_index:
                return i
    elif day_or_index in days.keys():
        return days.get(day_or_index)


print(return_day_or_index("Tuesday"))

# exercise 2
grades = {
    "Anna": 5,
    "Peter": 4,
    "Viktoria": 5,
    "Harry": 3,
    "Daria": 4,
    "Yana": 5
}


def return_grades_counts(grades_dic):
    counts = {}
    for grade in grades_dic.values():
        counts[grade] = counts.get(grade, 0) + 1
    return counts

# exercise 3
def find_lesson_days(lesson):
    schedule = {
        1: ["math", "informatics", "literature"],
        2: ["english", "history", "gym"],
        3: ["math", "physics", "informatics"],
        4: ["chemistrry", "biology", "english"],
        5: ["german", "literature", "math"]
    }

    day_names = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
    }

    days_found = []
    for day_num, lessons in schedule.items():
        if lesson.lower() in [l.lower() for l in lessons]:
            days_found.append(day_names[day_num])

    if days_found:
        return days_found
    else:
        return f"Lesson '{lesson}' not found in the schedule."

