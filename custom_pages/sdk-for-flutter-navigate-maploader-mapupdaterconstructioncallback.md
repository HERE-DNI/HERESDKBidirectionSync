---
title: "MapUpdaterConstructionCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdaterConstructionCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapUpdaterConstructionCallback typedef</li>
</ol>
<div class="self-name">MapUpdaterConstructionCallback</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapUpdaterConstructionCallback typedef</h1></div>
<section class="multi-line-signature">
MapUpdaterConstructionCallback =
     void Function(/sdk-for-flutter-navigate-maploader-mapupdater-class mapUpdater)
</section>
<section class="desc markdown">
<p>A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync has been completed.</p>
<p>Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p>
<ul>
<li><code>mapUpdater</code> Represents a constructed <code>MapUpdater</code> object.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapUpdaterConstructionCallback = void Function(MapUpdater mapUpdater);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapUpdaterConstructionCallback typedef</li>
</ol>
<h5>maploader library</h5>
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
