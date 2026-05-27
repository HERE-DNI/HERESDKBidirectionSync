---
title: "MapCameraState constructor"
slug: "sdk-for-flutter-explore-mapview-mapcamerastate-mapcamerastate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraState.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcamerastate-class</li>
<li class="self-crumb">MapCameraState constructor</li>
</ol>
<div class="self-name">MapCameraState</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraState-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapCameraState constructor</h1></div>
<section class="multi-line-signature">
MapCameraState(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-core-geocoordinates-class targetCoordinates, </li>
<li>/sdk-for-flutter-explore-core-geoorientation-class orientationAtTarget, </li>
<li>double distanceToTargetInMeters, </li>
<li>double zoomLevel, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>targetCoordinates</code> Camera's 'LookAt' target position in geodetic space.</li>
</ul>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>orientationAtTarget</code> Camera's orientation at target point.</li>
<li><code>distanceToTargetInMeters</code> Distance from the camera to the target point in meters.</li>
<li><code>zoomLevel</code> Zoom level corresponding to the current distance to target.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapCameraState(this.targetCoordinates, this.orientationAtTarget, this.distanceToTargetInMeters, this.zoomLevel);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcamerastate-class</li>
<li class="self-crumb">MapCameraState constructor</li>
</ol>
<h5>MapCameraState class</h5>
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
