import os

def get_articles(posts_dir='posts', limit=None):
    posts = []
    posts_dir = os.path.join(os.path.dirname(__file__), 'posts') #ruta del directorio

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            modification_time = os.path.getmtime(filepath)
            posts.append((filename, modification_time))
    
    posts.sort(key=lambda x: x[1], reverse=True)
    
    if limit:
        posts = posts[:limit]
    
    articles = []
    for filename, _ in posts:
        title = filename[:-3].replace('_', ' ').title()
        articles.append({'title': title, 'filename': filename})
    
    return articles
