


# !Create job boarding application
# Write a job boarding application that has the following Requirements
# TODO1. Prompts [name: ] = input
# TODO2. Prompts [Years of experience]
# for example users enters 4 
# clas openingpositions: name, location , years of e
# TODO3: Show the user opening jobs to apply
# opening jobs will be displayed according the users experience
# opening jobs will have name, location, years of experience fields
# so if the user's input value [years of experience] is greater or equal to any of the opening jobs experience field 

from dataclasses import dataclass
from typing import List




# @dataclass
# class Department:
#     name:str
@dataclass
class OpeningPositions:
    name: str
    location:str
    experience:str

    def __repr__(self):
        return f'{self.name} {self.location} {self.experience}'

@dataclass
class Benefits:
    name:str
    description:str = None

    def __repr__(self):
        return f"{self.name}"

@dataclass
class Projects:
    name:str
    location:str

    def __repr__(self):
        return f"{self.name}, {self.location}"

@dataclass
class Company:
    name:str
    opening_positoins: List[OpeningPositions]
    benefits: List[Benefits]
    projects:List[Projects]

    def invite(self,you):
        # Benefits
        print(f"{you} welcome to {self.name}")
        for indx, benefit in enumerate(self.benefits):
            print(f"{indx}. {benefit}")
        
        # Projects
        for indx, project in enumerate(self.projects):
            print(f"{indx}. {project}")
        

# Department = [
#     Department("Network Engineer","Business Developer")
# ]
POSITIONS = [
    OpeningPositions("Network Engineer","Hodan District",5),
    OpeningPositions("Business Developer","Wadajir District",7),
    OpeningPositions("System Engineer","Hodan District",15)
]


BENEFITS = [
    Benefits("Remote Work"),
    Benefits("Free Lunch"),
    Benefits("Free Travel"),
]

PROJECTS = [
    Projects("Network Setup","Mogadishu"),
    Projects("System Setup","Waberi"),
]

# TODO 1. Company information setup

def apply_job():
    try:
        you = input("Your Name: ")
        experience = int(input("Years of experience: "))
        somaliREN = Company("SomaliREN",opening_positoins=POSITIONS,benefits=BENEFITS,projects=PROJECTS) 
    #    somaliREN.invite(you)
        for indx, job in enumerate(POSITIONS):
            if POSITIONS[indx].experience <= experience :
                print(f"{indx}. {job}")
        
       
            
        # else:
        #     print("No Opening Positons")
            
    except ValueError:
        print("Wrong Command")
    
apply_job()














