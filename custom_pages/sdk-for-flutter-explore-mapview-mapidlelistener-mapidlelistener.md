---
title: "MapIdleListener constructor"
slug: "sdk-for-flutter-explore-mapview-mapidlelistener-mapidlelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapIdleListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapidlelistener-class</li>
<li class="self-crumb">MapIdleListener factory constructor</li>
</ol>
<div class="self-name">MapIdleListener</div>
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
<div class="main-content" data-above-sidebar="mapview/MapIdleListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapIdleListener constructor</h1></div>
<section class="multi-line-signature">
MapIdleListener(<wbr/><ol class="parameter-list single-line"> <li>void onMapBusyLambda(), </li>
<li>void onMapIdleLambda()</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Used to detect when the map becomes idle or busy.</p>
<p>Map is considered busy when its state changes (for example as a result of camera manipulation)
and/or when it requires a redraw (for example, as a result of map data being downloaded).</p>
<p>Map is considered idle when current state is fully rendered and no further
redraws are necessary.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapIdleListener(
  void Function() onMapBusyLambda,
  void Function() onMapIdleLambda,

) =&gt; MapIdleListener$Lambdas(
  onMapBusyLambda,
  onMapIdleLambda,

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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapidlelistener-class</li>
<li class="self-crumb">MapIdleListener factory constructor</li>
</ol>
<h5>MapIdleListener class</h5>
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
