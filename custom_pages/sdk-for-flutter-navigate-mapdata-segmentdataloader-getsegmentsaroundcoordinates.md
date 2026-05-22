---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSegmentsAroundCoordinates.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdataloader-class</li>
<li class="self-crumb">getSegmentsAroundCoordinates abstract method</li>
</ol>
<div class="self-name">getSegmentsAroundCoordinates</div>
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
<div class="main-content" data-above-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getSegmentsAroundCoordinates abstract method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-ocmsegmentid-class&gt;
getSegmentsAroundCoordinates(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, </li>
<li>double radiusInMeters</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Loads the segments around a certain coordinates.</p>
<p>Returns an empty list in case no segments could be found around the coordinates.</p>
<ul>
<li>
<p><code>coordinates</code> The location to explore</p>
</li>
<li>
<p><code>radiusInMeters</code> The radius of the search. Only values between 1m and 5000m are accepted.</p>
</li>
</ul>
<p>Returns <code>List&lt;OCMSegmentId&gt;</code>. The list of segments around the given position.</p>
<p>The segments are sorted by distance
from the point.
Throws if it's not possible to return list of a list of segments.</p>
<p>Throws /sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class. Specifies reason, why list of a list of segments is not returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;OCMSegmentId&gt; getSegmentsAroundCoordinates(GeoCoordinates coordinates, double radiusInMeters);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdataloader-class</li>
<li class="self-crumb">getSegmentsAroundCoordinates abstract method</li>
</ol>
<h5>SegmentDataLoader class</h5>
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
