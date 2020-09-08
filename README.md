# Self-learning Web Scraping with AutoScraper in Python

[AutoScraper](https://github.com/alirezamika/autoscraper) is a Smart, Automatic, Fast and Lightweight Web Scraper for Python.

Developed by [Alireza Mika](https://github.com/alirezamika), it can be downloaded at https://github.com/alirezamika/autoscraper

## Concept and problem solved

Despite the availability of tools such as [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Web Scraping is difficult.

A library such Beautiful Soup helps you to:

- query a Web page
- parse the result of the query into a structured data structure: a tree
- query the resulting tree with an idiomatic way

But a Web Scraper doesn't write the query for you.

The purpose of a web page is to be consumed by humans not machines:

- the format of the page can change over time, and so the query could stop to work
- writing a "web scraping query" is time-consuming

**What if a library could learn from an example and then can write the scrap query for you : it's "the reason d'être of AutoScraper"**.

## How to use **AutoScraper**

### Problem

I want to create a Web scraper for the Web site [Quora](https://www.quora) to all the questions about a subject.

### Phase 1 : the learning phase

- We train our library on a specific page: "https://www.quora.com/search?q=deep%20learning&time=year"
- We give to the library an example about what we seek on the page for example "When will deep learning finally die out?"

#### Install AutoScraper from Github

```bash
pip install git+https://github.com/alirezamika/autoscraper.git
```

#### Create the file demo_train.py

```python

from autoscraper import AutoScraper

# Parameters
url = "https://www.quora.com/search?q=deep%20learning&time=year"
model_name = "model_quora"

wanted_list = ["When will deep learning finally die out?"]

# We instanciate the AutoScraper
scraper = AutoScraper()

# We train the Scraper
# Here we can also pass html content via the html parameter instead of the url (html=html_content)
result = scraper.build(url, wanted_list)

# We display the results if any
if(result):
  print("🚀 Great a query has been inferred !! Great gob.")
  print(result)

# If no result we leave with an error code
if(result == None):
  print("Sorry no query can be inferred ... 😿")
  exit(-1)

# We save the model for future use
print(f"💿 > Save the model {model_name}")
scraper.save(model_name)

```

#### We execute the file demo_train.py

```bash
python3 demo_train.py
```

#### Result of the execution of demo_train.py

```plain
🚀 Great a query has been inferred !! Great gob.
['When will deep learning finally die out?', 'What newly developed machine learning models could surpass deep learning?', 'What is the future of machine learning/deep learning startups?', 'How promising is deep learning?', 'How can a regression problem be solved with deep learning?', 'What is the brutal truth about deep learning?', 'Why is there still no theory underlying deep learning?', 'What are the frameworks for deep learning modelling?', 'What is deep learning in terms of programming?']
💿 > Save the model model_quora
```

### Phase 2 : the usage phase

A model has been saved in the preceding step that contains all the rules of scraping.

Now, we can apply our model on a page that shares the same structure with the page we have used during the training phase.

#### We create a new file called demo.py

```python
from autoscraper import AutoScraper

# AutoScraper must be installed with
#  pip install git+https://github.com/alirezamika/autoscraper.git

question = "france"
time = "year"
url = f"https://www.quora.com/search?q={question}&time={time}"
model_name = "model_quora"

scraper = AutoScraper()
scraper.load(f"./{model_name}")
# Get all the results in the page similar to our model
results = scraper.get_result_similar(url)

# if no results
if results:
  for r in results:
    print(r)
else:
  print("No result found")

```

#### We test if the scraper works

```bash
python3 demo.py
```

#### Result of the execution of demo.py

```plain
Is France really as useless at war as portrayed in America?
France fined Google 166M. Can Google just say no and not pay it? What are they going to do, ban Google in France?
Is there freedom of expression in France?
How is France dealing with Covid-19?
What country is the oldest ally to France?
Is France really 'littered' with abandoned chateaux?
Why is France considered the most advanced country of Europe?
Will Germany and France leave the European Union following Brexit?
American expats to France, is France what it is cracked up to be?
```

### Conclusion

The scraper must be trained again if the structure of the page changes.

The real advantage of the is approach is to be very reactive when a new format is available and to propose a new model quickly to continue the data extraction.

The library is very new. It's not perfect, but a big thanks to [Alireza Mika](https://github.com/alirezamika) for this great approach.

Writen by Raphaël MANSUY CTO at https://www.elitizon.com



  
