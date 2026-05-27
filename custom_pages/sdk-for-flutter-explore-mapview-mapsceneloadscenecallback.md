---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapsceneloadscenecallback"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapSceneLoadSceneCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapSceneLoadSceneCallback typedef</li>
</ol>
<div class="self-name">MapSceneLoadSceneCallback</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapSceneLoadSceneCallback typedef</h1></div>
<section class="multi-line-signature">
MapSceneLoadSceneCallback =
     void Function(<a href="../mapview/MapError.html">/sdk-for-flutter-explore-mapview-maperror</a>? loadSceneError)
</section>
<section class="desc markdown">
<p>Called on the main thread after <code>loadScene()</code> method finishes loading
the scene.</p>
<ul>
<li><code>loadSceneError</code> The load scene error</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapSceneLoadSceneCallback = void Function(MapError? loadSceneError);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapSceneLoadSceneCallback typedef</li>
</ol>
<h5>mapview library</h5>
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
