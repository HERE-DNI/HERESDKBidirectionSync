---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtArea.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">lookAtArea static method</li>
</ol>
<div class="self-name">lookAtArea</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lookAtArea static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapcameraupdate-class
lookAtArea(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-geobox-class target</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to look at the given geo-box,
preserving current orientation and zooming at the center of viewport.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li><code>target</code> Geodetic box that should be visible inside the viewport rectangle.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtArea(GeoBox target) =&gt; $prototype.lookAtArea(target);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">lookAtArea static method</li>
</ol>
<h5>MapCameraUpdateFactory class</h5>
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
