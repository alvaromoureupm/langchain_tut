import os
import requests
from dotenv import load_dotenv

LINKEDIN_URL = "https://www.linkedin.com/in/alvaro-moure-prado/"
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool=False):
    """
    Scrapes a LinkedIn profile and returns a dictionary with the following keys:
    """
    if mock:
        url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(url, timeout=10)   
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dict = {
            "Authorization": f"Bearer {os.getenv('PROXY_CURL_API_KEY')}"
        }
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dict,
            timeout=10,
        )

    data = response.json()

    data = {
        k:v
        for k,v in data.items()
        if v not in ([], "", None)
        and k not in ["people_also_viewed", "certifications", "recommendations"]
    }

    if data.get("groups"):
        for group in data.get("groups"):
            group.pop("profile_pic_url")
    

    return data
    

if __name__ == "__main__":
    data = scrap_linkedin_profile(LINKEDIN_URL, mock=True)
    print(data)