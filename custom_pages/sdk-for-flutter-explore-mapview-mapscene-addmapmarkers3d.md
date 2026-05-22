---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmapmarkers3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarkers3d.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">addMapMarkers3d abstract method</li>
</ol>
<div class="self-name">addMapMarkers3d</div>
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
<h1>addMapMarkers3d abstract method</h1></div>
<section class="multi-line-signature">
void
addMapMarkers3d(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmarker3d-class&gt; markers</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Adds multiple 3D map markers to this map scene.</p>
<p>Adding the same 3D marker instances multiple
times has no effect.</p>
<p><strong>Note:</strong>
Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D
markers (especially 500+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the /sdk-for-flutter-explore-mapview-mapscene-class class doc.</p>
<ul>
<li><code>markers</code> The list of 3D markers to be added to this map scene.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapMarkers3d(List&lt;MapMarker3D&gt; markers);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">addMapMarkers3d abstract method</li>
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



</div>
`
}</HTMLBlock>
