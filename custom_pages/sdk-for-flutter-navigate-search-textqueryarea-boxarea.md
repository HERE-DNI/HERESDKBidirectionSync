---
title: "boxArea property"
slug: "sdk-for-flutter-navigate-search-textqueryarea-boxarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boxArea.html -->


<div>
<h1>boxArea property</h1></div>

<a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>?
        boxArea
<div class="features">final</div>


<p>Geographic rectangle area in which to provide the most relevant places.
For Offline Search, one of <a href="/sdk-for-flutter-navigate-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="/sdk-for-flutter-navigate-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="/sdk-for-flutter-navigate-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set,
otherwise it will result in <a href="/sdk-for-flutter-navigate-search-searcherror">SearchError.invalidArea</a>.
Also, for Offline Search, search in a given <code>GeoBox</code> restricts the results to only POIs.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final GeoBox? boxArea;</code></pre>

 



</div>
`
}</HTMLBlock>
