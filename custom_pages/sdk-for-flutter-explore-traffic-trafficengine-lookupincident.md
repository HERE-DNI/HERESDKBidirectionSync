---
title: "Untitled"
slug: "sdk-for-flutter-explore-traffic-trafficengine-lookupincident"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookupIncident.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficengine-class</li>
<li class="self-crumb">lookupIncident abstract method</li>
</ol>
<div class="self-name">lookupIncident</div>
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
<h1>lookupIncident abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-threading-taskhandle-class
lookupIncident(<wbr/><ol class="parameter-list single-line"> <li>String originalId, </li>
<li>/sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class lookupOptions, </li>
<li>/sdk-for-flutter-explore-traffic-trafficincidentlookupcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously queries for traffic incident by the original id.</p>
<p>See /sdk-for-flutter-explore-traffic-trafficincident-originalid for more information.</p>
<ul>
<li>
<p><code>originalId</code> The requested incident original id.</p>
</li>
<li>
<p><code>lookupOptions</code> The options which are specific for the incident lookup query.</p>
</li>
<li>
<p><code>callback</code> The callback object that will be invoked after the incident lookup query.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle lookupIncident(String originalId, TrafficIncidentLookupOptions lookupOptions, TrafficIncidentLookupCallback callback);</code></pre>
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
<li class="self-crumb">lookupIncident abstract method</li>
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



</div>
`
}</HTMLBlock>
