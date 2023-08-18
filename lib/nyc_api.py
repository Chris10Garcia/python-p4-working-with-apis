
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_school(self):

    programs = json.loads(self.get_programs())
    # programs_list = []
    # for program in programs:
    #   programs_list.append(program["agency"])

    programs_list = [program["agency"] for program in programs]

    return programs_list


# programs = GetPrograms().get_programs()
# print(programs)

# programs = GetPrograms()
# programs_school = programs.program_school()

programs_school = GetPrograms().program_school()

for school in set(programs_school):
  print(school)
