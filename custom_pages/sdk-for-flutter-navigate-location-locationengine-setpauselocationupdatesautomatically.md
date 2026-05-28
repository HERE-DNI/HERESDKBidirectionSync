---
title: "setPauseLocationUpdatesAutomatically method"
slug: "sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPauseLocationUpdatesAutomatically.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">setPauseLocationUpdatesAutomatically method</li>
</ol>
<div class="self-name">setPauseLocationUpdatesAutomatically</div>
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
<h1>setPauseLocationUpdatesAutomatically method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
setPauseLocationUpdatesAutomatically(<wbr/><ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      <div class="features">override</div>
</section>
<section class="desc markdown">
<p>On iOS devices this controls automatic pausing of location updates e.g.
for improving device's battery life at times when
location data is unlikely to change.
By default automatic pausing of location updates is allowed.
Set <code>allowed</code> to true to allow automatic pausing of location updates, or false to disable them.
When calling this method then /sdk-for-flutter-navigate-location-locationenginestatus is returned.</p>
<p>On Android devices this is not supported and /sdk-for-flutter-navigate-location-locationenginestatus is returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed) {
  if (Platform.isIOS) {
    return _location.setPauseLocationUpdatesAutomatically(allowed);
  }
  return LocationEngineStatus.notSupported;
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
<li class="self-crumb">setPauseLocationUpdatesAutomatically method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
