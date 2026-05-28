---
title: "getOfflineMapsStorageSizeInBytesAsync abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getOfflineMapsStorageSizeInBytesAsync.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getOfflineMapsStorageSizeInBytesAsync abstract method</li>
</ol>
<div class="self-name">getOfflineMapsStorageSizeInBytesAsync</div>
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
<h1>getOfflineMapsStorageSizeInBytesAsync abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
getOfflineMapsStorageSizeInBytesAsync(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-offlinestoragesizecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.</p>
<p>This includes also data that is currently being downloaded.</p>
<ul>
<li><code>callback</code> A callback which receives the value of offline map size or error on the main thread.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle getOfflineMapsStorageSizeInBytesAsync(OfflineStorageSizeCallback callback);</code></pre>
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
<li class="self-crumb">getOfflineMapsStorageSizeInBytesAsync abstract method</li>
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
