---
title: "isRenderInternalsEnabled property"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-isrenderinternalsenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isRenderInternalsEnabled.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker3d-class</li>
<li class="self-crumb">isRenderInternalsEnabled property</li>
</ol>
<div class="self-name">isRenderInternalsEnabled</div>
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
<h1>isRenderInternalsEnabled property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isRenderInternalsEnabled
</section>
<section class="desc markdown">
<p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.</p>
<p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
passes: first pass with front-face, second pass with back-face culling enabled.
With this flag enabled for 3D marker with depth check disabled rendering is performed in a
single pass with back-face culling disabled.
Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front
facing polygons. Default value is <code>false</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isRenderInternalsEnabled;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isRenderInternalsEnabled=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.</p>
<p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
passes: first pass with front-face, second pass with back-face culling enabled.
With this flag enabled for 3D marker with depth check disabled rendering is performed in a
single pass with back-face culling disabled.
Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front
facing polygons.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isRenderInternalsEnabled(bool value);</code></pre>
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
<li class="self-crumb">isRenderInternalsEnabled property</li>
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
