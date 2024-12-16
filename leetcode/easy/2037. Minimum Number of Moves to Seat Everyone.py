class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        res = 0
        for seat in seats:
            for student in students:
                if seat == student:
                    while seat in seats and student in students:
                        seats.remove(seat)
                        students.remove(student)

        for _ in range(len(seats)):
            if max(seats) > max(students):
                res += max(seats) - max(students)
                seats.remove(max(seats))
                students.remove(max(students))

            else:
                res += max(students) - max(seats)
                seats.remove(max(seats))
                students.remove(max(students))

        return res