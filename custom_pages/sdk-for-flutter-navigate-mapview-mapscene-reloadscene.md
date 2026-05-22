---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapscene-reloadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- reloadScene.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapscene-class</li>
<li class="self-crumb">reloadScene abstract method</li>
</ol>
<div class="self-name">reloadScene</div>
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
<h1>reloadScene abstract method</h1></div>
<section class="multi-line-signature">
void
reloadScene(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously reloads the current map scene from file.</p>
<p>This skips any cached data used internally and reloads the
scene including any changes made to the (custom) map styles in JSON.</p>
<p><code>MapFeature</code> settings will be preserved.</p>
<p>Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore,
calling this method may take slightly longer than calling one of the <code>loadScene(..)</code> overloads.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void reloadScene();</code></pre>
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
<li class="self-crumb">reloadScene abstract method</li>
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
