---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setpauselocationupdatesautomatically"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPauseLocationUpdatesAutomatically.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">setPauseLocationUpdatesAutomatically abstract method</li>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setPauseLocationUpdatesAutomatically abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
setPauseLocationUpdatesAutomatically(<wbr/><ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Controls automatic pausing of location updates e.g.</p>
<p>for improving device's battery life at times when
location data is unlikely to change. By default automatic pausing of location updates is allowed.</p>
<ul>
<li><code>allowed</code> Set to <code>true</code> to allow automatic pausing of location updates, or <code>false</code> to disable them.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-location-locationenginestatus. /sdk-for-flutter-navigate-location-locationenginestatus if call succeeds. /sdk-for-flutter-navigate-location-locationenginestatus on platforms
which do not support automatic pausing of location updates.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed);</code></pre>
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
<li class="self-crumb">setPauseLocationUpdatesAutomatically abstract method</li>
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



</div>
`
}</HTMLBlock>
