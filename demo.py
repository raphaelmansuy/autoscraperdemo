

from autoscraper import AutoScraper

# AutoScraper must be installed with
#  pip install git+https://github.com/alirezamika/autoscraper.git

question = "france"
time = "year"
url = f"https://www.quora.com/search?q={question}&time={time}"
model_name = "model_quora"

scraper = AutoScraper()
scraper.load(f"./{model_name}")
results = scraper.get_result_similar(url)

# if no results
if results:
  for r in results:
    print(r)
else:
  print("No result found")

