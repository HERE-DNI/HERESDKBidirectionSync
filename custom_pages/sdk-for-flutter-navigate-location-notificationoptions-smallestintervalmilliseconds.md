---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-notificationoptions-smallestintervalmilliseconds"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- smallestIntervalMilliseconds.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-notificationoptions-class</li>
<li class="self-crumb">smallestIntervalMilliseconds property</li>
</ol>
<div class="self-name">smallestIntervalMilliseconds</div>
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
<div class="main-content" data-above-sidebar="location/NotificationOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>smallestIntervalMilliseconds property</h1></div>
<section class="multi-line-signature">
        
        int
        smallestIntervalMilliseconds
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Smallest allowed interval for position updates in milliseconds.  It is
guaranteed that positions are not provided more often than this value.
Smallest interval could be used for throttling position updates, e.g.
when each position update triggers CPU intensive calculations in the
client application. This value is used as a minimum update interval
when requesting GNSS location updates from the operating system.
When hdEnabled is set to <code>true</code> in SatellitePositioningOptions, the
smallest_interval_milliseconds value has a limited range. The SDK will
adjust the value to allow location updates with a frequency of 1Hz to
10Hz (1000 ms to 100 ms, respectively).
Default interval is 900 milliseconds.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int smallestIntervalMilliseconds;</code></pre>
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
<li>/sdk-for-flutter-navigate-location-notificationoptions-class</li>
<li class="self-crumb">smallestIntervalMilliseconds property</li>
</ol>
<h5>NotificationOptions class</h5>
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
