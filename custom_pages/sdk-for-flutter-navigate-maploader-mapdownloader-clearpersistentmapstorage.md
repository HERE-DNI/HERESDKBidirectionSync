---
title: "clearPersistentMapStorage abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- clearPersistentMapStorage.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">clearPersistentMapStorage abstract method</li>
</ol>
<div class="self-name">clearPersistentMapStorage</div>
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
<div class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>clearPersistentMapStorage abstract method</h1></div>
<section class="multi-line-signature">
void
clearPersistentMapStorage(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-sdkcachecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous operation to clear the persistent map storage from all data.</p>
<p>All downloaded regions will be removed.
Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.</p>
<p>Any previously built index will also be deleted.
See /sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions to learn more about index.</p>
<ul>
<li><code>callback</code> Callback which receives the result of clearing on the main thread.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void clearPersistentMapStorage(SDKCacheCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">clearPersistentMapStorage abstract method</li>
</ol>
<h5>MapDownloader class</h5>
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
