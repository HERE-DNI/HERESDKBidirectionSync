---
title: "maxPoints property"
slug: "sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maxPoints.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-polylinesimplifieroptions-class</li>
<li class="self-crumb">maxPoints property</li>
</ol>
<div class="self-name">maxPoints</div>
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
<div class="main-content" data-above-sidebar="core/PolylineSimplifierOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>maxPoints property</h1></div>
<section class="multi-line-signature">
        
        int
        maxPoints
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Sets the upper limit on the resulting collection for
the /sdk-for-flutter-explore-core-polylinesimplifier-simplify. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int maxPoints;</code></pre>
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
<li>/sdk-for-flutter-explore-core-polylinesimplifieroptions-class</li>
<li class="self-crumb">maxPoints property</li>
</ol>
<h5>PolylineSimplifierOptions class</h5>
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
