---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-settiltrangeatzoom"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setTiltRangeAtZoom.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameralimits-class</li>
<li class="self-crumb">setTiltRangeAtZoom abstract method</li>
</ol>
<div class="self-name">setTiltRangeAtZoom</div>
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
<h1>setTiltRangeAtZoom abstract method</h1></div>
<section class="multi-line-signature">
void
setTiltRangeAtZoom(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapmeasure-class zoom, </li>
<li>/sdk-for-flutter-navigate-core-anglerange-class tiltRange</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets tilt ranges that can be set on the camera at given zoom.</p>
<p>The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no tilt range is specified for /sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel, the tilt range set through /sdk-for-flutter-navigate-mapview-mapcameralimits-tiltrange is used for interpolation.</p>
<p>Zoom or tilt values outside the supported zoom and tilt range are ignored.
By default, the maximum tilt range for all zoom values is set during initialization.</p>
<ul>
<li>
<p><code>zoom</code> Zoom at which the range is set.</p>
</li>
<li>
<p><code>tiltRange</code> Tilt range.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setTiltRangeAtZoom(MapMeasure zoom, AngleRange tiltRange);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcameralimits-class</li>
<li class="self-crumb">setTiltRangeAtZoom abstract method</li>
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



</div>
`
}</HTMLBlock>
