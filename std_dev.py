class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_age(self) -> int:
        return self.__age

def std_dev(person_list: list) -> float:
    if not person_list:
        return None

    total_age = sum(person.get_age() for person in person_list)
    mean_age = total_age / len(person_list)
    variance = sum((person.get_age() - mean_age) ** 2 for person in person_list) / len(person_list)
    return variance ** 0.5

# Example usage
if __name__ == "__main__":
    p1 = Person("Kyoungmin", 73)
    p2 = Person("Mercedes", 24)
    p3 = Person("Beatrice", 48)
    person_list = [p1, p2, p3]
    answer = std_dev(person_list)
    print(answer)  # Output: 20.00555
