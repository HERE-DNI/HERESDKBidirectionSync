---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setLastKnownLocationPersistent.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">setLastKnownLocationPersistent method</li>
</ol>
<div class="self-name">setLastKnownLocationPersistent</div>
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
<h1>setLastKnownLocationPersistent method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
setLastKnownLocationPersistent(<wbr/><ol class="parameter-list single-line"> <li>bool persistent</li>
</ol>)

      <div class="features">override</div>
</section>
<section class="desc markdown">
<p>On Android devices this enables or disables saving of last known location so
that it persists across application sessions.
By default persistent saving across sessions is enabled.
Set <code>persistent</code> to true to enable last known location to persist across application sessions, or false to disable it.
When calling this method then /sdk-for-flutter-navigate-location-locationenginestatus is returned.</p>
<p>On iOS devices this is not supported and the value is stored, by default, across sessions.
When calling this method then /sdk-for-flutter-navigate-location-locationenginestatus is returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setLastKnownLocationPersistent(bool persistent)  {
  if (Platform.isAndroid) {
    return _location.setLastKnownLocationPersistent(persistent);
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
<li class="self-crumb">setLastKnownLocationPersistent method</li>
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
