---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateCatalog.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdater-class</li>
<li class="self-crumb">updateCatalog abstract method</li>
</ol>
<div class="self-name">updateCatalog</div>
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
<div class="main-content" data-above-sidebar="maploader/MapUpdater-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>updateCatalog abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-maploader-catalogupdatetask-class
updateCatalog(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class catalogInfo, </li>
<li>/sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request for each catalog to update map data to the latest available version.</p>
<p>This applies to all previously installed /sdk-for-flutter-navigate-maploader-region-class map data and any incomplete downloads in a pending state.</p>
<p>If no regions are downloaded, this method updates only the map version.
The map cache and persisted regions are always bound to the same map version.</p>
<p>If no updates are available, /sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback from
/sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo returns an empty list.
In this case, /sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete is called immediately.</p>
<p>To check for available updates, use /sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo to retrieve catalogs with newer versions.
Individual catalogs can then be updated using this method.
Ensure that the device has enough free disk space to perform a catalog update.
Information about the required disk space is available in /sdk-for-flutter-navigate-maploader-catalogupdateinfo-disksizeinbytes.</p>
<p>If there is not enough space to perform the catalog update with the default
/sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy, try using /sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy.
This option requires less space but follows a different strategy for handling errors during the map update.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated.
The index helps <code>OfflineSearchEngine</code> provide better search results.</p>
<p>Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p>
<ul>
<li>
<p><code>catalogInfo</code> catalog to update. CatalogUpdateInfo should be get from /sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-maploader-catalogupdatetask-class. A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CatalogUpdateTask updateCatalog(CatalogUpdateInfo catalogInfo, CatalogUpdateProgressListener callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-mapupdater-class</li>
<li class="self-crumb">updateCatalog abstract method</li>
</ol>
<h5>MapUpdater class</h5>
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
