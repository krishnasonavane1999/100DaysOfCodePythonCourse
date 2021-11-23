travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

print(len(travel_log))

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, total_visits, list_of_cities):
  new_entry = {
          "country": country,
          "visits": total_visits,
          "cities": list_of_cities
  }

  travel_log.append(new_entry)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# Nesting list in the dictionary

