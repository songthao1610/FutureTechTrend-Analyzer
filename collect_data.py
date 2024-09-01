import time
import requests
import json
import time

url='https://api.github.com/search/repositories/q=QUERY+language:LANGnotnull+created:>START_DATE+pushed:>PUSHED_DATE&sort=stars&order=desc'


results = []

def search_repo_paging(q, yr):
  url = 'https://api.github.com/search/repositories'
  params = {'q':q, 'sort':'forks','forks_count':'<500','order':'desc', 'per_page':100}
  
  while True:
    res = requests.get(url, params = params)
    result = res.json() 
    try: 
      with open(f"datasets/year{yr}.json", "a") as outfile:
        json.dump(result['items'], outfile, indent=4)
      params = {}
      url = res.links['next']['url']
    except requests.exceptions.HTTPError as err:
      if res.status_code == 403:
        time.sleep(120)
      else:
        time.sleep(120)
    except Exception as e:
      time.sleep(120)
    except:
      break

yrs =  [2018, 2019, 2020, 2021, 2022, 2023, 2024]
for yr in yrs:
  q = f'created:{yr}-01-01..{yr}-12-31 forks:<500'
  search_repo_paging(q,yr)