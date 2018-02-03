import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def search_rt(query):
    url = "https://www.rottentomatoes.com"
    query = "/search/?search=" + query
    search_query = url + query
    response = requests.get(search_query, headers=headers)
    htmldoc = response.text
    movies_json =  json.loads("{" + htmldoc[htmldoc.index("\"movies\":[") : htmldoc.index("\"tvCount\"")-1] + "}")
    return movies_json

def get_rtscores(movie_url):
    response = requests.get(movie_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    aud_score = soup.findAll("div", {"class": "meter-value"})[0].contents[1].contents[0]
    aud_rating = soup.findAll("div", {"class": "audience-info hidden-xs superPageFontColor"})[0].contents[1].contents[2].strip(' \t\n\r')
    all_crit_score = soup.findAll("span", {"class": "meter-value"})[0].contents[0].contents[0] + "%"
    top_crit_score = soup.findAll("span", {"class": "meter-value"})[1].contents[0].contents[0] + "%"
    all_crit_rating = soup.findAll("div", {"class": "superPageFontColor"})[0].contents[2].strip(' \t\n\r')
    top_crit_rating = soup.findAll("div", {"class": "superPageFontColor"})[4].contents[2].strip(' \t\n\r')
    return aud_rating, aud_score, all_crit_rating, all_crit_score, top_crit_rating, top_crit_score

def search_imdb(query):
    url = "http://www.imdb.com"
    search = "/search/title?title="+query+"&title_type=feature,tv_movie&count=100"
    search_query = url + search
    response = requests.get(search_query, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    tempdiv = soup.findAll("div", {'class' : 'lister-item-image float-left'})
    movie_list = []
    for movie in tempdiv:
        title = movie.contents[1].contents[1]['alt']
        href = url + movie.contents[1]["href"]
        imgsrc = movie.contents[1].contents[1]['loadlate']
        movie_tuple = (title, href, imgsrc)
        movie_list.append(movie_tuple)
    return movie_list

def get_imdbscores(movie_url):
    response = requests.get(movie_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    tempdiv = soup.findAll("div", {'class' : 'ratingValue'})
    rating = tempdiv[0].contents[1].contents[0].contents[0] + "/10"
    return rating
    
    
def main2():
    movies_json = search_rt(query)
    i = 1
    for movie in movies_json["movies"]:
        print(str(i) + "). \t" + movie["name"])
        i = i + 1
        
    print("")
    element = int(input("Which element? " )) - 1
    movie = url + movies_json["movies"][element]["url"]
    print(get_scores(movie))
                                    
def main():
    movieDB = dict()
    
    query = input("Give me a movie name: ")
    movie_list = search_imdb(query)
    i = 1
    for movie in movie_list:
        print(str(i) + "). \t" + movie[0])
        i = i + 1
    print("")
    element = int(input("Which element? " )) - 1
    print(get_imdbscores(movie_list[element][1]))
    
if __name__ == "__main__":
    main()
