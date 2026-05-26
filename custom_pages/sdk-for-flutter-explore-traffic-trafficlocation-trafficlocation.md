---
title: "TrafficLocation constructor"
slug: "sdk-for-flutter-explore-traffic-trafficlocation-trafficlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficLocation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficlocation-class</li>
<li class="self-crumb">TrafficLocation constructor</li>
</ol>
<div class="self-name">TrafficLocation</div>
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
<div class="main-content" data-above-sidebar="traffic/TrafficLocation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TrafficLocation constructor</h1></div>
<section class="multi-line-signature">
TrafficLocation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-geopolyline-class polyline, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-explore-core-geopolyline-class&gt; additionalPolylines, </li>
<li>int lengthInMeters</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>polyline</code> The polyline representing the traffic entity shape.
The current field contains a continuous polyline with no gaps between geo-coordinates.
All others following the gap are present in the <code>additional_polylines</code> field.</li>
<li><code>additionalPolylines</code> List of polylines that were not included in continuous polyline.
Use this to fill any gaps in the continuous polyline.</li>
<li><code>lengthInMeters</code> The affected road length in meters.
The length can be 0 only if the incident supplier has provided incomplete data.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TrafficLocation(this.polyline, this.additionalPolylines, this.lengthInMeters)
    : description = "";</code></pre>
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
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficlocation-class</li>
<li class="self-crumb">TrafficLocation constructor</li>
</ol>
<h5>TrafficLocation class</h5>
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
