---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-locationindicator-enable"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- enable.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a></li>
<li class="self-crumb">enable abstract method</li>
</ol>
<div class="self-name">enable</div>
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
<h1>enable abstract method</h1></div>
<section class="multi-line-signature">
void
enable(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a> mapView</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Enables <a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a> for provided <a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a>.</p>
<p>If <a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a> is already enabled (added to map view) for passed map view, this function does nothing.
If <a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a> is added to different <a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a>, this function removes first <a href="../../mapview/LocationIndicator-class.html">/sdk-for-flutter-explore-mapview-locationindicator-class</a>
from previous map view before adding to new one.</p>
<ul>
<li><code>mapView</code> The <a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a> instance.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void enable(MapViewBase mapView);</code></pre>
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
<li class="self-crumb">enable abstract method</li>
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
