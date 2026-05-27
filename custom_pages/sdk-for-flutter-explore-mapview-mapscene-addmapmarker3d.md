---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmapmarker3d"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- addMapMarker3d.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapScene-class.html">/sdk-for-flutter-explore-mapview-mapscene-class</a></li>
<li class="self-crumb">addMapMarker3d abstract method</li>
</ol>
<div class="self-name">addMapMarker3d</div>
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
<div class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>addMapMarker3d abstract method</h1></div>
<section class="multi-line-signature">
void
addMapMarker3d(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a> marker</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Adds a 3D map marker to this map scene.</p>
<p>Does nothing if the marker instance was already added to the scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarker3D API to add a very large number of 3D
markers (especially 500+ also depending on the complexity of the 3D object) is not
recommended. Adding this many 3D markers has a negative impact on the performance leading to
stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="../../mapview/MapScene-class.html">/sdk-for-flutter-explore-mapview-mapscene-class</a> class doc.</p>
<ul>
<li><code>marker</code> The marker to be added to this map scene.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapMarker3d(MapMarker3D marker);</code></pre>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapScene-class.html">/sdk-for-flutter-explore-mapview-mapscene-class</a></li>
<li class="self-crumb">addMapMarker3d abstract method</li>
</ol>
<h5>MapScene class</h5>
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
