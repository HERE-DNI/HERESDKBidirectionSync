---
title: "onLocationUpdated abstract method"
slug: "sdk-for-flutter-navigate-core-locationlistener-onlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLocationUpdated.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
<li class="self-crumb">onLocationUpdated abstract method</li>
</ol>
<div class="self-name">onLocationUpdated</div>
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
<div class="main-content" data-above-sidebar="core/LocationListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onLocationUpdated abstract method</h1></div>
<section class="multi-line-signature">
void
onLocationUpdated(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-location-class location</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called each time a new location is available.</p>
<p>In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
object so that the HERE SDK can map-match the locations properly.
If the <code>Location.time</code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code>Location</code> object.
Invoked on the main thread.</p>
<ul>
<li><code>location</code> Current location.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onLocationUpdated(Location location);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
<li class="self-crumb">onLocationUpdated abstract method</li>
</ol>
<h5>LocationListener class</h5>
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
