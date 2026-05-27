---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcamera-zoomby"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- zoomBy.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a></li>
<li class="self-crumb">zoomBy abstract method</li>
</ol>
<div class="self-name">zoomBy</div>
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
<h1>zoomBy abstract method</h1></div>
<section class="multi-line-signature">
void
zoomBy(<wbr/><ol class="parameter-list single-line"> <li>double factor, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> origin</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Zooms in or out by a specified factor.</p>
<p>This effectively changes the distance from the camera to the <a href="../../mapview/MapCameraState/targetCoordinates.html">/sdk-for-flutter-explore-mapview-mapcamerastate-targetcoordinates</a>
by the specified factor, which changes <a href="../../mapview/MapCameraState/zoomLevel.html">/sdk-for-flutter-explore-mapview-mapcamerastate-zoomlevel</a> as well.</p>
<p>Values above 1.0 will zoom in and values below will zoom out.</p>
<p>The relation with <a href="../../mapview/MapCameraState/distanceToTargetInMeters.html">/sdk-for-flutter-explore-mapview-mapcamerastate-distancetotargetinmeters</a> is inversely linear,
meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5
will increase distance to target by 2.</p>
<p>The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will
increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom
factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).</p>
<p>The zooming occurs around the specified origin inside the view.</p>
<ul>
<li>
<p><code>factor</code> The zoom factor. Values above 1.0 will zoom in and values below will zoom out.</p>
</li>
<li>
<p><code>origin</code> Pixel point in view coordinates around which zooming occurs.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void zoomBy(double factor, Point2D origin);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a></li>
<li class="self-crumb">zoomBy abstract method</li>
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
</HTMLBlock>
