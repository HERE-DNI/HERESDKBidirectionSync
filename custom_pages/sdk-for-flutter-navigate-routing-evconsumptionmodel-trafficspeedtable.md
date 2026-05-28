---
title: "trafficSpeedTable property"
slug: "sdk-for-flutter-navigate-routing-evconsumptionmodel-trafficspeedtable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficSpeedTable.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-evconsumptionmodel-class</li>
<li class="self-crumb">trafficSpeedTable property</li>
</ol>
<div class="self-name">trafficSpeedTable</div>
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
<div class="main-content" data-above-sidebar="routing/EVConsumptionModel-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>trafficSpeedTable property</h1></div>
<section class="multi-line-signature">
        
        Map&lt;<wbr/>int, double&gt;
trafficSpeedTable
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Traffic speed table describes energy consumption when traveling under heavy traffic
conditions, i.e. when the vehicle is expected to often change the travel speed.
It defines a function curve specifying consumption rate at a given speed under traffic
conditions on a flat stretch of road.
Map keys represent traffic speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
If only one key/value pair is set, the consumption value is
used for all possible traffic speed keys.
If /sdk-for-flutter-navigate-routing-evconsumptionmodel-trafficspeedtable is empty then only
/sdk-for-flutter-navigate-routing-evconsumptionmodel-freeflowspeedtable is used for calculating speed-related
energy consumption.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;int, double&gt; trafficSpeedTable;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-evconsumptionmodel-class</li>
<li class="self-crumb">trafficSpeedTable property</li>
</ol>
<h5>EVConsumptionModel class</h5>
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
