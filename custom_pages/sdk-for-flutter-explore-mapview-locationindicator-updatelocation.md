---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-locationindicator-updatelocation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- updateLocation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a></li>
<li class="self-crumb">updateLocation abstract method</li>
</ol>
<div class="self-name">updateLocation</div>
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
<h1>updateLocation abstract method</h1></div>
<section class="multi-line-signature">
void
updateLocation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/Location-class.html">/sdk-for-flutter-explore-core-location-class</a> location</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Updates the indicator to a new location.</p>
<p>If accuracy visualized is set to <code>true</code> the field <a href="../../core/Location/horizontalAccuracyInMeters.html">/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters</a>
determines the size of the accuracy indicator halo.</p>
<p>The altitude of the location is ignored.</p>
<ul>
<li><code>location</code> The updated location of the user.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void updateLocation(Location location);</code></pre>
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
<li><a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a></li>
<li class="self-crumb">updateLocation abstract method</li>
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
</div></div>
</div>
</HTMLBlock>
