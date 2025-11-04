from bs4 import BeautifulSoup
import requests
import regex as re 
import unittest

# TASK 2: PROCESS LANDMARK DATA
def get_landmark_data(soup) -> dict[dict]:
    '''
    creates a nested dictionary of landmarks and their data

    the outer keys are the landmark names
    the inner keys are information about the landmark 
        - data designated
        - location 
        - county
        - description 

    returns a nested dictionary
    '''
    

# TASK 3: GET PROPER NOUNS
def get_proper_noun_phrases(landmarks_dict:dict[dict], target_landmark:str) -> list[str]:
    '''
    extracts all proper noun phrases from the description field of the target landmark 

    proper noun phrase = multiple consecutive capitalized worlds (e.g. 'Great Lakes' or 'Michigan State')

    returns a list with all proper nounts
    '''

    d = {}
    

    table = soup.find("table", class_="wikitable sortable")
    rows = table.find_all("tr")

    for row in rows:
        elements = row.find_all("td")
        name = elements[0].text.strip()
        nested = ["data designated"] = elements[2].text.strip()
        nested["location"] = elements[3].text.strip()
        nested["country"] = elements[4].text.strip()
        nested["description"] = elements[5].text.strip()
        print(elements)

        d[name] = nested
    return d





def main():
    #TASK 1: GET DATA FROM WIKIPEDIA
    url = 'https://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Michigan'
    
    # Supply this as requests.get(url, headers=headers)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    }

    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    
    else:
        print("response not valid")
        return
    
    d = get_landmark_data(soup)
    


# DO NOT MODIFY TEST CASES
class TestAllFunctions(unittest.TestCase):
    def setUp(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        }
        soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Michigan", headers=headers).text, 'html.parser')
        self.landmarks_data = get_landmark_data(soup)

    def test_get_landmark_data(self):
        self.assertEqual(len(self.landmarks_data), 42)
        self.assertTrue('USS Silversides (Submarine)' in self.landmarks_data)

        self.assertEqual(self.landmarks_data['Bay View']['county'], 'Emmet')
        self.assertEqual(self.landmarks_data['Cranbrook']['county'], 'Oakland')

    def test_get_proper_noun_phrases(self):
        bay_view = get_proper_noun_phrases(self.landmarks_data, 'Bay View')
        self.assertEqual(bay_view, [])

        gm = get_proper_noun_phrases(self.landmarks_data, 'General Motors Building')
        self.assertEqual(gm, ['General Motors'])

        guardian_building = get_proper_noun_phrases(self.landmarks_data, 'Guardian Building')
        self.assertEqual(guardian_building, ['Union Trust', 'Union Trust Company'])


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)