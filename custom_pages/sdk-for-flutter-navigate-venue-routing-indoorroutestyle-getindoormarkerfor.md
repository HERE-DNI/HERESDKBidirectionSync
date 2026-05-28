---
title: "getIndoorMarkerFor abstract method"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutestyle-getindoormarkerfor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getIndoorMarkerFor.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-class</li>
<li class="self-crumb">getIndoorMarkerFor abstract method</li>
</ol>
<div class="self-name">getIndoorMarkerFor</div>
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
<div class="main-content" data-above-sidebar="venue.routing/IndoorRouteStyle-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getIndoorMarkerFor abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapmarker-class?
getIndoorMarkerFor(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-indoorlevelchangefeatures feature, </li>
<li>int deltaZ</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns a /sdk-for-flutter-navigate-mapview-mapmarker-class for a given indoor feature and
the number of levels to change.</p>
<p>By default, no map markers are provided.</p>
<ul>
<li>
<p><code>feature</code> An indoor feature.</p>
</li>
<li>
<p><code>deltaZ</code> A number of levels to change, positive for up, negative for down.
In the case of 0, the method returns an exit map marker.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-mapmarker-class. The result /sdk-for-flutter-navigate-mapview-mapmarker-class, if it was set.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMarker? getIndoorMarkerFor(IndoorLevelChangeFeatures feature, int deltaZ);</code></pre>
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
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-class</li>
<li class="self-crumb">getIndoorMarkerFor abstract method</li>
</ol>
<h5>IndoorRouteStyle class</h5>
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
