---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- bearingRange.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameralimits-class</li>
<li class="self-crumb">bearingRange property</li>
</ol>
<div class="self-name">bearingRange</div>
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
<h1>bearingRange property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-anglerange-class
bearingRange
</section>
<section class="desc markdown">
<p>The bearing range within which the camera can be rotated.
Gets the currently set bearing range.</p>
<p>This may not be active now if no rendering loop has been executed since
the last call to set the range.</p>
<p>By default, range for a full circle is set during initialization.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AngleRange get bearingRange;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
bearingRange=(<wbr/>/sdk-for-flutter-explore-core-anglerange-class value)
</section>
<section class="desc markdown">
<p>The bearing range within which the camera can be rotated.
Sets a new bearing range.</p>
<p>It will be updated during the next rendering loop.
All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.</p>
<p>If the current camera bearing exceeds the limit range, it will immediately be set to minimum or
maximum, depending on which is closest.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set bearingRange(AngleRange value);</code></pre>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameralimits-class</li>
<li class="self-crumb">bearingRange property</li>
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
