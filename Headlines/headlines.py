import feedparser as fp
'''
render_template: render jinja template and produce pure html
'''
from flask import Flask, render_template
app = Flask(__name__)

RssFeed = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}
#for root
@app.route('/')
#for bbc location
# @app.route('/bbc')
# def bbc():
#     return get_news('bbc')

# @app.route('/cnn')
# def cnn():
#     return get_news('cnn')
@app.route("/<feedname>")
# Any variables specified by the
#decorator must be accounted for in our function's definition
def get_news(feedname ="cnn"):
    feed = fp.parse(RssFeed[feedname])
    # firstArticle = feed.entries[0]
    
    # return render_template("home.html",
    #                         title = firstArticle.title, 
    #                         published = firstArticle.published,
    #                         summary = firstArticle.summary  )   
    return render_template("home.html", 
                            articles = feed.entries)
   
if __name__ == "__main__":
    app.run(port=5000, debug = True)    
