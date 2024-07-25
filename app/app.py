from flask import Flask, render_template
import markdown2
import os
from tools import get_articles  # Re-utilizar función


app = Flask(__name__)


@app.route("/")
def index():
    recent_articles = get_articles(limit=3)
    return render_template('index.html', recent_articles=recent_articles)



@app.route('/blog')
def blog():
    posts = get_articles()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<filename>')

def post(filename):
    posts_dir = os.path.join(os.path.dirname(__file__), 'posts') #ruta del directorio
    filepath = os.path.join(posts_dir, filename)  #ruta del archivo 


    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content = markdown2.markdown(content)

    return render_template('post.html', title=filename[:-3].replace('_', ' ').title(), content=html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)