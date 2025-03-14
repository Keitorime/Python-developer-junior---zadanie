import requests
from bs4 import BeautifulSoup as BS
import json
from datetime import datetime


class Parsing:

    def __init__(self):
        try:
            request = requests.get("https://www.prospektmaschine.de/hypermarkte")
            self.html = BS(request.text, 'html.parser')

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


    def parse(self):
        self.brochures = []
        for brochure in self.html.find_all("div", class_ = "brochure-thumb" ):
            title = brochure.find("strong").text
            
            thumbnail_tag: str = brochure.find("img")
            if thumbnail_tag and thumbnail_tag.has_attr("src"):
                thumbnail = thumbnail_tag["src"]
            elif thumbnail_tag and thumbnail_tag.has_attr("data-src"):
                thumbnail = thumbnail_tag["data-src"]
            logo_tag = brochure.find("img", class_="lazyloadLogo")
            shop_name = logo_tag["alt"].replace("Logo", "").strip()
            
            valid_data_tag = brochure.find("small", class_="hidden-sm")

            valid_data = valid_data_tag.text.strip()
    
            parts = valid_data.split(" ") 
            valid_from = parts[0] if parts[0] != "von" else parts[0] + " " + parts[1]
            valid_to = parts[-1]

            parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            self.brochures.append({
                "title": title, 
                "thumbnail": thumbnail,
                "shop_name": shop_name,
                "valid_from": valid_from,
                "valid_to": valid_to,
                "parsed_time": parsed_time
            })

            print(self.brochures)


    def save(self):
        filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.brochures, f, indent=4, ensure_ascii=False)

        


if __name__ == "__main__":
    parsing = Parsing()
    parsing.parse()
    parsing.save()