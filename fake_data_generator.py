import random

import pandas as pd


class FakeDataGenerator:
    def __init__(self):
        self.districts = [
            "Śródmieście",
            "Wrzeszcz",
            "Oliwa",
            "Przymorze",
            "Zaspa",
            "Jasień",
            "Ujeścisko-Łostowice",
            "Piecki-Migowo",
            "Orunia Górna",
            "Chełm",
            "Brzeźno",
            "Nowy Port",
            "Letnica",
            "Kokoszki",
        ]

        self.streets = [
            "Długa",
            "Mariacka",
            "Długi Targ",
            "Oliwska",
            "Grunwaldzka",
            "Wałowa",
            "Podwale Grodzkie",
            "Szeroka",
            "Piwna",
            "Świętego Ducha",
            "Targ Rybny",
            "Targ Węglowy",
            "Kartuska",
            "Wita Stwosza",
            "Słowackiego",
        ]

        self.title_prefixes = [
            "Nowoczesne",
            "Przestronne",
            "Słoneczne",
            "Stylowe",
            "Komfortowe",
            "Ekskluzywne",
            "Funkcjonalne",
            "Przytulne",
            "Z klimatem",
            "Z widokiem",
            "Z tarasem",
            "Z balkonem",
            "Z pięknym widokiem",
            "Z ogródkiem",
            "Z komórką lokatorską",
        ]

        self.title_suffixes = [
            "w świetnej lokalizacji",
            "w centrum",
            "w spokojnej okolicy",
            "w pobliżu morza",
            "w pobliżu parku",
            "w pobliżu szkoły",
            "w pobliżu komunikacji miejskiej",
            "w pobliżu sklepów",
            "w pobliżu restauracji",
            "w pobliżu plaży",
            "w pobliżu lasu",
            "w pobliżu centrum handlowego",
            "w pobliżu przystanku",
            "w pobliżu metra",
            "w pobliżu dworca",
        ]

        self.cat_urls = [
            "https://http.cat/200",
            "https://http.cat/201",
            "https://http.cat/202",
            "https://http.cat/204",
            "https://http.cat/206",
            "https://http.cat/207",
            "https://http.cat/300",
            "https://http.cat/301",
            "https://http.cat/302",
            "https://http.cat/303",
            "https://http.cat/304",
            "https://http.cat/307",
            "https://http.cat/400",
            "https://http.cat/401",
            "https://http.cat/402",
            "https://http.cat/403",
            "https://http.cat/404",
            "https://http.cat/405",
            "https://http.cat/406",
            "https://http.cat/408",
            "https://http.cat/409",
            "https://http.cat/410",
            "https://http.cat/411",
            "https://http.cat/412",
            "https://http.cat/413",
            "https://http.cat/414",
            "https://http.cat/415",
            "https://http.cat/416",
            "https://http.cat/417",
            "https://http.cat/418",
            "https://http.cat/422",
            "https://http.cat/423",
            "https://http.cat/424",
            "https://http.cat/425",
            "https://http.cat/426",
            "https://http.cat/428",
            "https://http.cat/429",
            "https://http.cat/431",
            "https://http.cat/444",
            "https://http.cat/450",
            "https://http.cat/451",
            "https://http.cat/499",
            "https://http.cat/500",
            "https://http.cat/501",
            "https://http.cat/502",
            "https://http.cat/503",
            "https://http.cat/504",
            "https://http.cat/506",
            "https://http.cat/507",
            "https://http.cat/508",
            "https://http.cat/509",
            "https://http.cat/510",
            "https://http.cat/511",
            "https://http.cat/599",
        ]

        # Gdańsk center coordinates
        self.center_lat = 54.3520
        self.center_lon = 18.6466

        # Random descriptions
        self.descriptions = [
            "Spacious apartment with a view of the sea",
            "Cozy studio in the heart of the city",
            "Modern apartment with parking space",
            "Renovated apartment in a quiet neighborhood",
            "Luxury apartment with balcony",
            "Family-friendly apartment near schools",
            "Apartment with a beautiful garden view",
            "Stylish apartment in a historic building",
            "Sunny apartment with large windows",
            "Apartment with a view of the Old Town",
        ]

    def generate_coordinates(self):
        # Generate random coordinates within ~5km of Gdańsk center
        lat = self.center_lat + random.uniform(-0.05, 0.05)
        lon = self.center_lon + random.uniform(-0.05, 0.05)
        return lat, lon

    def generate_apartment(self):
        district = random.choice(self.districts)
        street = random.choice(self.streets)
        house_number = random.randint(1, 100)
        floor = random.randint(0, 10)
        rooms = random.randint(1, 5)
        area = round(random.uniform(30, 120), 1)
        # More realistic price range for Gdańsk (per m²)
        price_per_m2 = random.uniform(8000, 15000)
        price = round(area * price_per_m2, 2)
        year_built = random.randint(1950, 2023)
        lat, lon = self.generate_coordinates()
        cat_url = random.choice(self.cat_urls)
        description = random.choice(self.descriptions)

        # Generate realistic title
        prefix = random.choice(self.title_prefixes)
        suffix = random.choice(self.title_suffixes)
        title = f"{prefix} {rooms}-pokojowe mieszkanie {area}m² {suffix}"

        return {
            "title": title,
            "price": price,
            "area": area,
            "rooms": rooms,
            "floor": floor,
            "year_built": year_built,
            "address": f"{street} {house_number}",
            "description": description,
            "url": cat_url,
            "latitude": lat,
            "longitude": lon,
            "district": district,
        }

    def generate_dataset(self, num_apartments=100):
        print(f"Generating {num_apartments} fake apartment listings...")
        apartments = [self.generate_apartment() for _ in range(num_apartments)]
        df = pd.DataFrame(apartments)

        # Save to CSV
        output_file = "apartments_gdansk.csv"
        df.to_csv(output_file, index=False)
        print(f"Saved {len(df)} fake listings to {output_file}")
        return df


if __name__ == "__main__":
    generator = FakeDataGenerator()
    generator.generate_dataset()
