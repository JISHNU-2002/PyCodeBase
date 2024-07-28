import json

person = { "name" : "Jishnu", "age" : 21, "dep" : "CSE" }

p_json = json.dumps(person, indent=4, sort_keys=True)
print(p_json,type(p_json))

p_dict = json.loads(p_json)
print(p_dict,type(p_dict))

with open("person.json", "w") as json_file:
    json.dump(person, json_file)
    
with open('person.json', 'r') as json_file:
    person_from_file = json.load(json_file)
    print(person_from_file)
