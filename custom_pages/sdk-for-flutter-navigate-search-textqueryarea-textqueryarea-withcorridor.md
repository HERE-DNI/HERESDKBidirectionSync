---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-textqueryarea-textqueryarea-withcorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TextQueryArea.withCorridor.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-textqueryarea-class</li>
<li class="self-crumb">TextQueryArea.withCorridor factory constructor</li>
</ol>
<div class="self-name">TextQueryArea.withCorridor</div>
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
<h1>TextQueryArea.withCorridor constructor</h1></div>
<section class="multi-line-signature">
TextQueryArea.withCorridor(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocorridor-class corridorArea, </li>
<li>/sdk-for-flutter-navigate-core-geocoordinates-class areaCenter</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs a new instance of this class from provided parameters.</p>
<p>The given corridor and center define the area that will be used in the search query.</p>
<p>When used with SearchEngine, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>The area center has to be within the corridor, otherwise it is ignored.</p>
<p>For Offline Search, search in a given <code>GeoCorridor</code> restricts the results to only POIs.</p>
<ul>
<li>
<p><code>corridorArea</code> Geographic corridor area in which to provide the most relevant places.</p>
</li>
<li>
<p><code>areaCenter</code> Geographic coordinates of the prioritized area center.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TextQueryArea.withCorridor(GeoCorridor corridorArea, GeoCoordinates areaCenter) =&gt; $prototype.withCorridor(corridorArea, areaCenter);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-textqueryarea-class</li>
<li class="self-crumb">TextQueryArea.withCorridor factory constructor</li>
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



</div>
`
}</HTMLBlock>
