#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

class NewYearResolution:
    def __init__(self, resolution, category, completion_date):
        self.resolution = resolution
        self.category = category
        self.completion_date = completion_date
        self.info = [resolution, category, completion_date]



class ResolutionList:
    def __init__(self):
        self.resolutions = ['']

    def add_resolution(self, resolution, category, completion_date):
        self.resolutions.append(NewYearResolution(resolution, category, completion_date))


if __name__ == "__main__":
    r = ResolutionList()
    r.add_resolution("Exercite-se regularmente","Saúde", "2024-03-31")
    response = r.resolutions[1]
    print(response.info)
