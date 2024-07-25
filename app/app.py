from flask import Flask, render_template
import markdown2
import os

app = Flask(__name__)


@app.route("/")

def principal():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = []
    posts_dir = 'posts'
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            title = filename[:-3].replace('_', ' ').title()
            posts.append({'title': title, 'filename': filename}) 
    return render_template('blog.html', posts=posts)


@app.route('/blog/<filename>')
def post(filename):
    posts_dir = 'posts'
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content = markdown2.markdown(content)
    return render_template('post.html', title=filename[:-3].replace('_', ' ').title(), content=html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)