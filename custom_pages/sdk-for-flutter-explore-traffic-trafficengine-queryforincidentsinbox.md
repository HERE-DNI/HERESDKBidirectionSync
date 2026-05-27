---
title: "queryForIncidentsInBox abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInBox.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficengine-class</li>
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
/sdk-for-flutter-explore-core-threading-taskhandle-class
queryForIncidentsInBox(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-geobox-class boxArea, </li>
<li>/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class queryOptions, </li>
<li>/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback callback</li>
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
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficengine-class</li>
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
`
}</HTMLBlock>
