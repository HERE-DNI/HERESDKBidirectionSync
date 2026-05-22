---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookattargetandpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtTargetAndPoints.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">lookAtTargetAndPoints static method</li>
</ol>
<div class="self-name">lookAtTargetAndPoints</div>
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
<h1>lookAtTargetAndPoints static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
lookAtTargetAndPoints(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-geocoordinatesupdate-class target, </li>
<li>/sdk-for-flutter-navigate-core-geoorientationupdate-class orientation, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; points, </li>
<li>/sdk-for-flutter-navigate-core-rectangle2d-class viewRectangle, </li>
<li>/sdk-for-flutter-navigate-mapview-mapmeasure-class minMeasure, </li>
<li>/sdk-for-flutter-navigate-mapview-mapmeasure-class maxMeasure, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to position the camera to look at the given target with the given
orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.</p>
<p>Such position update can possibly not be found.</p>
<p>Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>If the provided <code>MapCameraUpdateFactory.lookAtTargetAndPoints.points</code> list is empty, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>If map measures are not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
<li>
<p><code>points</code> Array of points in geodetic space that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p>
</li>
<li>
<p><code>minMeasure</code> Minimum map measure:</p>
</li>
<li>
<p>as distance: the minimum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned closer to target than this.</p>
</li>
<li>
<p>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom closer than a given level.</p>
</li>
<li>
<p>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</p>
</li>
<li>
<p><code>maxMeasure</code> Maximum map measure:</p>
</li>
<li>
<p>as distance: the maximum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned further from target than this.</p>
</li>
<li>
<p>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom further than a given level.</p>
</li>
<li>
<p>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtTargetAndPoints(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, List&lt;GeoCoordinates&gt; points, Rectangle2D viewRectangle, MapMeasure minMeasure, MapMeasure maxMeasure) =&gt; $prototype.lookAtTargetAndPoints(target, orientation, points, viewRectangle, minMeasure, maxMeasure);</code></pre>
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
<li class="self-crumb">lookAtTargetAndPoints static method</li>
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
