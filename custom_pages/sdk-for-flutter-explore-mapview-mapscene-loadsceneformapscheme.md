---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadSceneForMapScheme.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">loadSceneForMapScheme abstract method</li>
</ol>
<div class="self-name">loadSceneForMapScheme</div>
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
<h1>loadSceneForMapScheme abstract method</h1></div>
<section class="multi-line-signature">
void
loadSceneForMapScheme(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-mapscheme mapScheme, </li>
<li>/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback? callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously loads a map scene described by a specified map scheme.</p>
<p>Any previous map scene config will be replaced. The loaded scene is cached and so any changes
made to the scene files on disk might not get reflected on a successive call to this function.
Instead the reloadScene API can handle such use-cases to force-update the scene.</p>
<p>Map features enabled or disabled using /sdk-for-flutter-explore-mapview-mapscene-enablefeatures
and /sdk-for-flutter-explore-mapview-mapscene-disablefeatures will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
<ul>
<li>
<p><code>mapScheme</code> Map scheme.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadSceneForMapScheme(MapScheme mapScheme, MapSceneLoadSceneCallback? callback);</code></pre>
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
<li class="self-crumb">loadSceneForMapScheme abstract method</li>
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
