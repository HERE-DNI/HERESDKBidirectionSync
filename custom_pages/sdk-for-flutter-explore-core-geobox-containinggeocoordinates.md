---
title: "containingGeoCoordinates static method"
slug: "sdk-for-flutter-explore-core-geobox-containinggeocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- containingGeoCoordinates.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geobox-class</li>
<li class="self-crumb">containingGeoCoordinates static method</li>
</ol>
<div class="self-name">containingGeoCoordinates</div>
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
<div class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>containingGeoCoordinates static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-geobox-class?
containingGeoCoordinates(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt; geoCoordinates</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a <code>GeoBox</code> which encompases all coordinates from the list.</p>
<p>The provided list must contain at least two points.
The altitude values of the input coordinates are not considered for the result.</p>
<ul>
<li><code>geoCoordinates</code> List of coordinates to encompass inside bounding box.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-geobox-class. <code>GeoBox</code> containing all supplied coordinates, or <code>null</code> if less than two coordinates were provided.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static GeoBox? containingGeoCoordinates(List&lt;GeoCoordinates&gt; geoCoordinates) =&gt; $prototype.containingGeoCoordinates(geoCoordinates);</code></pre>
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
<li>/sdk-for-flutter-explore-core-geobox-class</li>
<li class="self-crumb">containingGeoCoordinates static method</li>
</ol>
<h5>GeoBox class</h5>
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
