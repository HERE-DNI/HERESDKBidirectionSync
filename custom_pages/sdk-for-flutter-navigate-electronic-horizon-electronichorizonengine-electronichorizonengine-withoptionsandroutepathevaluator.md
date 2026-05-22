---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-electronichorizonengine-withoptionsandroutepathevaluator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class</li>
<li class="self-crumb">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator factory constructor</li>
</ol>
<div class="self-name">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator constructor</h1></div>
<section class="multi-line-signature">
ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, </li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class options, </li>
<li>/sdk-for-flutter-navigate-transport-transportmode transportMode, </li>
<li>/sdk-for-flutter-navigate-routing-route-class? route, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance of /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class.</p>
<ul>
<li>
<p><code>sdkEngine</code> The /sdk-for-flutter-navigate-core-engine-sdknativeengine-class instance that provides shared services, such as networking and map data.</p>
</li>
<li>
<p><code>options</code> The /sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class instance that configures how the electronic horizon is calculated, including look-ahead distances.</p>
</li>
<li>
<p><code>transportMode</code> The /sdk-for-flutter-navigate-transport-transportmode that is used when building the electronic horizon paths.</p>
</li>
<li>
<p><code>route</code> The /sdk-for-flutter-navigate-routing-route-class that improves the calculation of the most-preferred path (MPP).
If <code>null</code> is passed, the most-preferred path can deviate from the route.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-core-errors-instantiationexception-class. /sdk-for-flutter-navigate-core-errors-instantiationexception-class If the electronic horizon engine cannot be created.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator(SDKNativeEngine sdkEngine, ElectronicHorizonOptions options, TransportMode transportMode, Route? route) =&gt; $prototype.WithOptionsAndRoutePathEvaluator(sdkEngine, options, transportMode, route);</code></pre>
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class</li>
<li class="self-crumb">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator factory constructor</li>
</ol>
<h5>ElectronicHorizonEngine class</h5>
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
