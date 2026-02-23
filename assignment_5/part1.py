class University:
    def __init__(self, name, enrollment, urban):
        self.name = name
        self.enrollment = None
        self.set_enrollment(enrollment)
        self.urban = urban
    
    def set_enrollment(self, new_enrollment):
        if 1 <= new_enrollment <= 200000:
            self.enrollment = new_enrollment
        else:
            print("Warning: Enrollment must be between 1 and 200,000!")
        
    def get_details(self):
        return (f"University Name: {self.name}. University Enrollment: {self.enrollment}. University Urban: {self.urban}.")
    
class TSU(University):
    def __init__(self, location, numberOfCampuses):
        super().__init__("TSU", 8000, True)
        self.location = location
        self.numberOfCampuses = None
        self.set_numberOfCampuses(numberOfCampuses)
    
    def set_numberOfCampuses(self, new_numberOfCampuses):
        if new_numberOfCampuses >= 0:
            self.numberOfCampuses = new_numberOfCampuses
        else:
            print("Warning: Number of Campuses must be non-negative!")
    
    def get_details(self):
        return (f"University Name: {self.name}. University Enrollment: {self.enrollment}. University Urban: {self.urban}. Campus Location: {self.location}. Number of Campuses: {self.numberOfCampuses}.")

class Vanderbilt(University):
    def __init__(self, numberOfColleges):
        super().__init__("Vanderbilt", 10000, True)
        self.numberOfColleges = None
        self.set_numberOfColleges(numberOfColleges)
    
    def set_numberOfColleges(self, new_numberOfColleges):
        if new_numberOfColleges >= 0:
            self.numberOfColleges = new_numberOfColleges
        else:
            print("Warning: Number of Colleges must be non-negative!")
    
    def get_details(self):
        return (f"University Name: {self.name}. University Enrollment: {self.enrollment}. University Urban: {self.urban}. Number of Colleges: {self.numberOfColleges}")


tsu = TSU("Nashville", 3)
print(tsu.get_details())

vandy = Vanderbilt(10)
print(vandy.get_details())

tsu.set_enrollment(9500)
print(tsu.get_details())

vandy.set_enrollment(12000)
print(vandy.get_details())