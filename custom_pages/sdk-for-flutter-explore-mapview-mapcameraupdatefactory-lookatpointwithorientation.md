---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithorientation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- lookAtPointWithOrientation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraUpdateFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</a></li>
<li class="self-crumb">lookAtPointWithOrientation static method</li>
</ol>
<div class="self-name">lookAtPointWithOrientation</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lookAtPointWithOrientation static method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a>
lookAtPointWithOrientation(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoCoordinatesUpdate-class.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-class</a> target, </li>
<li><a href="../../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to position the map camera to look at the given target with the given
orientation preserving the current map measure (zoom level/distance/scale)
Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
</ul>
<p>Returns <a href="../../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a>. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPointWithOrientation(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation) =&gt; $prototype.lookAtPointWithOrientation(target, orientation);</code></pre>
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
<li><a href="../../mapview/MapCameraUpdateFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</a></li>
<li class="self-crumb">lookAtPointWithOrientation static method</li>
</ol>
<h5>MapCameraUpdateFactory class</h5>
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
