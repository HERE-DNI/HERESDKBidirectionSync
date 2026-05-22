---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-isdepthcheckenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isDepthCheckEnabled.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker3d-class</li>
<li class="self-crumb">isDepthCheckEnabled property</li>
</ol>
<div class="self-name">isDepthCheckEnabled</div>
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
<h1>isDepthCheckEnabled property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isDepthCheckEnabled
</section>
<section class="desc markdown">
<p>Determines whether the depth of the 3D marker's vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p>
<p>By default depth check is set to <code>false</code>.</p>
<p>Use the altitude of the /sdk-for-flutter-explore-mapview-mapmarker3d-coordinates to position the 3D marker sufficiently high above the
surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
3D model unexpectedly shine through.
Returns <code>true</code> if depth check is enabled.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isDepthCheckEnabled;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isDepthCheckEnabled=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>Determines whether the depth of the 3D marker's vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p>
<p>By default depth check is set to <code>false</code>.</p>
<p>Use the altitude of the /sdk-for-flutter-explore-mapview-mapmarker3d-coordinates to position the 3D marker sufficiently high above the
surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
3D model unexpectedly shine through.
Set whether the depth of the 3D marker's vertices is considered during rendering.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isDepthCheckEnabled(bool value);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapmarker3d-class</li>
<li class="self-crumb">isDepthCheckEnabled property</li>
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
