---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapscene-loadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadScene.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapscene-class</li>
<li class="self-crumb">loadScene abstract method</li>
</ol>
<div class="self-name">loadScene</div>
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
<div class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>loadScene abstract method</h1></div>
<section class="multi-line-signature">
void
loadScene(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class options, </li>
<li>/sdk-for-flutter-navigate-mapview-mapsceneloadscenecallback? callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously loads a map scene using MapSceneLoadOptions.</p>
<p>This is an unified API that supports loading from either a map scheme or configuration file,
with optional feature and watermark configuration. It's more efficient to load the scene with
this function by specifying the list of enabled features and disabled features, compared to
loading the scene first and enabling or disabling map features in the scene loading callback
function.</p>
<p>Configuration defaults are used for features that are not part of the enabled features or
disabled features parameters. When a feature is in both the enabled and disabled lists,
the feature is considered as requested to be enabled. If the same feature is present multiple
times in the enabled list with different modes, then the feature is considered as requested
to be enabled, but with an unspecified mode (any of the many specified in the enabled list).</p>
<p>Any previous map scene config will be replaced. The callback is called on the main thread.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>options</code> Scene configuration options created using MapSceneLoadOptionsBuilder.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadScene(MapSceneLoadOptions options, MapSceneLoadSceneCallback? callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapscene-class</li>
<li class="self-crumb">loadScene abstract method</li>
</ol>
<h5>MapScene class</h5>
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
