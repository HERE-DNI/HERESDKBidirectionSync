---
title: "Untitled"
slug: "sdk-for-flutter-navigate-traffic-trafficflow-confidence"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confidence.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-traffic-trafficflow-class</li>
<li class="self-crumb">confidence property</li>
</ol>
<div class="self-name">confidence</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="traffic/TrafficFlow-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>confidence property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double?
confidence
</section>
<section class="desc markdown">
<p>The confidence field indicates the proportion of real-time data included in the speed calculation.
It is a normalized value between 0.0 and 1.0 with the following meaning:</p>
<ul>
<li>0.7 &lt; confidence &lt;= 1.0 indicates real time speeds</li>
<li>0.5 &lt; confidence &lt;= 0.7 indicates historical speeds</li>
<li>0.0 &lt; confidence &lt;= 0.5 indicates speed limit</li>
</ul>
<p>This field can be used to identify whether the data for a location is derived from
real-time probe sources or historical information only.
All confidence data 0.71 and above is based on real-time information,
where a confidence value of 0.75 or greater indicates high confidence real-time information.
A confidence value equal to 0.70 or lower means that the data is derived from historical data only.
Gets the confidence field value which is normalized value between 0.0 and 1.0.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get confidence;</code></pre>
</section>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-traffic-trafficflow-class</li>
<li class="self-crumb">confidence property</li>
</ol>
<h5>TrafficFlow class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
