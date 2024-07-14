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
            with open(os.path.join(posts_dir, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                html_content = markdown2.markdown(content)  # Cambiado a markdown2.markdown
                posts.append({
                    'title': filename[:-3].replace('_', ' ').title(),  # Usa el nombre del archivo como título
                    'content': (html_content)
                })
    return render_template('blog.html', posts=posts)




if __name__ == '__main__':
    app.run(debug=True, port=5000)