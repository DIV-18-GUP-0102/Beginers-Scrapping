import os
import sys
import pandas as pd
from utils.web import parse_html, extract_content
from utils.nlp_analysis import perform_nlp_analysis

def scrape_articles(num_urls_to_process):
    df = pd.read_excel('Input.xlsx')
    files_created = []
    folder_path = "text_files" 

    if num_urls_to_process is not None:
        df = df.head(num_urls_to_process)
    
    for index, row in df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        html_content = parse_html(url)
        article_title, article_text = extract_content(html_content)
        
        if article_text:
            file_name = os.path.join(folder_path, f"{url_id}.txt")  
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(f"{article_title}\n\n{article_text}")
            print(f"Content saved to '{file_name}'")
            files_created.append((file_name, url_id, url))
        else:
            print(f"Error: Unable to extract content from {url}")

    return files_created


def main(num_urls_to_process):
    files_created = scrape_articles(num_urls_to_process)
    results = []
    folder_path = "text_files"

    for file_name, url_id, url in files_created:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            article_content = file.read()

        # Perform NLP analysis
        analysis_result = perform_nlp_analysis(article_content)
        
        # Include url_id and url in the analysis result
        analysis_result_with_metadata = {
            'URL_ID': url_id,
            'URL': url,
            'POSITIVE SCORE': analysis_result[0],
            'NEGATIVE SCORE': analysis_result[1],
            'POLARITY SCORE': analysis_result[2],
            'SUBJECTIVITY SCORE': analysis_result[3],
            'AVG SENTENCE LENGTH': analysis_result[4],
            'PERCENTAGE OF COMPLEX WORDS': analysis_result[5],
            'FOG INDEX': analysis_result[6],
            'AVG NUMBER OF WORDS PER SENTENCE': analysis_result[7],
            'COMPLEX WORD COUNT': analysis_result[8],
            'WORD COUNT': analysis_result[9],
            'SYLLABLE PER WORD': analysis_result[10],
            'PERSONAL PRONOUNS': analysis_result[11],
            'AVG WORD LENGTH': analysis_result[12]
        }

        results.append(analysis_result_with_metadata)
        print("...NLP processing done for " + file_name)

    # Create DataFrame and save results to Excel file
    columns = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']
    df_results = pd.DataFrame(results, columns=columns)
    df_results.to_excel('Output_Data.xlsx', index=False)
    print("Ooutput Data completed")

if __name__ == "__main__":
    num_urls_to_process = int(sys.argv[1]) if len(sys.argv) > 1 else None
    main(num_urls_to_process)


