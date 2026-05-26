---
title: "calculateTrafficOnRoute abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRoute.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">calculateTrafficOnRoute abstract method</li>
</ol>
<div class="self-name">calculateTrafficOnRoute</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateTrafficOnRoute abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-threading-taskhandle-class
calculateTrafficOnRoute(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-routing-route-class route, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li>/sdk-for-flutter-explore-routing-calculatetrafficonroutecallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates the traffic along a route starting from the index of the last
traveled route section and an offset (in meters) from the last visited position on the
section.</p>
<p>Call this when only the contained traffic information or the latest ETA duration
is needed. This can be called periodically to retrieve updated ETA values during navigation.</p>
<p><strong>Note:</strong> Calling this method will trigger a new "HERE Traffic" transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
<ul>
<li>
<p><code>route</code> A /sdk-for-flutter-explore-routing-route-class calculated using the online routing engine. Its
/sdk-for-flutter-explore-routing-routehandle-class and the original route calculation options will be used to
compute the traffic on the route. The original route remains untouched.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't
be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route traffic has been calculated.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateTrafficOnRoute(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateTrafficOnRouteCallback callback);</code></pre>
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
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">calculateTrafficOnRoute abstract method</li>
</ol>
<h5>RoutingEngine class</h5>
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
