import feedparser as fp

from flask import Flask
app = Flask(__name__)

bbcFeed = 'http://feeds.bbci.co.uk/news/rss.xml'

@app.route('/')
def get_news():
    feed = fp.parse(bbcFeed)
    firstArticle = feed.entries[3]
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
