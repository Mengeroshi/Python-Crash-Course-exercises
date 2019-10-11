from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

labels, comments, titles = [], [], []
for articles in submission_dicts:
    title = articles['title']
    link = articles['hn_link']
    label = f"<a href='{link}'>{title[:20]}</a>"

    labels.append(label)

    titles.append(title)

    comments.append(articles['comments'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': labels,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(0, 0, 0)',
        #'line': {'width': 1.5, 'color': 'rgb(0, 0, 0)'}
    },
}]

my_layout = {
    'title': 'HackerNews Active Discussions',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hackernews_discussions.html')