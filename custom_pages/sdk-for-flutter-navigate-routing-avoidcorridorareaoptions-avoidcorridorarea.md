---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-avoidcorridorarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- avoidCorridorArea.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-class</li>
<li class="self-crumb">avoidCorridorArea property</li>
</ol>
<div class="self-name">avoidCorridorArea</div>
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
<div class="main-content" data-above-sidebar="routing/AvoidCorridorAreaOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>avoidCorridorArea property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-geocorridor-class
avoidCorridorArea
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Area of corridor shape which routes must not cross. Strictly enforced.
Violations are reported as /sdk-for-flutter-navigate-routing-sectionnoticecode.
<strong>Note:</strong>
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCorridor avoidCorridorArea;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-class</li>
<li class="self-crumb">avoidCorridorArea property</li>
</ol>
<h5>AvoidCorridorAreaOptions class</h5>
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
