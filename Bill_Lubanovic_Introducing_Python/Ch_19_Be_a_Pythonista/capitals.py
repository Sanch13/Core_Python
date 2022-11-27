

def process_cities(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # if 'quit' in line.lower():    # 1 case
            #     return                    # 1 case
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            country = country.strip()
            city = city.strip()
            print(f"{country.title()} capital --> {city.title()}")


if __name__ == '__main__':
    process_cities('cities.csv')
