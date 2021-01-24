


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
# then show the list like this
# We have two opening Jobs which one would you like to apply
# 1- Network in mogadishu 
# 2- systems in Kismayo
# classes
# opening positons
# benefits 
# projects 
# company  - invite
# appicant 

#TODO4: if the user selects 1 or 2  invite them for interview
# Also  print benefits and projects they will work on
# otherwise, prompt the user that they haven't fulfilled the requirements [Sorry Our job requires x years of experience]
# name = input("whats your name")



from dataclasses import dataclass
from typing import List,Optional

# @dataclass
# class OpeningPositions:
#     name:str
#     location:str
#     years_of_exp:int
#     shift:str =  None

#     def __repr__(self):
#         return f"{self.name} in {self.location} requires {self.years_of_exp} years of experience"

def opining_positions(*,name,location,years_of_exp,shift=None):
    return {"name":name,"location":location,'years_of_exp':years_of_exp}
    # return f"{name} in {location} requires {years_of_exp} years of experience" 

@dataclass
class Benifits:
    name:str

    def __repr__(self):
        return f"{self.name}"


# Opening 

OPENING_POSITIONS = [
    opining_positions(name="System Engineering",location="Mogadishu",years_of_exp=3,shift="Night"),
    opining_positions(name="Network Engineering",location="Mogadishu",years_of_exp=5)
# OpeningPositions(name="System Engineering",location="Mogadishu",years_of_exp=3,shift="Night"),
# OpeningPositions(location="Mogadishu",name="Network Engineering",years_of_exp=5),
# OpeningPositions(location="Nairobi",name="DevOps",years_of_exp=8),
]

position1=  opining_positions(name="System Engineering",location="Mogadishu",years_of_exp=3,shift="Night")
print(position1["name"])

# print(OPENING_POSITIONS[0].name)
# print(OPENING_POSITIONS[1].name)


BENEFITS = [
    Benifits("Free lunch"),
    Benifits("Remote Work"),
]

@dataclass
class Company:
    benefits:List[Benifits]

    def invite(self):
        for benefit in self.benefits:
            print(benefit)


somaliren = Company(benefits=BENEFITS)
somaliren.invite()



MAX = 14 # user enters 4

# Looping Opening positions 
for index,job in enumerate(OPENING_POSITIONS):
    if OPENING_POSITIONS[index]["years_of_exp"] <= MAX:
        print(f"{index+1}. {job['name']} in {job['location']} requires {job['years_of_exp']} years of experience")

# option = int(input("Select Option: "))
# option -=1
# print(option)

# loves_networking = True














# OPENING_POSITIONS_DICT = [
# {"positionName":"Netowrk"},
# {"positionName":"System"},
# ]
# # dictname.get("value")
# print(OPENING_POSITIONS_DICT[0].get("positionName"))
# print(OPENING_POSITIONS_DICT[1].get("positionName"))



