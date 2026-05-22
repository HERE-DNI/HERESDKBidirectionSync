---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientationAndViewRectangle.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">lookAtAreaWithGeoOrientationAndViewRectangle static method</li>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lookAtAreaWithGeoOrientationAndViewRectangle static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
lookAtAreaWithGeoOrientationAndViewRectangle(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geobox-class target, </li>
<li>/sdk-for-flutter-navigate-core-geoorientationupdate-class orientation, </li>
<li>/sdk-for-flutter-navigate-core-rectangle2d-class viewRectangle</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Create an update to look at the given geo-box and fit it inside the given rectangle.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>All <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> values need to be finite to be considered as valid.</p>
<p>In cases where it is not possible to find a solution for the given parameters,
the resulting MapCameraUpdate will not change the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> Geodetic box that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at the target point.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle) =&gt; $prototype.lookAtAreaWithGeoOrientationAndViewRectangle(target, orientation, viewRectangle);</code></pre>
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
<li class="self-crumb">lookAtAreaWithGeoOrientationAndViewRectangle static method</li>
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
