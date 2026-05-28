---
title: "repairPersistentMap abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- repairPersistentMap.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">repairPersistentMap abstract method</li>
</ol>
<div class="self-name">repairPersistentMap</div>
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
<h1>repairPersistentMap abstract method</h1></div>
<section class="multi-line-signature">
void
repairPersistentMap(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-repairpersistentmapcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Tries to repair already downloaded regions that are in a corrupted state (see /sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus).</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then index will be
rebuilt if existing index does not match with the installed map regions after this operation.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<ul>
<li><code>callback</code> A callback which receives the result of the repair operation on the main thread.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void repairPersistentMap(RepairPersistentMapCallback callback);</code></pre>
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
<li class="self-crumb">repairPersistentMap abstract method</li>
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
