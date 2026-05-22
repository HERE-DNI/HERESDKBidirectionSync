---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- retrieveCatalogsUpdateInfo.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdater-class</li>
<li class="self-crumb">retrieveCatalogsUpdateInfo abstract method</li>
</ol>
<div class="self-name">retrieveCatalogsUpdateInfo</div>
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
<h1>retrieveCatalogsUpdateInfo abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
retrieveCatalogsUpdateInfo(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Retrieves information of all catalogs that have newer version available.</p>
<p>This method can also be used to query
catalog information like HRN, current installed version and newer available version on server.
An empty list in /sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback represent no map updates.</p>
<ul>
<li><code>callback</code> Callback which receives the result on the main thread.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. A handle to cancel a pending operation.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle retrieveCatalogsUpdateInfo(CatalogsUpdateInfoCallback callback);</code></pre>
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
<li class="self-crumb">retrieveCatalogsUpdateInfo abstract method</li>
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
