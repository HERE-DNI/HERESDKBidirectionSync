---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-segmentreference-segmentreference"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SegmentReference.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/SegmentReference-class.html">/sdk-for-flutter-explore-routing-segmentreference-class</a></li>
<li class="self-crumb">SegmentReference constructor</li>
</ol>
<div class="self-name">SegmentReference</div>
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
<div class="main-content" data-above-sidebar="routing/SegmentReference-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SegmentReference constructor</h1></div>
<section class="multi-line-signature">
SegmentReference(<wbr/>[<ol class="parameter-list"> <li>String segmentId = "", </li>
<li><a href="../../routing/TravelDirection.html">/sdk-for-flutter-explore-routing-traveldirection</a> travelDirection = TravelDirection.bidirectional, </li>
<li>double offsetStart = 0.0, </li>
<li>double offsetEnd = 1.0, </li>
<li>int tilePartitionId = 0, </li>
<li>int? localId = 0, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>segmentId</code> Topology segment id representing a unique identifier within the HERE platform catalogs.</li>
<li><code>travelDirection</code> Travel direction of the segment.</li>
<li><code>offsetStart</code> The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</li>
<li><code>offsetEnd</code> The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</li>
<li><code>tilePartitionId</code> HERE tile partition id (Morton-encoding + level indicator) of the segment.
As in HERE Map Content.</li>
<li><code>localId</code> Local ID of the segment inside the OCM tile.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentReference([String segmentId = "", TravelDirection travelDirection = TravelDirection.bidirectional, double offsetStart = 0.0, double offsetEnd = 1.0, int tilePartitionId = 0, int? localId = 0])
  : segmentId = segmentId, travelDirection = travelDirection, offsetStart = offsetStart, offsetEnd = offsetEnd, tilePartitionId = tilePartitionId, localId = localId;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/SegmentReference-class.html">/sdk-for-flutter-explore-routing-segmentreference-class</a></li>
<li class="self-crumb">SegmentReference constructor</li>
</ol>
<h5>SegmentReference class</h5>
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
</HTMLBlock>
