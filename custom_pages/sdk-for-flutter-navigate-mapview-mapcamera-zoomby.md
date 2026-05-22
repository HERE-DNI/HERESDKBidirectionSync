---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-zoomby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomBy.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
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
<li>/sdk-for-flutter-navigate-core-point2d-class origin</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Zooms in or out by a specified factor.</p>
<p>This effectively changes the distance from the camera to the /sdk-for-flutter-navigate-mapview-mapcamerastate-targetcoordinates
by the specified factor, which changes /sdk-for-flutter-navigate-mapview-mapcamerastate-zoomlevel as well.</p>
<p>Values above 1.0 will zoom in and values below will zoom out.</p>
<p>The relation with /sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters is inversely linear,
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
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



</div>
`
}</HTMLBlock>
