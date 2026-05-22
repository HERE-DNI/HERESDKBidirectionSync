---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-isolineroutingengine-calculateisoline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateIsoline.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-isolineroutingengine-class</li>
<li class="self-crumb">calculateIsoline abstract method</li>
</ol>
<div class="self-name">calculateIsoline</div>
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
<div class="main-content" data-above-sidebar="routing/IsolineRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateIsoline abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
calculateIsoline(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-waypoint-class center, </li>
<li>/sdk-for-flutter-navigate-routing-isolineoptions-class isolineOptions, </li>
<li>/sdk-for-flutter-navigate-routing-calculateisolinecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates isolines to indicate the reachable area from a center point.</p>
<p>This finds all destinations that can be reached in a specific amount of time,
a maximum travel distance, or even the charge level available in an electric vehicle.
The result is a polygon area where each point is reachable within the provided limit.</p>
<ul>
<li>
<p><code>center</code> Center point from which isolines are calculated.
At minimum, the waypoint must contain the coordinates as point of origin.</p>
</li>
<li>
<p><code>isolineOptions</code> Options for isoline calculation.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after isoline calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateIsoline(Waypoint center, IsolineOptions isolineOptions, CalculateIsolineCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-isolineroutingengine-class</li>
<li class="self-crumb">calculateIsoline abstract method</li>
</ol>
<h5>IsolineRoutingEngine class</h5>
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
