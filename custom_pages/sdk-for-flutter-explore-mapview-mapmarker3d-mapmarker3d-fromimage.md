---
title: "MapMarker3D.fromImage constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.fromImage.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker3d-class</li>
<li class="self-crumb">MapMarker3D.fromImage factory constructor</li>
</ol>
<div class="self-name">MapMarker3D.fromImage</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapMarker3D.fromImage constructor</h1></div>
<section class="multi-line-signature">
MapMarker3D.fromImage(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-core-geocoordinates-class at, </li>
<li>/sdk-for-flutter-explore-mapview-mapimage-class image, </li>
<li>double scale, </li>
<li>/sdk-for-flutter-explore-mapview-rendersizeunit unit, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a flat marker from provided map image.</p>
<p>Such map marker is a flat 3D marker of rectangular shape textured with given image.
Aspect ratio of the flat marker is determined by aspect ratio of the image.</p>
<p>Only bitmap images are supported, using a /sdk-for-flutter-explore-mapview-mapimage-class created from SVG data
will result in distorted rendering of the flat marker.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Size of the rendered flat marker can be specified in either world or screen coordinate space.</p>
<p>For /sdk-for-flutter-explore-mapview-rendersizeunit, the flat marker will cover <code>MapMarker3D.fromImage.scale</code> * image's width pixels
horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height pixels vertically. The size of the flat marker
remains constant on the screen.</p>
<p>For /sdk-for-flutter-explore-mapview-rendersizeunit the flat marker will cover <code>MapMarker3D.fromImage.scale</code> *
image's width density independent pixels horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height
density independent pixels vertically. The size of the flat marker remains constant on
the screen.</p>
<p>For /sdk-for-flutter-explore-mapview-rendersizeunit the flat marker will cover <code>MapMarker3D.fromImage.scale</code> * image's width meters
horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height meters vertically. Unlike with pixels or
density independent pixels the size of the flat marker will grow and shrink together
with regular map content like streets or buildings.</p>
<ul>
<li>
<p><code>at</code> The geographical coordinates where the flat marker is placed corresponding to center of the
provided map image.</p>
</li>
<li>
<p><code>image</code> The MapImage containing the texture data of the flat marker. SVG images are not supported.</p>
</li>
<li>
<p><code>scale</code> Scale factor applied to the dimensions of the image.</p>
</li>
<li>
<p><code>unit</code> Determines whether the size of the flat marker is represented in world or in screen space.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker3D.fromImage(GeoCoordinates at, MapImage image, double scale, RenderSizeUnit unit) =&gt; $prototype.fromImage(at, image, scale, unit);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapmarker3d-class</li>
<li class="self-crumb">MapMarker3D.fromImage factory constructor</li>
</ol>
<h5>MapMarker3D class</h5>
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
`
}</HTMLBlock>
