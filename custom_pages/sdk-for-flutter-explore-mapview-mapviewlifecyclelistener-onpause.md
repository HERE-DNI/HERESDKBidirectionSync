---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-onpause"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- onPause.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a></li>
<li class="self-crumb">onPause abstract method</li>
</ol>
<div class="self-name">onPause</div>
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
<div class="main-content" data-above-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onPause abstract method</h1></div>
<section class="multi-line-signature">
void
onPause(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Called when the map view to which this <a href="../../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a> is attached to gets paused
(usually when the app goes into background).</p>
<p>This should be used by components that
perform continuous updates to pause those updates until <a href="../../mapview/MapViewLifecycleListener/onResume.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-onresume</a>
is called.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onPause();</code></pre>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a></li>
<li class="self-crumb">onPause abstract method</li>
</ol>
<h5>MapViewLifecycleListener class</h5>
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
