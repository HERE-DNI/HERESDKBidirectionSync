---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-boundingbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boundingBox.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
<li class="self-crumb">boundingBox property</li>
</ol>
<div class="self-name">boundingBox</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>boundingBox property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-geobox-class?
boundingBox
</section>
<section class="desc markdown">
<p>Currently visible map area encompassed in a GeoBox.
Note that this bounding box is always rectangular, and its sides are always
parallel to the latitude and longitude. If the camera is rotated, the returned
bounding box will be a circumscribed rectangle that is larger than the
visible map area. Similarly, when the map is tilted (for example, if
the map is tilted by 45 degrees), the visible map area represents
a trapezoidal area in the world. Resulting value will then be a larger
circumscribed rectangle that contains this trapezoid area.
Because on this, corners of the resulting bounding box may be located
outside of the currently visible area.</p>
<p>When the map area does not fully fill the viewport, <code>null</code> is returned.
Gets the current visible map area encompassed in a GeoBox.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox? get boundingBox;</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
<li class="self-crumb">boundingBox property</li>
</ol>
<h5>MapCamera class</h5>
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
