---
title: "circleArea property"
slug: "sdk-for-flutter-navigate-search-textqueryarea-circlearea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- circleArea.html -->


<div>
<h1>circleArea property</h1></div>

<a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a>?
        circleArea
<div class="features">final</div>


<p>Geographic circle area in which to provide the most relevant places.
For Offline Search, one of <a href="sdk-for-flutter-navigate-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-navigate-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-navigate-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set,
otherwise it will result in <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.invalidArea</a>.
Also, for Offline Search, search in a given <code>GeoCircle</code> restricts the results to only POIs.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final GeoCircle? circleArea;</code></pre>

 



</div>
`
}</HTMLBlock>
