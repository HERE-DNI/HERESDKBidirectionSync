---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-setbearingrangeatzoom"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- setBearingRangeAtZoom.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraLimits-class.html">/sdk-for-flutter-explore-mapview-mapcameralimits-class</a></li>
<li class="self-crumb">setBearingRangeAtZoom abstract method</li>
</ol>
<div class="self-name">setBearingRangeAtZoom</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraLimits-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setBearingRangeAtZoom abstract method</h1></div>
<section class="multi-line-signature">
void
setBearingRangeAtZoom(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> zoom, </li>
<li><a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a> bearingRange</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the bearing range within which the camera can rotate at a given zoom.</p>
<p>The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no bearing range is specified for <a href="../../mapview/MapCameraLimits/minZoomLevel.html">/sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel</a>, the bearing range set through
<a href="../../mapview/MapCameraLimits/bearingRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange</a> is used for interpolation.</p>
<p>Zoom values outside the supported zoom range are ignored.
By default, the maximum bearing range for all zoom values is set during initialization.</p>
<ul>
<li>
<p><code>zoom</code> Zoom at which the range is set.</p>
</li>
<li>
<p><code>bearingRange</code> Bearing range.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setBearingRangeAtZoom(MapMeasure zoom, AngleRange bearingRange);</code></pre>
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
<li><a href="../../mapview/MapCameraLimits-class.html">/sdk-for-flutter-explore-mapview-mapcameralimits-class</a></li>
<li class="self-crumb">setBearingRangeAtZoom abstract method</li>
</ol>
<h5>MapCameraLimits class</h5>
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
