---
title: "PolylineSimplificationCallback typedef"
slug: "sdk-for-flutter-explore-core-polylinesimplificationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplificationCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">PolylineSimplificationCallback typedef</li>
</ol>
<div class="self-name">PolylineSimplificationCallback</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PolylineSimplificationCallback typedef</h1></div>
<section class="multi-line-signature">
PolylineSimplificationCallback =
     void Function(/sdk-for-flutter-explore-core-polylinesimplificationerror? queryError, List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt;? result)
</section>
<section class="desc markdown">
<p>The method will be called on the main thread when
/sdk-for-flutter-explore-core-polylinesimplifier-simplify is finished.</p>
<ul>
<li>
<p><code>queryError</code> The optional error, which occurred during
simplification.</p>
</li>
<li>
<p><code>result</code> The simplified polyline with number of
points less or equal to the input polyline
of /sdk-for-flutter-explore-core-polylinesimplifier-simplify.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PolylineSimplificationCallback = void Function(PolylineSimplificationError? queryError, List&lt;GeoCoordinates&gt;? result);</code></pre>
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
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">PolylineSimplificationCallback typedef</li>
</ol>
<h5>core library</h5>
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
