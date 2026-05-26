---
title: "setPrincipalPoint static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setprincipalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPrincipalPoint.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">setPrincipalPoint static method</li>
</ol>
<div class="self-name">setPrincipalPoint</div>
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
<h1>setPrincipalPoint static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapcameraupdate-class
setPrincipalPoint(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-point2d-class principalPoint</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to change the map camera's principal point (where the view vector intersects
the image plane - default is the center of the view).</p>
<p>Point values are in screen coordinates
and values that fall outside of the viewport, are clamped.
(0,0) is top left of the viewport.</p>
<ul>
<li><code>principalPoint</code> Principal point in absolute viewport pixel coordinates.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate setPrincipalPoint(Point2D principalPoint) =&gt; $prototype.setPrincipalPoint(principalPoint);</code></pre>
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
<li class="self-crumb">setPrincipalPoint static method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
