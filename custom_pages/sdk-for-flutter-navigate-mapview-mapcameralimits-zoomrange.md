---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-zoomrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomRange.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameralimits-class</li>
<li class="self-crumb">zoomRange property</li>
</ol>
<div class="self-name">zoomRange</div>
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
<h1>zoomRange property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapmeasurerange-class
zoomRange
</section>
<section class="desc markdown">
<p>The zoom range that can be applied to the camera.
Gets the currently set camera zoom range.</p>
<p>By default, a /sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel-/sdk-for-flutter-navigate-mapview-mapcameralimits-maxzoomlevel zoom range is set during initialization.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureRange get zoomRange;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
zoomRange=(<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasurerange-class value)
</section>
<section class="desc markdown">
<p>The zoom range that can be applied to the camera.
Sets a new camera zoom range.</p>
<p>The supported values fall inside /sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel-/sdk-for-flutter-navigate-mapview-mapcameralimits-maxzoomlevel range.
Values outside the supported zoom range are ignored.</p>
<p>If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.</p>
<p>This new limit range becomes active during the next rendering loop.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set zoomRange(MapMeasureRange value);</code></pre>
</section>
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
<li class="self-crumb">zoomRange property</li>
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
