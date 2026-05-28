---
title: "update abstract method"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- update.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class</li>
<li class="self-crumb">update abstract method</li>
</ol>
<div class="self-name">update</div>
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
<h1>update abstract method</h1></div>
<section class="multi-line-signature">
void
update(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class mapMatchedLocation</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Updates the electronic horizon paths based on the provided map-matched location.</p>
<p>This method returns immediately and does not block.
When internal calculation is complete, callbacks are called on the main thread.
When multiple updates are triggered while processing is still running,
intermediate locations are skipped and only the last location is processed.</p>
<ul>
<li><code>mapMatchedLocation</code> The map-matched location that defines the current vehicle position on the road network.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void update(MapMatchedLocation mapMatchedLocation);</code></pre>
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
<li class="self-crumb">update abstract method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
