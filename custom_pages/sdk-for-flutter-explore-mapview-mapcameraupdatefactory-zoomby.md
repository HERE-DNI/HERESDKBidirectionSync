---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomby"
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
<li><a href="../../mapview/MapCameraUpdateFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</a></li>
<li class="self-crumb">zoomBy static method</li>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>zoomBy static method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a>
zoomBy(<wbr/><ol class="parameter-list single-line"> <li>double factor, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> origin</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to zoom map camera by a given factor preserving a given focus point.</p>
<p>Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out,
which moves map camera further.</p>
<p>If factor is zero, negative or not finite, no update will be applied to the map camera.</p>
<p>If the focusPoint is not inside the viewport bounds, then the current principal point will be used.</p>
<ul>
<li>
<p><code>factor</code> Zooming factor.</p>
</li>
<li>
<p><code>origin</code> Pixel location on the screen to use as zoom origin.</p>
</li>
</ul>
<p>Returns <a href="../../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a>. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate zoomBy(double factor, Point2D origin) =&gt; $prototype.zoomBy(factor, origin);</code></pre>
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
<li><a href="../../mapview/MapCameraUpdateFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</a></li>
<li class="self-crumb">zoomBy static method</li>
</ol>
<h5>MapCameraUpdateFactory class</h5>
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
