def city_country(city,country,population=''):
    '''生成城市信息'''
    if population:
        city_descri = city .title() + ',' + country.title() + ' - population '+ population
    else:
        city_descri = city .title() + ',' + country.title()
    return city_descri
    
