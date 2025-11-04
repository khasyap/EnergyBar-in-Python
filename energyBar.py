import math
import os
import requests

# Complete the 'energyBar' function below.
# The function is expected to return a STRING.
# The function accepts STRING country as parameter.
# API URL: https://jsonmock.hackerrank.com/api/chocolates?countryOfOrigin=<country>

def energyBar(country):
    base_url = "https://jsonmock.hackerrank.com/api/chocolates?countryOfOrigin={country}&page={page}"
    page = 1
    max_energy = -math.inf
    best_chocolate = ""

    while True:

        url = base_url.format(country=country, page=page)
        response = requests.get(url)
        data = response.json()


        if not data['data']:
            break

        for choc in data['data']:
            kcal = choc['nutritionalInformation']['kcal']
            weights = choc['weights']

            if len(weights) == 0:
                continue

            avg_weight = sum(weights) / len(weights)
            energy_per_gram = math.floor(kcal * 0.01 * avg_weight)

            brand_type = f"{choc['brand']}:{choc['type']}"

            if energy_per_gram > max_energy:
                max_energy = energy_per_gram
                best_chocolate = brand_type
            elif energy_per_gram == max_energy:
                if brand_type < best_chocolate:
                    best_chocolate = brand_type
        if page >= data['total_pages']:
            break
        page += 1

    return best_chocolate


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    country = input().strip()
    result = energyBar(country)
    fptr.write(result + '\n')
    fptr.close()
