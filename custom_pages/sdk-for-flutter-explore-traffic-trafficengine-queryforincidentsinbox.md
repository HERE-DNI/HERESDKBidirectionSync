---
title: "Implementation"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- queryForIncidentsInBox.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li><a href="../../traffic/TrafficEngine-class.html">/sdk-for-flutter-explore-traffic-trafficengine-class</a></li>
<li class="self-crumb">queryForIncidentsInBox abstract method</li>
</ol>
<div class="self-name">queryForIncidentsInBox</div>
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
<div class="main-content" data-above-sidebar="traffic/TrafficEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>queryForIncidentsInBox abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
queryForIncidentsInBox(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> boxArea, </li>
<li><a href="../../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a> queryOptions, </li>
<li><a href="../../traffic/TrafficIncidentsQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously queries for traffic incidents using a bounding box as a filter.</p>
<ul>
<li>
<p><code>boxArea</code> The bounding box area to search for traffic incidents.
The maximum width and height for a bounding box filter is 1 degree.</p>
</li>
<li>
<p><code>queryOptions</code> The options which are specific for incidents query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForIncidentsInBox(GeoBox boxArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li><a href="../../traffic/TrafficEngine-class.html">/sdk-for-flutter-explore-traffic-trafficengine-class</a></li>
<li class="self-crumb">queryForIncidentsInBox abstract method</li>
</ol>
<h5>TrafficEngine class</h5>
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
</HTMLBlock>
