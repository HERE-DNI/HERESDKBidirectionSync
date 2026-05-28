---
title: "lookToMatchGeoPointToViewPoint static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookToMatchGeoPointToViewPoint.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">lookToMatchGeoPointToViewPoint static method</li>
</ol>
<div class="self-name">lookToMatchGeoPointToViewPoint</div>
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
<h1>lookToMatchGeoPointToViewPoint static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
lookToMatchGeoPointToViewPoint(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class geoPoint, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class viewPoint</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to position the map camera to look at the map
with the given geo point located at the given view point.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>geoPoint</code> The geo point that will be matched to the given view point.
Note: the geo point will differ from the look at target of the camera. After this update the camera
will still look at the principal point and therefore the look at target will be different from the geo
point, since the geo point will correspond to the given view point and the look at target
will correspond to the principal point. Look at target and the geo point will be identical only
if the given view point is identical to the principal point.</p>
</li>
<li>
<p><code>viewPoint</code> View point coordinates in pixels.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookToMatchGeoPointToViewPoint(GeoCoordinates geoPoint, Point2D viewPoint) =&gt; $prototype.lookToMatchGeoPointToViewPoint(geoPoint, viewPoint);</code></pre>
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
<li class="self-crumb">lookToMatchGeoPointToViewPoint static method</li>
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
`
}</HTMLBlock>
