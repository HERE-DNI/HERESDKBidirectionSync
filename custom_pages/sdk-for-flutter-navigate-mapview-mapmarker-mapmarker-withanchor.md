---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker.withAnchor.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapmarker-class</li>
<li class="self-crumb">MapMarker.withAnchor factory constructor</li>
</ol>
<div class="self-name">MapMarker.withAnchor</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapMarker.withAnchor constructor</h1></div>
<section class="multi-line-signature">
MapMarker.withAnchor(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, </li>
<li>/sdk-for-flutter-navigate-mapview-mapimage-class image, </li>
<li>/sdk-for-flutter-navigate-core-anchor2d-class anchor</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an instance of a marker at given coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the marker's coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image's dimensions on the screen.
For example, (0, 0) places the top-left corner of the image at the marker's coordinates.
(1, 1) would place the bottom-right corner of the image at the marker's coordinates.
(0.5, 0.5) which is the default value would center the image at the marker's coordinates.
Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the marker's coordinates at the distance
in pixels that is equal to the height of the image.</p>
<ul>
<li>
<p><code>coordinates</code> The marker's geographical coordinates.</p>
</li>
<li>
<p><code>image</code> The image to draw on the map.</p>
</li>
<li>
<p><code>anchor</code> The anchor point for the marker image which specifies the position offset relative
to the marker's coordinates.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker.withAnchor(GeoCoordinates coordinates, MapImage image, Anchor2D anchor) =&gt; $prototype.withAnchor(coordinates, image, anchor);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapmarker-class</li>
<li class="self-crumb">MapMarker.withAnchor factory constructor</li>
</ol>
<h5>MapMarker class</h5>
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
