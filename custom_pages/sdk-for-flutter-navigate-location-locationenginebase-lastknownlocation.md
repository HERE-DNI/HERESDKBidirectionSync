---
title: "lastKnownLocation property"
slug: "sdk-for-flutter-navigate-location-locationenginebase-lastknownlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastKnownLocation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">lastKnownLocation property</li>
</ol>
<div class="self-name">lastKnownLocation</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lastKnownLocation property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-location-class?
lastKnownLocation
</section>
<section class="desc markdown">
<p>The last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
This property can be obtained without starting the <code>LocationEngine</code>. However, the initial value might be <code>null</code>
if no location has ever been obtained by the <code>LocationEngine</code>.
The time attribute of the <code>Location</code> object indicates when the last location was obtained.
Note: In order to receive continuous location updates, add a <code>LocationListener</code>.
Gets the last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Location? get lastKnownLocation;</code></pre>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">lastKnownLocation property</li>
</ol>
<h5>LocationEngineBase class</h5>
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
