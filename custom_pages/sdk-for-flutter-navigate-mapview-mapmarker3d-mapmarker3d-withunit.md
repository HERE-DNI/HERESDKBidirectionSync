---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-withunit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.withUnit.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapmarker3d-class</li>
<li class="self-crumb">MapMarker3D.withUnit factory constructor</li>
</ol>
<div class="self-name">MapMarker3D.withUnit</div>
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
<h1>MapMarker3D.withUnit constructor</h1></div>
<section class="multi-line-signature">
MapMarker3D.withUnit(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class at, </li>
<li>/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class model, </li>
<li>double scale, </li>
<li>/sdk-for-flutter-navigate-mapview-rendersizeunit unit, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p>
<p>The unit specifies how the 3D geometry of the model is interpreted (meters for world space,
pixels or density independent pixels for screen space), while scale determines its relative size.</p>
<p>For /sdk-for-flutter-navigate-mapview-rendersizeunit one unit of the 3D marker model will cover <code>MapMarker3D.withUnit.scale</code> pixels.
The size of the 3D marker remains constant on the screen.</p>
<p>For /sdk-for-flutter-navigate-mapview-rendersizeunit one unit of the 3D marker model will
cover <code>MapMarker3D.withUnit.scale</code> density independent pixels. The size of the 3D marker remains constant on
the screen.</p>
<p>For /sdk-for-flutter-navigate-mapview-rendersizeunit one unit of the 3D marker model will cover <code>MapMarker3D.withUnit.scale</code> meters
in the real world. Unlike with pixels or density-independent pixels the size of the
3D marker will grow and shrink together with regular map content like streets or buildings.</p>
<p>The origin of the 3D model's local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<ul>
<li>
<p><code>at</code> The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model's local coordinate system.</p>
</li>
<li>
<p><code>model</code> The 3D model used to render the 3D marker.</p>
</li>
<li>
<p><code>scale</code> Scale factor to apply to the 3D model.</p>
</li>
<li>
<p><code>unit</code> Determines the unit of the model vertices and whether the size of the 3D marker
is expressed in world or screen space.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker3D.withUnit(GeoCoordinates at, MapMarker3DModel model, double scale, RenderSizeUnit unit) =&gt; $prototype.withUnit(at, model, scale, unit);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapmarker3d-class</li>
<li class="self-crumb">MapMarker3D.withUnit factory constructor</li>
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



</div>
`
}</HTMLBlock>
