# capitals

countries = input().split(', ')
capitals = input().split(', ')
result = dict(zip(countries, capitals))  # zip() returns zip object

[print(f"{key} -> {value}") for key, value in result.items()]
