---
title: "withVisibilityRange abstract method"
slug: "sdk-for-flutter-navigate-mapview-maplayerbuilder-withvisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withVisibilityRange.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maplayerbuilder-class</li>
<li class="self-crumb">withVisibilityRange abstract method</li>
</ol>
<div class="self-name">withVisibilityRange</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withVisibilityRange abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-maplayerbuilder-class
withVisibilityRange(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-class visibilityRange</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Configures the builder to set the layer visible in the given zoom levels range.</p>
<p>Values outside the map zoom level range (0, 24) will be ignored.
Providing the visibility range is optional. If not provided, the layer will be visible
on all zoom levels.</p>
<ul>
<li><code>visibilityRange</code> Visibility range which should be applied to the layer.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-maplayerbuilder-class. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerBuilder withVisibilityRange(MapLayerVisibilityRange visibilityRange);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maplayerbuilder-class</li>
<li class="self-crumb">withVisibilityRange abstract method</li>
</ol>
<h5>MapLayerBuilder class</h5>
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
