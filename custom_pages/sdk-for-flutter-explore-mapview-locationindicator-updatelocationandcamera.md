---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationAndCamera.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">updateLocationAndCamera abstract method</li>
</ol>
<div class="self-name">updateLocationAndCamera</div>
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
<div class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>updateLocationAndCamera abstract method</h1></div>
<section class="multi-line-signature">
void
updateLocationAndCamera(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-location-class location, </li>
<li>/sdk-for-flutter-explore-mapview-mapcameraupdate-class cameraUpdate</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Updates the indicator to a new location and applies a camera update at the same time.</p>
<p>Does nothing if the indicator instance is not enabled.
If accuracy visualized is set to <code>true</code> the field /sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters
determines the size of the accuracy indicator halo.</p>
<p>The altitude of the location is ignored.</p>
<ul>
<li>
<p><code>location</code> The updated location of the user.</p>
</li>
<li>
<p><code>cameraUpdate</code> The update to apply to the camera.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void updateLocationAndCamera(Location location, MapCameraUpdate cameraUpdate);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">updateLocationAndCamera abstract method</li>
</ol>
<h5>LocationIndicator class</h5>
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
