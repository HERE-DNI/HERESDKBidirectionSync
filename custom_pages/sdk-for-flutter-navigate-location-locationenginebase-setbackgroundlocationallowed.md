---
title: "setBackgroundLocationAllowed abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationAllowed.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">setBackgroundLocationAllowed abstract method</li>
</ol>
<div class="self-name">setBackgroundLocationAllowed</div>
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
<h1>setBackgroundLocationAllowed abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
setBackgroundLocationAllowed(<wbr/><ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Enables or disables background location updates for an application.</p>
<p>Defaults to <code>false</code>.</p>
<ul>
<li><code>allowed</code> Set to <code>true</code> to allow background location updates, or <code>false</code> to disable them.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-location-locationenginestatus. /sdk-for-flutter-navigate-location-locationenginestatus if call succeeds. /sdk-for-flutter-navigate-location-locationenginestatus if the application
does not have background location capabilities enabled.
/sdk-for-flutter-navigate-location-locationenginestatus on platforms which do not support controlling of background location modes.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setBackgroundLocationAllowed(bool allowed);</code></pre>
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
<li class="self-crumb">setBackgroundLocationAllowed abstract method</li>
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
