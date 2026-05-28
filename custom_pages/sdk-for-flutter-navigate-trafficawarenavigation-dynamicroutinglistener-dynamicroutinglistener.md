---
title: "DynamicRoutingListener constructor"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-dynamicroutinglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class</li>
<li class="self-crumb">DynamicRoutingListener factory constructor</li>
</ol>
<div class="self-name">DynamicRoutingListener</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>DynamicRoutingListener constructor</h1></div>
<section class="multi-line-signature">
DynamicRoutingListener(<wbr/><ol class="parameter-list single-line"> <li>void onBetterRouteFoundLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-route-class, </li>
<li>int, </li>
<li>int</li>
</ol>), </li>
<li>void onRoutingErrorLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-routingerror</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented in order to
receive notifications about the new route via the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DynamicRoutingListener(
  void Function(Route, int, int) onBetterRouteFoundLambda,
  void Function(RoutingError) onRoutingErrorLambda,

) =&gt; DynamicRoutingListener$Lambdas(
  onBetterRouteFoundLambda,
  onRoutingErrorLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class</li>
<li class="self-crumb">DynamicRoutingListener factory constructor</li>
</ol>
<h5>DynamicRoutingListener class</h5>
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
