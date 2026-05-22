---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsdirection-altitude"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- altitude.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscenelightsdirection-class</li>
<li class="self-crumb">altitude property</li>
</ol>
<div class="self-name">altitude</div>
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
<h1>altitude property</h1></div>
<section class="multi-line-signature">
        
        double
        altitude
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Direction altitude value in degrees in the range [0, 90].
The default value is 0.0.
The altitude value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
When both azimuth and altitude values are provided, they are adjusted independently:
For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double altitude;</code></pre>
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
<li class="self-crumb">altitude property</li>
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
