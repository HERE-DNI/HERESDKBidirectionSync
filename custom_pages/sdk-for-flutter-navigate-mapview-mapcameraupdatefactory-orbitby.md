---
title: "orbitBy static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-orbitby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- orbitBy.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">orbitBy static method</li>
</ol>
<div class="self-name">orbitBy</div>
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
<h1>orbitBy static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcameraupdate-class
orbitBy(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geoorientationupdate-class delta, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class origin</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.</p>
<p>If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.</p>
<p>Orientation elements that are not valid will be excluded from the update.
Resulting bearing values are wrapped around degrees range [0, 360].
Resulting tilt values are clamped inside degrees range [0, 180].
Resulting roll values are wrapped around degrees range [-180, 180].</p>
<ul>
<li>
<p><code>delta</code> Geodetic orientation delta update.</p>
</li>
<li>
<p><code>origin</code> Screen pixel origin of rotation.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate orbitBy(GeoOrientationUpdate delta, Point2D origin) =&gt; $prototype.orbitBy(delta, origin);</code></pre>
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
<li class="self-crumb">orbitBy static method</li>
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
