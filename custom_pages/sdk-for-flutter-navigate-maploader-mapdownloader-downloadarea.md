---
title: "downloadArea abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadArea.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">downloadArea abstract method</li>
</ol>
<div class="self-name">downloadArea</div>
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
<h1>downloadArea abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-maploader-mapdownloadertask-class
downloadArea(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geopolygon-class area, </li>
<li>/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class statusListener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to download map data for area specified by a GeoPolygon.</p>
<p><code>MapDownloader.downloadArea.statusListener</code> is receiving notifications until /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called.
Returned /sdk-for-flutter-navigate-maploader-mapdownloadertask-class should be used to pause or resume started download, by invoking
<code>MapDownloaderTask.pauseWithCompaction</code> or /sdk-for-flutter-navigate-maploader-mapdownloadertask-resume.
Request can be cancelled by calling /sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel on returned /sdk-for-flutter-navigate-maploader-mapdownloadertask-class object, afterwards
/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called with error /sdk-for-flutter-navigate-maploader-maploadererror.</p>
<p>/sdk-for-flutter-navigate-maploader-mapdownloadertask-class remains operational until /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called.</p>
<p>Downloaded area will be associated to a unique id that will be reported via /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class.</p>
<p>Simultaneous download of the same region twice is not supported. When such condition occurs then
/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called with error /sdk-for-flutter-navigate-maploader-maploadererror
for a new request, while previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for area download, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<br/>
Note: If user try to re-download same GeoPolygon the status will be reported as per the
state of previous download operation.
<ul>
<li>
<p><code>area</code> Area to download.</p>
</li>
<li>
<p><code>statusListener</code> Notifies on the download progress.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-maploader-mapdownloadertask-class. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapDownloaderTask downloadArea(GeoPolygon area, DownloadRegionsStatusListener statusListener);</code></pre>
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
<li class="self-crumb">downloadArea abstract method</li>
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
