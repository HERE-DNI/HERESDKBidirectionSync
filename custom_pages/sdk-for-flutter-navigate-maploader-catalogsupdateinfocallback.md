---
title: "CatalogsUpdateInfoCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogsUpdateInfoCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">CatalogsUpdateInfoCallback typedef</li>
</ol>
<div class="self-name">CatalogsUpdateInfoCallback</div>
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
<h1>CatalogsUpdateInfoCallback typedef</h1></div>
<section class="multi-line-signature">
CatalogsUpdateInfoCallback =
     void Function(/sdk-for-flutter-navigate-maploader-maploadererror? error, List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class&gt;? catalogs)
</section>
<section class="desc markdown">
<p>This method will be called on the main thread when /sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo has been completed.</p>
<p>The first parameter indicates an error in case of a failure. The second parameter contains the results.
Both parameters cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.
An empty <code>CatalogUpdateInfo</code> list  represent no map updates.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>catalogs</code> Represents a list of all catalogs that can be updated. It is <code>null</code> in case of an error.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CatalogsUpdateInfoCallback = void Function(MapLoaderError? error, List&lt;CatalogUpdateInfo&gt;? catalogs);</code></pre>
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
<li class="self-crumb">CatalogsUpdateInfoCallback typedef</li>
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
