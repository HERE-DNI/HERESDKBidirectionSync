---
title: "principalPoint property"
slug: "sdk-for-flutter-explore-mapview-mapcamera-principalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- principalPoint.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcamera-class</li>
<li class="self-crumb">principalPoint property</li>
</ol>
<div class="self-name">principalPoint</div>
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
<h1>principalPoint property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-point2d-class
principalPoint
</section>
<section class="desc markdown">
<p>Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
Gets the pixel point that determines where the target is placed within the map view.
By default, the principal point is located at the center of the map view.</p>
<p>The value of the principal point is adjusted when the dimensions of the
map view change, so that it stays in the same point relative to width
and height. Meaning that when a principal point it set to bottom
middle of the map view, it will stay in the bottom middle regardless
of the changes to dimensions and orientation of the view.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Point2D get principalPoint;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
principalPoint=(<wbr/>/sdk-for-flutter-explore-core-point2d-class value)
</section>
<section class="desc markdown">
<p>Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
Sets the pixel point that determines where the target appears within the map view.
This instantly moves the map to render the current target coordinates
at the new principal point.</p>
<p>By default, the principal point is located at the center of the map view.
It is set in pixels relative to the map view's origin top-left (0, 0).
Values outside the map view's dimensions (x &lt; 0 || x &gt; width, y &lt; 0 || y &gt; height)
will be rejected silently and the current principal point is kept.</p>
<p>The value of the principal point is adjusted when the dimensions of the
map view change, so that it stays in the same point relative to width
and height. Meaning that when a principal point it set to bottom
middle of the map view, it will stay in the bottom middle regardless
of the changes to dimensions and orientation of the view.</p>
<p>Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom)
and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate,
are not affected.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set principalPoint(Point2D value);</code></pre>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcamera-class</li>
<li class="self-crumb">principalPoint property</li>
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
</div></div>
</div>
`
}</HTMLBlock>
