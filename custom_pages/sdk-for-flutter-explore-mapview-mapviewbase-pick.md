---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-pick"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- pick.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a></li>
<li class="self-crumb">pick abstract method</li>
</ol>
<div class="self-name">pick</div>
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
<div class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>pick abstract method</h1></div>
<section class="multi-line-signature">
void
pick(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapSceneMapPickFilter-class.html">/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class</a>? filter, </li>
<li><a href="../../core/Rectangle2D-class.html">/sdk-for-flutter-explore-core-rectangle2d-class</a> viewArea, </li>
<li><a href="../../mapview/MapViewBaseMapPickCallback.html">/sdk-for-flutter-explore-mapview-mapviewbasemappickcallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns all map content located inside the specified pick area.</p>
<p>Content to be picked is
specified by a pick content filter.
The pick area is defined by a rectangle in map view coordinates
in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner
of the map view.</p>
<ul>
<li>
<p><code>filter</code> Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
</li>
<li>
<p><code>viewArea</code> The rectangular pixel area of the view inside which map content will be picked.
View area is relative to the map view's origin at (0, 0) at the top-left corner
of the map view.</p>
</li>
<li>
<p><code>callback</code> Callback to call with the result. This will be called on a main thread when pick operation
completes.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void pick(MapSceneMapPickFilter? filter, Rectangle2D viewArea, MapViewBaseMapPickCallback callback);</code></pre>
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
<li><a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a></li>
<li class="self-crumb">pick abstract method</li>
</ol>
<h5>MapViewBase class</h5>
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
