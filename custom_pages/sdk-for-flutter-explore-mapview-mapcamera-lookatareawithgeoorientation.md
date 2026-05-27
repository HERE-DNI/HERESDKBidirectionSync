---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a></li>
<li class="self-crumb">lookAtAreaWithGeoOrientation abstract method</li>
</ol>
<div class="self-name">lookAtAreaWithGeoOrientation</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lookAtAreaWithGeoOrientation abstract method</h1></div>
<section class="multi-line-signature">
void
lookAtAreaWithGeoOrientation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> target, </li>
<li><a href="../../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Makes the camera look at the specified geodetic area.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method.</p>
<p>The altitude of the target points is ignored.</p>
<ul>
<li>
<p><code>target</code> Geodetic area at which the camera will point</p>
</li>
<li>
<p><code>orientation</code> Desired orientation of the camera</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtAreaWithGeoOrientation(GeoBox target, GeoOrientationUpdate orientation);</code></pre>
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
<li><a href="../../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a></li>
<li class="self-crumb">lookAtAreaWithGeoOrientation abstract method</li>
</ol>
<h5>MapCamera class</h5>
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
