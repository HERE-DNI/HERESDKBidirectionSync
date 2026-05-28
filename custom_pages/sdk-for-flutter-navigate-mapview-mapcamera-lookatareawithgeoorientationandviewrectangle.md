---
title: "lookAtAreaWithGeoOrientationAndViewRectangle abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientationAndViewRectangle.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
<li class="self-crumb">lookAtAreaWithGeoOrientationAndViewRectangle abstract method</li>
</ol>
<div class="self-name">lookAtAreaWithGeoOrientationAndViewRectangle</div>
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
<h1>lookAtAreaWithGeoOrientationAndViewRectangle abstract method</h1></div>
<section class="multi-line-signature">
void
lookAtAreaWithGeoOrientationAndViewRectangle(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geobox-class target, </li>
<li>/sdk-for-flutter-navigate-core-geoorientationupdate-class orientation, </li>
<li>/sdk-for-flutter-navigate-core-rectangle2d-class viewRectangle</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Makes the camera look at the specified geodetic area and pass a rectangle which specifies
where the area should appear inside of the map view.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method. Please note that
the resulting orientation might deviate from the provided orientation.
This is particularly the case if a large geobox on world level and a
view rectangle which is relatively small was passed to the method.</p>
<p>The altitude of the target points is ignored.</p>
<ul>
<li>
<p><code>target</code> Geodetic area which will be shown in the viewRectangle.</p>
</li>
<li>
<p><code>orientation</code> Desired orientation of the camera.</p>
</li>
<li>
<p><code>viewRectangle</code> The view rectangle in viewport pixel coordinates inside which the geographical target
area is displayed.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle);</code></pre>
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
<li class="self-crumb">lookAtAreaWithGeoOrientationAndViewRectangle abstract method</li>
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
