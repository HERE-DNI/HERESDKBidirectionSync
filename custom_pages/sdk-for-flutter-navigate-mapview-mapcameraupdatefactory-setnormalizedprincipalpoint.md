---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setNormalizedPrincipalPoint.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">setNormalizedPrincipalPoint static method</li>
</ol>
<div class="self-name">setNormalizedPrincipalPoint</div>
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
<h1>setNormalizedPrincipalPoint static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
setNormalizedPrincipalPoint(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-anchor2d-class principalPoint</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to change the map camera's principal point (where the view vector
intersects the image plane - default is (0.5, 0.5)).</p>
<p>Point values are in normalized screen coordinates.</p>
<p>If the principalPoint is outside [0,1] interval, it is clamped.
(0,0) is top left of the viewport, (1,1) is bottom right.</p>
<ul>
<li><code>principalPoint</code> Principal point in normalized screen coordinates.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate setNormalizedPrincipalPoint(Anchor2D principalPoint) =&gt; $prototype.setNormalizedPrincipalPoint(principalPoint);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">setNormalizedPrincipalPoint static method</li>
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
