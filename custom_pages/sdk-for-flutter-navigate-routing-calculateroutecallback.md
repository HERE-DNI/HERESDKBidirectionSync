---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-calculateroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CalculateRouteCallback.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">CalculateRouteCallback typedef</li>
</ol>
<div class="self-name">CalculateRouteCallback</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CalculateRouteCallback typedef</h1></div>
<section class="multi-line-signature">
CalculateRouteCallback =
     void Function(/sdk-for-flutter-navigate-routing-routingerror? routingError, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-route-class&gt;? routeList)
</section>
<section class="desc markdown">
<p>A function which is called by the RoutingEngine after route calculation has completed.</p>
<p>It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
The second argument is the calculated routes. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>routingError</code> The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>routeList</code> The calculated routes. It is <code>null</code> in case of an error.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CalculateRouteCallback = void Function(RoutingError? routingError, List&lt;Route&gt;? routeList);</code></pre>
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
<li class="self-crumb">CalculateRouteCallback typedef</li>
</ol>
<h5>routing library</h5>
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
