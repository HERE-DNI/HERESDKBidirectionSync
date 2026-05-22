---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-freeflowspeedtable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeFlowSpeedTable.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-class</li>
<li class="self-crumb">freeFlowSpeedTable property</li>
</ol>
<div class="self-name">freeFlowSpeedTable</div>
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
<div class="main-content" data-above-sidebar="routing/EmpiricalConsumptionModel-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>freeFlowSpeedTable property</h1></div>
<section class="multi-line-signature">
        
        Map&lt;<wbr/>int, double&gt;
freeFlowSpeedTable
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Free flow speed table describes energy consumption when traveling at constant speed.
It defines a function curve specifying consumption rate at a given free flow speed
on a flat stretch of road.
Map keys represent speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
At minimum, one key/value pair must be set. In this case the consumption value is
used for all possible speed keys.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;int, double&gt; freeFlowSpeedTable;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-class</li>
<li class="self-crumb">freeFlowSpeedTable property</li>
</ol>
<h5>EmpiricalConsumptionModel class</h5>
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
