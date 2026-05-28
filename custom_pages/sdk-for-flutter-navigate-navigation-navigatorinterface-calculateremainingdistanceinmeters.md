---
title: "calculateRemainingDistanceInMeters abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateRemainingDistanceInMeters.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">calculateRemainingDistanceInMeters abstract method</li>
</ol>
<div class="self-name">calculateRemainingDistanceInMeters</div>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateRemainingDistanceInMeters abstract method</h1></div>
<section class="multi-line-signature">
int?
calculateRemainingDistanceInMeters(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>This method calculates the distance between the current position and given coordinates.</p>
<p>The coordinates must be on the polyline.</p>
<ul>
<li><code>coordinates</code> The geographic coordinates of the location.</li>
</ul>
<p>Returns <code>int?</code>. distance in meters or null if given coordinates are not on route or given
coordinates were already traversed.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? calculateRemainingDistanceInMeters(GeoCoordinates coordinates);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">calculateRemainingDistanceInMeters abstract method</li>
</ol>
<h5>NavigatorInterface class</h5>
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
