---
title: "pixelScale property"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pixelScale.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
<li class="self-crumb">pixelScale property</li>
</ol>
<div class="self-name">pixelScale</div>
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
<div class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>pixelScale property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double
pixelScale
</section>
<section class="desc markdown">
<p>The pixel scale factor used by this <code>MapView</code>.</p>
<p>Pixel scale is 0.0 if the map view is not initialized.</p>
<p>In cases where the <code>MapView</code> moves in between screens (e.g. from main screen to a CarPlay screen),
/ the most up-to-date pixel scale value can be obtained after a render target gets attached to the view.
/ To get notified when a render target gets attached to the <code>MapView</code>, see /sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class.
It is used to support screen resolution and size independence.
This value is a derivative of the device's screen pixel density and is a direct analog of</p>
<p>devicePixelRatio from FlutterView, ViewConfiguration or MediaQueryData.
It can be used to translate between physical pixels and</p>
<p>logical pixels
according to the formula:</p>
<p>logicalPixels = pixels / pixelScale.
Gets the pixel scale factor used by this <code>MapView</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get pixelScale;</code></pre>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
<li class="self-crumb">pixelScale property</li>
</ol>
<h5>MapViewBase class</h5>
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
