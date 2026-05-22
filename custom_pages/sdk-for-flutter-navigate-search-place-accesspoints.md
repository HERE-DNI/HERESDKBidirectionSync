---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-place-accesspoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- accessPoints.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-place-class</li>
<li class="self-crumb">accessPoints property</li>
</ol>
<div class="self-name">accessPoints</div>
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
<div class="main-content" data-above-sidebar="search/Place-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>accessPoints property</h1></div>
<section id="getter">
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;
accessPoints
</section>
<section class="desc markdown">
<p>The access points to the place, such as the points on a road or in a parking lot.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
Gets the access points to the place, such as the points on a road or in a parking lot.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;GeoCoordinates&gt; get accessPoints;</code></pre>
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-place-class</li>
<li class="self-crumb">accessPoints property</li>
</ol>
<h5>Place class</h5>
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
