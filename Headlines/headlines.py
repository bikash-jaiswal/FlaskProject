import feedparser as fp

from flask import Flask
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
def get_news(feedname ="bbc"):
    feed = fp.parse(RssFeed[feedname])
    firstArticle = feed.entries[0]
    return f"""
           <html>
                    <body>
                        <h1> BBC Headlines </h1>
                        <b>{firstArticle.title}</b> 
                        <i>{firstArticle.published}<i><br/>
                        <p>{firstArticle.summary}</p><br/>     
                    </body>
            </html>
             """      
   
if __name__ == "__main__":
    app.run(port=5000, debug = True)    
