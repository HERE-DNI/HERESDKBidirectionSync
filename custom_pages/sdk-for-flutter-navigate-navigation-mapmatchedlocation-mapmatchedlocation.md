---
title: "MapMatchedLocation constructor"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-mapmatchedlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatchedLocation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class</li>
<li class="self-crumb">MapMatchedLocation constructor</li>
</ol>
<div class="self-name">MapMatchedLocation</div>
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
<div class="main-content" data-above-sidebar="navigation/MapMatchedLocation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapMatchedLocation constructor</h1></div>
<section class="multi-line-signature">
MapMatchedLocation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, </li>
<li>double? bearingInDegrees</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>coordinates</code> The geographic coordinates of the map-matched location.</li>
<li><code>bearingInDegrees</code> The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
for east it's equal to 90, and so on.
If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
range [0, 360).</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMatchedLocation(this.coordinates, this.bearingInDegrees)
    : segmentReference = SegmentReference.withDefaults(), segmentOffsetInCentimeters = 0, confidence = 0.0, isDrivingInTheWrongWay = false, horizontalAccuracyInMeters = null, speedInMetersPerSecond = null, timestamp = null;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class</li>
<li class="self-crumb">MapMatchedLocation constructor</li>
</ol>
<h5>MapMatchedLocation class</h5>
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
