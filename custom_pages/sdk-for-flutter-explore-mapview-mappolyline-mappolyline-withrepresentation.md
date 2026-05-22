---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolyline-mappolyline-withrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolyline.withRepresentation.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolyline-class</li>
<li class="self-crumb">MapPolyline.withRepresentation factory constructor</li>
</ol>
<div class="self-name">MapPolyline.withRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolyline.withRepresentation constructor</h1></div>
<section class="multi-line-signature">
MapPolyline.withRepresentation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-geopolyline-class geometry, </li>
<li>/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class representation</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new <code>MapPolyline</code> instance with a specified visual representation.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
<p>After creating a <code>MapPolyline</code> with this representation, the deprecated <code>MapPolyline</code>
properties do not work and any change to them will be ignored. Any modifications to polyline's
appearance must be done with /sdk-for-flutter-explore-mapview-mappolyline-setrepresentation.</p>
<ul>
<li>
<p><code>geometry</code> The list of vertices representing the polyline.</p>
</li>
<li>
<p><code>representation</code> The styling properties of the polyline.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolyline.withRepresentation(GeoPolyline geometry, MapPolylineRepresentation representation) =&gt; $prototype.withRepresentation(geometry, representation);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mappolyline-class</li>
<li class="self-crumb">MapPolyline.withRepresentation factory constructor</li>
</ol>
<h5>MapPolyline class</h5>
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
