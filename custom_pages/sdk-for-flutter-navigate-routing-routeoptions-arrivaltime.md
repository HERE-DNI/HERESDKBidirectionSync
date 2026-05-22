---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-routeoptions-arrivaltime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- arrivalTime.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routeoptions-class</li>
<li class="self-crumb">arrivalTime property</li>
</ol>
<div class="self-name">arrivalTime</div>
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
<div class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>arrivalTime property</h1></div>
<section class="multi-line-signature">
        
        DateTime?
        arrivalTime
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per /sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both /sdk-for-flutter-navigate-routing-routeoptions-departuretime and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DateTime? arrivalTime;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routeoptions-class</li>
<li class="self-crumb">arrivalTime property</li>
</ol>
<h5>RouteOptions class</h5>
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
