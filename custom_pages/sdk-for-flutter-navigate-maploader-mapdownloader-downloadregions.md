---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadRegions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">downloadRegions abstract method</li>
</ol>
<div class="self-name">downloadRegions</div>
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
<h1>downloadRegions abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-maploader-mapdownloadertask-class
downloadRegions(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt; regions, </li>
<li>/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class statusListener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to download map data for regions specified
by a list of /sdk-for-flutter-navigate-maploader-regionid-class instances.</p>
<p><code>MapDownloader.downloadRegions.statusListener</code> receives notifications until
/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called.
The returned /sdk-for-flutter-navigate-maploader-mapdownloadertask-class can be used to pause or resume the download
using <code>MapDownloaderTask.pauseWithCompaction</code> or /sdk-for-flutter-navigate-maploader-mapdownloadertask-resume.</p>
<p>To cancel the request, call /sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel on the returned
/sdk-for-flutter-navigate-maploader-mapdownloadertask-class object. After cancellation,
/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called
with the error /sdk-for-flutter-navigate-maploader-maploadererror.</p>
<p>/sdk-for-flutter-navigate-maploader-mapdownloadertask-class remains operational until /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete is called.</p>
<p>To get list of downloadable regions use /sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode API.</p>
<p>Simultaneous downloads of the same region are not supported.
If this occurs, /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete
is called with /sdk-for-flutter-navigate-maploader-maploadererror for the new request,
while the previous one continues uninterrupted.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been downloaded, the corresponding index will be created.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<p>To control list of map content features for region download, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<br/>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br/>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<ul>
<li>
<p><code>regions</code> List of regions to download. Can be fetched using /sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode API.</p>
</li>
<li>
<p><code>statusListener</code> Notifies on the download progress.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-maploader-mapdownloadertask-class. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapDownloaderTask downloadRegions(List&lt;RegionId&gt; regions, DownloadRegionsStatusListener statusListener);</code></pre>
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
<li class="self-crumb">downloadRegions abstract method</li>
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
