import json
import re

data_ny_json = []
unike_ord = set()

f = open("lemma.json")
data = json.load(f)

#fjerner duplikater og ord som ikke er substantiv
for i in data:
    #print(i)
    #print(type(i))
    if "NOUN" in i[2]:
        if not re.match(r'^-', i[0]):
            if i[0] not in unike_ord:
                unike_ord.add(i[0])
                data_ny_json.append(i)
f.close

#fjern single bokstaver og kanskje de som begynner med tall
#fjern dur/moll og undersøk NOUN_uninfl
####


#lager ny json fil, med ordet, artikkel nr. og NOUN
def write_json(ny_data, filename='lemma_nouns.json'):
    json_obj =json.dumps(ny_data, indent= 4, sort_keys=True)
    with open(filename,'w') as file:
        file.write(json_obj)

write_json(data_ny_json)
print("complete! antall i set: ",len(unike_ord))