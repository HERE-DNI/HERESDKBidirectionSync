---
title: "lights property"
slug: "sdk-for-flutter-explore-mapview-mapscene-lights"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lights.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">lights property</li>
</ol>
<div class="self-name">lights</div>
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
<h1>lights property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapscenelights-class
lights
</section>
<section class="desc markdown">
<p>Controls lights present in the scene.
Provides access to a MapSceneLights instance that controls the lights in the scene.</p>
<p>The behavior of the returned MapSceneLights instance depends on the state of the scene:</p>
<ul>
<li>If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.</li>
<li>If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.</li>
</ul>
<p>Scene Change Behavior:</p>
<ul>
<li>If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.</li>
<li>Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.</li>
</ul>
<p>Error Handling:</p>
<ul>
<li>If the scene is loaded and the loaded scene does not utilize or specify light settings:
<ul>
<li>If the lights are not present, the error callback may return a NO_LIGHTS state.
Gets a MapSceneLights instance that controls lights present in the scene.</li>
</ul>
</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapSceneLights get lights;</code></pre>
</section>
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
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">lights property</li>
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
</div></div>
</div>
`
}</HTMLBlock>
