
def bing(city,country,population = 0):
    city = str(city)
    country = str(country)
    if population:
        result = city+','+country+' - population = '+\
                 str(population)
        return result.title()
    else:
        result = city + ',' + country
        return result.title()

print(bing('beijing','china',population=14))