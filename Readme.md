# Web Scrapping and NLP Analysis Project

This project is designed to scrape articles from given URLs, extract their content, and perform Natural Language Processing (NLP) analysis on the text. The output of the analysis is saved in an Excel file.

## File Structure
```
project/
│
├── main.py
├── Input.xlsx
├── Output_Data.xlsx
├── requirements.txt
├── README.md
└── text_files/
├── blackassign001.txt.txt
├── blackassign002.txt.txt
└── ...
└── utils/
├── init.py
├── web.py
├── analysis.py
├── generic.txt
├── ProperNoun.txt
├── negative.txt
└── positive.txt
```

- `main.py`: The main script to execute the NLP analysis on articles.
- `Input.xlsx`: Input file containing URLs to be scraped.
- `Output_Data.xlsx`: Output file containing the results of NLP analysis.
- `requirements.txt`: The txt file containing the library dependencies.
- `README.md`: This file explaining the project structure and functionality.
- `text_files/`: Folder containing text files scraped from URLs.
- `utils/`: Directory containing utility scripts.
  - `web.py`: Script for parsing HTML content and extracting article text.
  - `analysis.py`: Script for performing NLP analysis on text content.
  - `generic.txt`: Text file containing generic nouns.
  - `ProperNoun.txt`: Text file containing proper nouns.
  - `negative.txt`: Text file containing negative words.
  - `positive.txt`: Text file containing positive words.

## Functionality

- `main.py`: This script serves as the entry point for the project. It scrapes articles from URLs provided in `Input.xlsx`, extracts their content using `web.py`, performs NLP analysis using `analysis.py`, and saves the results in `Output_Data.xlsx`.
- `web.py`: Contains functions for parsing HTML content and extracting article text. It uses the BeautifulSoup library to parse HTML.
- `analysis.py`: Contains functions for performing NLP analysis on text content. It tokenizes sentences and words, calculates various metrics such as average sentence length, percentage of complex words, and polarity score.
- `Input.xlsx`: Input Excel file containing URLs to be scraped.
- `Output_Data.xlsx`: Output Excel file containing the results of NLP analysis.
- `text_files/`: Folder containing text files scraped from URLs.

## Usage

1. Add URLs to be scraped in the `Input.xlsx` file.
2. Run `main.py` script with the desired number of URLs to process as a command-line argument.

Example:

``` 
python main.py 5 
```

This will scrape and analyze the first 5 URLs listed in `Input.xlsx`.

## Important mentions


- I have used ``` python -m nltk.downloader punkt```
to download the `Punkt` tokenizer, a pre-trained unsupervised machine learning model provided by the Natural Language Toolkit (nltk) library, for   sentence tokenization and word tokenization.

- For finding the :
  - POSITIVE SCORE
  - NEGATIVE SCORE
  - POLARITY SCORE
  - SUBJECTIVITY SCORE

  I used the `filtered_words_2` list which is the list of words excluding any stopwords.
 
- In **Fog Index**, I have calculated the `AVG SENTENCE LENGTH` as the 
 `Sum of the total number of words(Including stopwords and duplicate words)/ total number of sentences`
And the `PERCENTAGE OF COMPLEX WORDS` as the count of words having more than 2 syllables but only after removing the Proper nouns.

- I am confused between `AVG SENTENCE LENGTH` and `AVG NUMBER OF WORDS PER SENTENCE` since they sounded same. Having calculated Summation of the number of words for each sentence and dividing it by the total number of sentences is same as finding the total number of words through `len(words)` and dividing by the total number of sentences. 

- For `COMPLEX WORD COUNT` I not only had the Proper noun removed from word list but also had duplicity removed.

- As mentioned in the instruction the `WORD COUNT` is calculated for the cleaned list of words.

- For `SYLLABLE PER WORD`, I again used the list with proper nouns removed, `filtered_words`.

- For `PERSONAL PRONOUNS` I used regex to find the pattern,  `\b(?:I|we|my|ours|us)\b` in the words to identify and count the presence of personal pronoun.

- For `AVG WORD LENGTH` I used the list of unique words with stopwords not removed.


## Problems

- When I ran my final code I encountered a problem where from some of the urls I am not able to extract the text content.
```
Content saved to 'blackassign0001.txt'

Content saved to 'blackassign0002.txt'

Content saved to 'blackassign0003.txt'

Content saved to 'blackassign0004.txt'

Content saved to 'blackassign0005.txt'

Content saved to 'blackassign0006.txt'

Content saved to 'blackassign0007.txt'

Content saved to 'blackassign0008.txt'

Content saved to 'blackassign0009.txt'

Content saved to 'blackassign0010.txt'

Content saved to 'blackassign0011.txt'

Content saved to 'blackassign0012.txt'

Content saved to 'blackassign0013.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/

Content saved to 'blackassign0015.txt'

Content saved to 'blackassign0016.txt'

Content saved to 'blackassign0017.txt'

Content saved to 'blackassign0018.txt'

Content saved to 'blackassign0019.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/

Content saved to 'blackassign0021.txt'

Content saved to 'blackassign0022.txt'

Content saved to 'blackassign0023.txt'

Content saved to 'blackassign0024.txt'

Content saved to 'blackassign0025.txt'

Content saved to 'blackassign0026.txt'

Content saved to 'blackassign0027.txt'

Content saved to 'blackassign0028.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/

Content saved to 'blackassign0030.txt'

Content saved to 'blackassign0031.txt'

Content saved to 'blackassign0032.txt'

Content saved to 'blackassign0033.txt'

Content saved to 'blackassign0034.txt'

Content saved to 'blackassign0035.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/

Content saved to 'blackassign0037.txt'

Content saved to 'blackassign0038.txt'

Content saved to 'blackassign0039.txt'

Content saved to 'blackassign0040.txt'

Content saved to 'blackassign0041.txt'

Content saved to 'blackassign0042.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/

Content saved to 'blackassign0044.txt'

Content saved to 'blackassign0045.txt'

Content saved to 'blackassign0046.txt'

Content saved to 'blackassign0047.txt'

Content saved to 'blackassign0048.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/

Content saved to 'blackassign0050.txt'

Content saved to 'blackassign0051.txt'

Content saved to 'blackassign0052.txt'

Content saved to 'blackassign0053.txt'

Content saved to 'blackassign0054.txt'

Content saved to 'blackassign0055.txt'

Content saved to 'blackassign0056.txt'

Content saved to 'blackassign0057.txt'

Content saved to 'blackassign0058.txt'

Content saved to 'blackassign0059.txt'

Content saved to 'blackassign0060.txt'


Content saved to 'blackassign0061.txt'

Content saved to 'blackassign0062.txt'

Content saved to 'blackassign0063.txt'

Content saved to 'blackassign0064.txt'

Content saved to 'blackassign0065.txt'

Content saved to 'blackassign0066.txt'

Content saved to 'blackassign0067.txt'

Content saved to 'blackassign0068.txt'

Content saved to 'blackassign0069.txt'

Content saved to 'blackassign0070.txt'

Content saved to 'blackassign0071.txt'

Content saved to 'blackassign0072.txt'

Content saved to 'blackassign0073.txt'

Content saved to 'blackassign0074.txt'

Content saved to 'blackassign0075.txt'

Content saved to 'blackassign0076.txt'

Content saved to 'blackassign0077.txt'

Content saved to 'blackassign0078.txt'

Content saved to 'blackassign0079.txt'

Content saved to 'blackassign0080.txt'

Content saved to 'blackassign0081.txt'

Content saved to 'blackassign0082.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/human-rights-outlook/

Error: Unable to extract content from https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/

Content saved to 'blackassign0085.txt'

Content saved to 'blackassign0086.txt'

Content saved to 'blackassign0087.txt'

Content saved to 'blackassign0088.txt'

Content saved to 'blackassign0089.txt'

Content saved to 'blackassign0090.txt'

Content saved to 'blackassign0091.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/

Content saved to 'blackassign0093.txt'

Content saved to 'blackassign0094.txt'

Content saved to 'blackassign0095.txt'

Content saved to 'blackassign0096.txt'

Content saved to 'blackassign0097.txt'

Content saved to 'blackassign0098.txt'

Error: Unable to extract content from https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/

Error: Unable to extract content from https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/
```   

- I found out that I am, for most of the URLs, extracting the title from `<h1 class="entry-title">` and the article from `<div class="td-post-content tagdiv-type">`, but for those errored cases the title belongs to `<h1 class="tdb-title-text">` and the article belongs to `<div class="tdb-block-inner td-fix-index">`.

- Therefore I tried to scrape from the newly founded `div` but was not able to, below is the modified code I tried to create:

```
from bs4 import BeautifulSoup

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    title_classes = ['entry-title', 'tdb-title-text']
    title = None
    for title_class in title_classes:
        title_element = soup.find('h1', class_=title_class)
        if title_element:
            title = title_element.get_text()
            break

    content = None
    post_content_div = soup.find('div', class_='tdb-block-inner td-fix-index')
    print(post_content_div)
    if post_content_div:
        if post_content_div.article and post_content_div.article.p:
            content = post_content_div.article.p.parent.get_text(separator='\n', strip=True)
    else:
        post_content_div = soup.find('div', class_='td-post-content tagdiv-type')
        if post_content_div:
            content = post_content_div.get_text(separator='\n', strip=True)

    return title, content

```