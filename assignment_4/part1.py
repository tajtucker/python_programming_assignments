class University():
    def __init__(self, name, enrollment, urban):
        self.name = name
        self.enrollment = enrollment
        self.urban = urban

    def get_name(self):
        return self.name
    
    def get_enrollment(self):
        return self.enrollment
    
    def get_urban(self):
        return self.urban
    
    def set_name(self, new_name):
        self.name = new_name

    def set_enrollment(self, new_enrollment):
        if new_enrollment > 0:
            self.enrollment = new_enrollment
        else:
            self.enrollment = 0
            print(" “Enrollment must be a positive number.")
    
    def set_urban(self, is_urban):
        self.urban = is_urban
    
    def print_details(self):
        print(self.name, self.enrollment, self.urban)

    def compare_enrollment(self, other_university):
        if self.enrollment > other_university.enrollment:
            return self.name
        else:
            return other_university.name
    

tsu = University("TSU", 8000, True)
vanderbilt = University("Vanderbilt", 12000, True)
fisk = University("Fisk", 1500, True)

tsu.print_details()
vanderbilt.print_details()
fisk.print_details()

tsu.set_enrollment(9000)
vanderbilt.set_enrollment(-5000)
fisk.set_enrollment(2000)

tsu.print_details()
vanderbilt.print_details()
fisk.print_details()

comparison_tsu_vanderbilt = tsu.compare_enrollment(vanderbilt)
print("Comparison between TSU and Vanderbilt:")
print(comparison_tsu_vanderbilt)