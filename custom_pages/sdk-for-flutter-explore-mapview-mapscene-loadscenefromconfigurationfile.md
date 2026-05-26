---
title: "loadSceneFromConfigurationFile abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-loadscenefromconfigurationfile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadSceneFromConfigurationFile.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">loadSceneFromConfigurationFile abstract method</li>
</ol>
<div class="self-name">loadSceneFromConfigurationFile</div>
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
<h1>loadSceneFromConfigurationFile abstract method</h1></div>
<section class="multi-line-signature">
void
loadSceneFromConfigurationFile(<wbr/><ol class="parameter-list single-line"> <li>String configurationFile, </li>
<li>/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback? callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously loads a map scene described by a specified file in one of the supported formats.</p>
<p>Any previous map scene config will be replaced.</p>
<p>When loading the same file again, consider to call <code>reloadScene()</code> instead.</p>
<p>Map features enabled or disabled using /sdk-for-flutter-explore-mapview-mapscene-enablefeatures
and /sdk-for-flutter-explore-mapview-mapscene-disablefeatures will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
<ul>
<li>
<p><code>configurationFile</code> Map scheme configuration file. It must contain the whole scene configuration.
In case it contains references to other files, they have to be reachable under
the paths specified in the main configuration file.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadSceneFromConfigurationFile(String configurationFile, MapSceneLoadSceneCallback? callback);</code></pre>
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
<li class="self-crumb">loadSceneFromConfigurationFile abstract method</li>
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
