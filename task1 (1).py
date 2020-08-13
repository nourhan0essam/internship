from bs4 import BeautifulSoup
import urllib
import time
import requests


# start
start_url = input('Enter - ')
# target
target_url = "https://en.wikipedia.org/wiki/Philosophy"
# store the visited article 
visited_urls = [start_url]

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return

    # Build a full url 
    first_link = urllib.parse.urljoin(
        'https://en.wikipedia.org/', article_link)

    return first_link

def continue_scraping(scraping_history, target_url, max_steps=30):
    # When reaches to philosphy
    if scraping_history[-1] == target_url:
        print("Target ('Philosphy') article reached!")
        return False
    # max iterations 
    elif len(scraping_history) > max_steps:
        print("Maximum (30) searches reached, interrupted.")
        return False
    elif scraping_history[-1] in scraping_history[:-1]:
        print("We are in a Loop , interrupted.")
        return False
    else:
        return True


while continue_scraping(visited_urls, target_url):
    #print first link
    print(visited_urls[-1])

    first_link = find_first_link(visited_urls[-1])
    # when arrive at an article with no links
    if not first_link:
        print("Arrived at an article with no links, search aborted.")
        break

    visited_urls.append(first_link)

    time.sleep(0.5)  # Slow things down so as to not overload Wikipedia's servers
visited_urls=[start_url]