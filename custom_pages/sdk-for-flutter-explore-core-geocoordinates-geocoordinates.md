---
title: "GeoCoordinates constructor"
slug: "sdk-for-flutter-explore-core-geocoordinates-geocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinates.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class</li>
<li class="self-crumb">GeoCoordinates factory constructor</li>
</ol>
<div class="self-name">GeoCoordinates</div>
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
<div class="main-content" data-above-sidebar="core/GeoCoordinates-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>GeoCoordinates constructor</h1></div>
<section class="multi-line-signature">
GeoCoordinates(<wbr/><ol class="parameter-list single-line"> <li>double latitude, </li>
<li>double longitude</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs a GeoCoordinates from the provided latitude and longitude values.</p>
<p>Corrects values of latitude and longitude if they exceed the ranges.
Altitude set to <code>null</code>.</p>
<ul>
<li>
<p><code>latitude</code> Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it's clamped to that range.
NaN value is converted to 0.0.</p>
</li>
<li>
<p><code>longitude</code> Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it's replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to 0.0.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoCoordinates(double latitude, double longitude) =&gt; $prototype.$init(latitude, longitude);</code></pre>
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
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class</li>
<li class="self-crumb">GeoCoordinates factory constructor</li>
</ol>
<h5>GeoCoordinates class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
