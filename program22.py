class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    # Method to display time in HH:MM:SS format
    def display(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    # Overload '+' operator to add two Time objects
    def __add__(self, other):
        if isinstance(other, Time):
            # Sum seconds, minutes, and hours
            total_seconds = self.__second + other.__second
            total_minutes = self.__minute + other.__minute + total_seconds // 60
            total_hours = self.__hour + other.__hour + total_minutes // 60

            # Calculate final hours, minutes, seconds
            final_seconds = total_seconds % 60
            final_minutes = total_minutes % 60
            final_hours = total_hours % 24  # 24-hour format

            return Time(final_hours, final_minutes, final_seconds)
        return NotImplemented

# Example usage
t1 = Time(2, 45, 50)
t2 = Time(1, 20, 30)

t3 = t1 + t2

print("Time 1:", t1.display())
print("Time 2:", t2.display())
print("Sum of Time 1 and Time 2:", t3.display())