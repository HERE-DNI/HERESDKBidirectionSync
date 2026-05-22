---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDownloader-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapDownloader class</li>
</ol>
<div class="self-name">MapDownloader</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapDownloader-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapDownloader class abstract</h1></div>
<section class="desc markdown">
<p>A class for downloading and managing map data for various regions worldwide.</p>
<p>Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
search, routing, and other features without an active data connection.
Users can query available regions, download them to disk, or delete them.
An instance of this class can be created using /sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync.</p>
<p>The storage path for downloaded maps can be specified via /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.</p>
<p>To control the type of content included in a map download, use <code>LayerConfiguration</code>.
Once applied, it affects both the map cache and offline maps.
Satellite-based map schemes are not included in the downloaded region data.</p>
<p><strong>Note:</strong>
During turn-by-turn navigation,
while a map download or update is in progress, navigation may not function as expected,
and the app may be blocked until the operation is completed.
Ensure that all pending map operations are finished before starting navigation.
This applies only to <code>MapDownloader</code> and <code>MapUpdater</code>. <code>RoutePrefetcher</code> operations are not affected.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapDownloader">
/sdk-for-flutter-navigate-maploader-mapdownloader-mapdownloader()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-maploader-mapdownloader-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-mapdownloader-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="taskCount">
/sdk-for-flutter-navigate-maploader-mapdownloader-taskcount
↔ int
</dt>
<dd>
  The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="clearPersistentMapStorage">
/sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage(<wbr/>/sdk-for-flutter-navigate-maploader-sdkcachecallback callback)
    → void

</dt>
<dd>
  Performs an asynchronous operation to clear the persistent map storage from all data.
  

</dd>
<dt class="callable" id="deleteRegions">
/sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt; regions, /sdk-for-flutter-navigate-maploader-deletedregionscallback callback)
    → void

</dt>
<dd>
  Performs an asynchronous operation to delete map data for regions specified by a list of /sdk-for-flutter-navigate-maploader-regionid-class.
  

</dd>
<dt class="callable" id="downloadArea">
/sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea(<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class area, /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class statusListener)
    → /sdk-for-flutter-navigate-maploader-mapdownloadertask-class

</dt>
<dd>
  Performs an asynchronous request to download map data for area specified by a GeoPolygon.
  

</dd>
<dt class="callable" id="downloadRegions">
/sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt; regions, /sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class statusListener)
    → /sdk-for-flutter-navigate-maploader-mapdownloadertask-class

</dt>
<dd>
  Performs an asynchronous request to download map data for regions specified
by a list of /sdk-for-flutter-navigate-maploader-regionid-class instances.
  

</dd>
<dt class="callable" id="getDownloadableRegions">
/sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregions(<wbr/>/sdk-for-flutter-navigate-maploader-downloadableregionscallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to fetch a list of /sdk-for-flutter-navigate-maploader-region-class objects
for downloading map data in a separate request.
  

</dd>
<dt class="callable" id="getDownloadableRegionsWithLanguageCode">
/sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode(<wbr/>/sdk-for-flutter-navigate-core-languagecode languageCode, /sdk-for-flutter-navigate-maploader-downloadableregionscallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to fetch a list of /sdk-for-flutter-navigate-maploader-region-class objects with /sdk-for-flutter-navigate-maploader-region-name
in given <code>MapDownloader.getDownloadableRegionsWithLanguageCode.languageCode</code>, that can be used to download the actual map data in a separate request.
  

</dd>
<dt class="callable" id="getInitialPersistentMapStatus">
/sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus(<wbr/>)
    → /sdk-for-flutter-navigate-maploader-persistentmapstatus

</dt>
<dd>
  Gets the initial status of the already downloaded regions at start-up time of the app.
  

</dd>
<dt class="callable" id="getInstalledRegions">
/sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-installedregion-class&gt;

</dt>
<dd>
  Method to get a list of map regions that are currently installed on the device.
  

</dd>
<dt class="callable" id="getOfflineMapsStorageSizeInBytes">
/sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytes(<wbr/>)
    → int

</dt>
<dd>
  Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.
  

</dd>
<dt class="callable" id="getOfflineMapsStorageSizeInBytesAsync">
/sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync(<wbr/>/sdk-for-flutter-navigate-maploader-offlinestoragesizecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-mapdownloader-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="repairPersistentMap">
/sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap(<wbr/>/sdk-for-flutter-navigate-maploader-repairpersistentmapcallback callback)
    → void

</dt>
<dd>
  Tries to repair already downloaded regions that are in a corrupted state (see /sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus).
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-mapdownloader-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-maploader-mapdownloader-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromSdkEngineAsync">
/sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync(<wbr/>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback mapDownloaderConstructionCallback)
    → void

</dt>
<dd>
  Gets a single instance of this class per provided /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.
  

</dd>
</dl>
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
<li class="self-crumb">MapDownloader class</li>
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



</div>
`
}</HTMLBlock>
