const news = document.createElement('div');
news.className = 'news';

var xhr = new XMLHttpRequest();

xhr.open('GET', 'http://127.0.0.1:5000/news_js', true);

xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const newsContent = xhr.responseText;
      console.log(newsContent);
      news.innerHTML = newsContent; 
    }
};
xhr.send(); 

document.body.appendChild(news); 