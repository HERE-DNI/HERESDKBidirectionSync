---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- tiltRange.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraLimits-class.html">/sdk-for-flutter-explore-mapview-mapcameralimits-class</a></li>
<li class="self-crumb">tiltRange property</li>
</ol>
<div class="self-name">tiltRange</div>
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
<h1>tiltRange property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a>
tiltRange
</section>
<section class="desc markdown">
<p>The tilt range that can be applied to the camera.
Gets the current tilt range.</p>
<p>By default, a <a href="../../mapview/MapCameraLimits/minTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-mintilt</a>-<a href="../../mapview/MapCameraLimits/maxTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt</a> tilt range is set during initialization.</p>
<p>This range might not be yet active if no rendering loop has been executed since the last call to set the range.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AngleRange get tiltRange;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
tiltRange=(<wbr/><a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a> value)
</section>
<section class="desc markdown">
<p>The tilt range that can be applied to the camera.
Sets a new tilt limit range.</p>
<p>The supported values fall inside <a href="../../mapview/MapCameraLimits/minTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-mintilt</a>-<a href="../../mapview/MapCameraLimits/maxTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt</a> range.
Values outside the supported range are ignored.</p>
<p>If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum,
depending on which is closest.</p>
<p>This new limit range becomes active during the next rendering loop.</p>
<p>All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set tiltRange(AngleRange value);</code></pre>
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
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraLimits-class.html">/sdk-for-flutter-explore-mapview-mapcameralimits-class</a></li>
<li class="self-crumb">tiltRange property</li>
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
