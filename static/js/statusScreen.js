const news = document.createElement('div');

news.className = 'news';

fetch('http://127.0.0.1:5000/news_js')
  .then(response => response.text())
  .then(newsContent => {
    news.innerHTML = newsContent;
  })
  .catch(error => {
    console.error('Error:', error);
  });

document.body.appendChild(news);