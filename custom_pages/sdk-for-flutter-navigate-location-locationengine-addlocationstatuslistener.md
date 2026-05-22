---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationengine-addlocationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addLocationStatusListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">addLocationStatusListener method</li>
</ol>
<div class="self-name">addLocationStatusListener</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>addLocationStatusListener method</h1></div>
<section class="multi-line-signature">
void
addLocationStatusListener(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationstatuslistener-class listener</li>
</ol>)

      <div class="features">override</div>
</section>
<section class="desc markdown">
<p>Adds a /sdk-for-flutter-navigate-location-locationstatuslistener-class to the engine to get notified when there is a an important status change.
Supports more than one listener, instance is added only once.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addLocationStatusListener(LocationStatusListener listener) {
  if (!_locationStatusListeners.containsKey(listener)) {
    _locationStatusListeners[listener] = LocationStatusListenerBridge(listener);
  }
  _location.addLocationStatusListener(_locationStatusListeners[listener]!);
}</code></pre>
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
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">addLocationStatusListener method</li>
</ol>
<h5>LocationEngine class</h5>
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
