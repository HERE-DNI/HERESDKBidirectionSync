---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-zoomby"
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
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
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
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
zoomBy(<wbr/><ol class="parameter-list single-line"> <li>double factor, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class origin</li>
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
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
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



</div>
`
}</HTMLBlock>
