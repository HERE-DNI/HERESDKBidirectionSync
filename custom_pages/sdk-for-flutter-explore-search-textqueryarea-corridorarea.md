---
title: "corridorArea property"
slug: "sdk-for-flutter-explore-search-textqueryarea-corridorarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- corridorArea.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-search-textqueryarea-class</li>
<li class="self-crumb">corridorArea property</li>
</ol>
<div class="self-name">corridorArea</div>
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
<div class="main-content" data-above-sidebar="search/TextQueryArea-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>corridorArea property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-geocorridor-class?
        corridorArea
<div class="features">final</div>
</section>
<section class="desc markdown">
<p>Geographic corridor area in which to provide the most relevant places.
The contained polyline and half-width define the area that will be used in a search query.</p>
<p>When used with SearchEngine, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>When /sdk-for-flutter-explore-search-textqueryarea-corridorarea is provided,
/sdk-for-flutter-explore-search-textqueryarea-areacenter has to be within it, otherwise
/sdk-for-flutter-explore-search-textqueryarea-areacenter is ignored when searching.</p>
<p>For Offline Search, search in a given <code>GeoCorridor</code> restricts the results to only POIs.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final GeoCorridor? corridorArea;</code></pre>
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
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-search-textqueryarea-class</li>
<li class="self-crumb">corridorArea property</li>
</ol>
<h5>TextQueryArea class</h5>
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
