---
title: "opacity property"
slug: "sdk-for-flutter-explore-mapview-mapmarkercluster-opacity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- opacity.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarkercluster-class</li>
<li class="self-crumb">opacity property</li>
</ol>
<div class="self-name">opacity</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarkerCluster-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>opacity property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double
opacity
</section>
<section class="desc markdown">
<p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Gets the current opacity of the marker cluster image.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get opacity;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
opacity=(<wbr/>double value)
</section>
<section class="desc markdown">
<p>Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Sets the opacity of the marker cluster image.</p>
<p>Provided value is clamped in range [0.0, 1.0]. Default value is 1.0 which means marker cluster
is displayed with the default opacity of the image.</p>
<p>Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.</p>
<p>Markers part of cluster will use their respective opacity when not displayed as a cluster icon.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set opacity(double value);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapmarkercluster-class</li>
<li class="self-crumb">opacity property</li>
</ol>
<h5>MapMarkerCluster class</h5>
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
