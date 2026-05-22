---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- deleteRegions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">deleteRegions abstract method</li>
</ol>
<div class="self-name">deleteRegions</div>
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
<h1>deleteRegions abstract method</h1></div>
<section class="multi-line-signature">
void
deleteRegions(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt; regions, </li>
<li>/sdk-for-flutter-navigate-maploader-deletedregionscallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous operation to delete map data for regions specified by a list of /sdk-for-flutter-navigate-maploader-regionid-class.</p>
<p>Note: Deleting a region when there is a pending download returns error
/sdk-for-flutter-navigate-maploader-maploadererror. Also, deleting a region when there is an ongoing download returns
error /sdk-for-flutter-navigate-maploader-maploadererror.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been deleted, the index over remaining regions will be rebuilt,
so that entries related to deleted regions are removed.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<ul>
<li>
<p><code>regions</code> List of regions to be deleted.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result of deletion on the main thread.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void deleteRegions(List&lt;RegionId&gt; regions, DeletedRegionsCallback callback);</code></pre>
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
<li class="self-crumb">deleteRegions abstract method</li>
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



</div>
`
}</HTMLBlock>
