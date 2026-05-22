---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-azimuth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- azimuth.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscenelightsdirection-class</li>
<li class="self-crumb">azimuth property</li>
</ol>
<div class="self-name">azimuth</div>
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
<div class="main-content" data-above-sidebar="mapview/MapSceneLightsDirection-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>azimuth property</h1></div>
<section class="multi-line-signature">
        
        double
        azimuth
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Direction azimuth value in degrees in the range [0, 360).
The default value is 0.0.
The azimuth range is half-open, meaning the maximum value is not included in the range.
If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
Specifically, values less than 0 will be increased by 360 until they fall within the range,
and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double azimuth;</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscenelightsdirection-class</li>
<li class="self-crumb">azimuth property</li>
</ol>
<h5>MapSceneLightsDirection class</h5>
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
