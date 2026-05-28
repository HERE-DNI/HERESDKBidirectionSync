---
title: "MapImageOverlay.withAnchor constructor"
slug: "sdk-for-flutter-navigate-mapview-mapimageoverlay-mapimageoverlay-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay.withAnchor.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapimageoverlay-class</li>
<li class="self-crumb">MapImageOverlay.withAnchor factory constructor</li>
</ol>
<div class="self-name">MapImageOverlay.withAnchor</div>
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
<div class="main-content" data-above-sidebar="mapview/MapImageOverlay-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapImageOverlay.withAnchor constructor</h1></div>
<section class="multi-line-signature">
MapImageOverlay.withAnchor(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-point2d-class viewCoordinates, </li>
<li>/sdk-for-flutter-navigate-mapview-mapimage-class image, </li>
<li>/sdk-for-flutter-navigate-core-anchor2d-class anchor</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an instance of an overlay at given view coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the overlay's view coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image's dimensions on the view.
For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
(1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
(0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.</p>
<p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the overlay's view coordinates at the distance
in pixels that is equal to the height of the image.</p>
<ul>
<li>
<p><code>viewCoordinates</code> The overlay's view coordinates in pixels.</p>
</li>
<li>
<p><code>image</code> The image to draw on the map.</p>
</li>
<li>
<p><code>anchor</code> The anchor point for the overlay image which specifies the position offset relative
to the overlay's view coordinates.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapImageOverlay.withAnchor(Point2D viewCoordinates, MapImage image, Anchor2D anchor) =&gt; $prototype.withAnchor(viewCoordinates, image, anchor);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapimageoverlay-class</li>
<li class="self-crumb">MapImageOverlay.withAnchor factory constructor</li>
</ol>
<h5>MapImageOverlay class</h5>
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
