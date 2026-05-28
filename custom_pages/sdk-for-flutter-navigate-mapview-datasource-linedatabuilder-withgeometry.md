---
title: "withGeometry abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-withgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withGeometry.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class</li>
<li class="self-crumb">withGeometry abstract method</li>
</ol>
<div class="self-name">withGeometry</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/LineDataBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withGeometry abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class
withGeometry(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geopolyline-class geometry</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Configures the builder with geometry for line to be created.</p>
<ul>
<li><code>geometry</code> Geometry of the polyline. Each vertex defines two line segments: one
with a previous vertex and one with a next vertex. First and last vertices don't have
resp. previous and next vertices and thus belong to single line segments.
Consecutive duplicate vertices are ignored.
Altitude of polyline vertices is ignored.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class. The builder.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LineDataBuilder withGeometry(GeoPolyline geometry);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class</li>
<li class="self-crumb">withGeometry abstract method</li>
</ol>
<h5>LineDataBuilder class</h5>
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
