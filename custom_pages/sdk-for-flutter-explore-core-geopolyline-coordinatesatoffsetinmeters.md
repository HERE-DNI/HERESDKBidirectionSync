---
title: "coordinatesAtOffsetInMeters method"
slug: "sdk-for-flutter-explore-core-geopolyline-coordinatesatoffsetinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- coordinatesAtOffsetInMeters.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geopolyline-class</li>
<li class="self-crumb">coordinatesAtOffsetInMeters method</li>
</ol>
<div class="self-name">coordinatesAtOffsetInMeters</div>
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
<div class="main-content" data-above-sidebar="core/GeoPolyline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>coordinatesAtOffsetInMeters method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-geocoordinates-class
coordinatesAtOffsetInMeters(<wbr/><ol class="parameter-list single-line"> <li>double offsetInMeters, </li>
<li>/sdk-for-flutter-explore-core-geopolylinedirection direction</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns the coordinates at the given distance along the polyline.</p>
<p>When the polyline is
traversed from the beginning, the distance is calculated from the start of the
polyline; while a direction from the end indicates a distance from the last vertex.</p>
<p>The offset is expected to be non-negative and smaller than the length of the polyline.
When the offset is negative, the function returns the starting end point of the polyline,
i.e. the first vertex in positive direction and the last vertex in the negative direction.
Similarly, when the offset is larger than the length of the polyline, then the function
returns the opposite end point of the polyline.</p>
<p>The distance between two consecutive vertices is calculated using the
/sdk-for-flutter-explore-core-geocoordinates-distanceto function. Therefore, it computes the distance (in meters) along
the great circle between the two vertices. Similarly, the full length of the polyline is the
sum of the distances between its vertices. The interpolation coordinates between two vertices
is calculated using the /sdk-for-flutter-explore-core-geocoordinates-interpolate function.</p>
<p>Note: the result may different from the analogue result from other matching components since
they may adapt the result to the length of the underlying object described by the polyline.</p>
<ul>
<li>
<p><code>offsetInMeters</code> The distance along the polyline in meters</p>
</li>
<li>
<p><code>direction</code> The direction in which the polyline is traversed.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-geocoordinates-class. The coordinates of the point at the given distance</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCoordinates coordinatesAtOffsetInMeters(double offsetInMeters, GeoPolylineDirection direction) =&gt; $prototype.coordinatesAtOffsetInMeters(this, offsetInMeters, direction);</code></pre>
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
<li>/sdk-for-flutter-explore-core-geopolyline-class</li>
<li class="self-crumb">coordinatesAtOffsetInMeters method</li>
</ol>
<h5>GeoPolyline class</h5>
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
