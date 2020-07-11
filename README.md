<h1 align="center"> 
  WikiFe
  </h1>

<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/MADE%20WITH%20-Python-blueviolet" height="20">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" height="20">
  </a>
  <a href="https://wikife.herokuapp.com/">
    <img src="https://img.shields.io/badge/Website-Up-success" height="20">
  </a>
</p>

<p align="center">
  <img src = "Assets/WikiFe - Home.png">
  </p>
  
<br>  
<h2>Introduction</h2>
<p> <a href="https://www.wikipedia.org/">Wikipedia</a> is an online repository which has some sort of information on almost every topic. This Flask app uses Wikipedia API to get a search query from the user and displays a list of the related topics. Once a topic is selected, the app then fetches the summary of that Wikipedia article and displays it.
The app also shows the most viewed Wikipedia topics in the past day along with the page views. These are hosted under the tab <b>Trending</b> on the navigation bar at the top.</p>

<h2>Demo</h2>
<p> The application is live at <a href="https://wikife.herokuapp.com/" target="_blank">WikiFe</a>.</p>

<h2>Major Technologies</h2>
<ul type="disc">
  <li>beautifulsoup4 - 4.9.1</li>
  <li>Flask - 1.1.2</li>
  <li>wikipedia - 1.4.0</li>
  <li>urllib3 - 1.25.9</li>
  <li>Jinja2 - 2.11.2</li>
  <li>requests - 2.24.0</li>
</ul>
<p> A complete list of all the dependencies can be found <a href="requirements.txt"> here</a>.</p>

<h2>Working</h2>
<p> The application makes use of Wikipedia API to get the required results. Once the user enters a specific word for search, the application returns a list of the most relevant topics related to the search item. The user can then click on any topic according to their interest and is lead to a summary of that topic.</p>
<p> The user can also check the <b>Trending</b> page to check the most viewed Wikipedia pages along with the page views all around the globe in the last day. This gives an indication of the recent happenings around the world. If interested in a specific trending topic, the user can click on the topic and it will lead the user to the respective Wikipedia page.</p>

<p align="center">
  <img src = "Assets/WikiFe - Home.png">
</p>
<br>
<p align="center">
  <img src="Assets/WikiFe - Trending.png">
</p>
  



<h2>License</h2>
<a href="LICENSE">MIT License</a>



