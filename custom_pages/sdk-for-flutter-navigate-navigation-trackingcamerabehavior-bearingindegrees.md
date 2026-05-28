---
title: "bearingInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-bearingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- bearingInDegrees.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class</li>
<li class="self-crumb">bearingInDegrees property</li>
</ol>
<div class="self-name">bearingInDegrees</div>
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
<div class="main-content" data-above-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>bearingInDegrees property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double?
bearingInDegrees
</section>
<section class="desc markdown">
<p>The camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the /sdk-for-flutter-navigate-core-location-class,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Gets the bearing in degrees.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get bearingInDegrees;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
bearingInDegrees=(<wbr/>double? value)
</section>
<section class="desc markdown">
<p>The camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the /sdk-for-flutter-navigate-core-location-class,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Sets the bearing in degrees.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set bearingInDegrees(double? value);</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class</li>
<li class="self-crumb">bearingInDegrees property</li>
</ol>
<h5>TrackingCameraBehavior class</h5>
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
