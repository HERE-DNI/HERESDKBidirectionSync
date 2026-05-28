---
title: "MapUpdater class abstract"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdater-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/MapUpdater-class.html#constructors">Constructors</a></li>
<li><a href="maploader/MapUpdater/MapUpdater.html">MapUpdater</a></li>
<li class="section-title">
<a href="maploader/MapUpdater-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="maploader/MapUpdater/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="maploader/MapUpdater/runtimeType.html">runtimeType</a></li>
<li><a href="maploader/MapUpdater/taskCount.html">taskCount</a></li>
<li><a href="maploader/MapUpdater/updateStatistics.html">updateStatistics</a></li>
<li class="section-title"><a href="maploader/MapUpdater-class.html#instance-methods">Methods</a></li>
<li><a href="maploader/MapUpdater/getCurrentMapVersion.html">getCurrentMapVersion</a></li>
<li class="inherited"><a href="maploader/MapUpdater/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="maploader/MapUpdater/retrieveCatalogsUpdateInfo.html">retrieveCatalogsUpdateInfo</a></li>
<li><a href="maploader/MapUpdater/setVersionCommitPolicy.html">setVersionCommitPolicy</a></li>
<li class="inherited"><a href="maploader/MapUpdater/toString.html">toString</a></li>
<li><a href="maploader/MapUpdater/updateCatalog.html">updateCatalog</a></li>
<li class="section-title inherited"><a href="maploader/MapUpdater-class.html#operators">Operators</a></li>
<li class="inherited"><a href="maploader/MapUpdater/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="maploader/MapUpdater-class.html#static-methods">Static methods</a></li>
<li><a href="maploader/MapUpdater/fromSdkEngineAsync.html">fromSdkEngineAsync</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapUpdater class</li>
</ol>
<div class="self-name">MapUpdater</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapUpdater-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapUpdater class abstract</h1></div>
<section class="desc markdown">
<p>A class for updating regions previously downloaded using the /sdk-for-flutter-navigate-maploader-mapdownloader-class.</p>
<p>First, updates for the regions are downloaded. Once the download is complete, the update process begins,
installing the new content.
It is recommended to regularly call /sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo to check for available updates
for any downloaded regions.</p>
<p>If updates are available, regions can be updated asynchronously using /sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog.
The /sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class provides update progress for each region.</p>
<p>Incremental map updates are supported, by default: Instead of downloading an entire region,
only the parts that have changed will be installed. This results in a faster update process.
MapUpdater also aligns previously downloaded content with <code>LayerConfiguration</code> changes made via <code>SDKOptions</code>.</p>
<p>Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started
with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.</p>
<p>In case of an error, the previous map data remains available for use. It is only replaced
after new map data has been successfully downloaded. Regions that fail to update
must be retried in a new call. Paused updates can be resumed later.</p>
<p>During the update process, /sdk-for-flutter-navigate-maploader-mapupdater-class internally retries failed downloads
until a timeout occurs. If this happens, it is reported via /sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class.</p>
<p>If the user cancels the update process during the update phase, it is ignored.
The update phase begins after all content has been downloaded, then the HERE SDK installs
and replaces the existing regions. Cancellation is only possible during the download phase,
and a successful cancellation is indicated via /sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete.</p>
<p>Note that a /sdk-for-flutter-navigate-maploader-maploadererror occurs when the /sdk-for-flutter-navigate-maploader-mapdownloader-class is used in parallel.
In general, background updates are not supported explicitly, as the OS can abort background processes.
In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
in progress and it will be indicated by a /sdk-for-flutter-navigate-maploader-maploadererror.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapUpdater">
/sdk-for-flutter-navigate-maploader-mapupdater-mapupdater()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-maploader-mapupdater-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-mapupdater-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="taskCount">
/sdk-for-flutter-navigate-maploader-mapupdater-taskcount
↔ int
</dt>
<dd>
  The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="updateStatistics">
/sdk-for-flutter-navigate-maploader-mapupdater-updatestatistics
→ /sdk-for-flutter-navigate-maploader-updatestatistics-class
</dt>
<dd>
  Map update statistics for the current application session.
In the event of binary updates, patches are downloaded and applied. This
property helps to  determine the success or failure rate of applied patches.
Map update statistics for the ongoing session of the current application.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getCurrentMapVersion">
/sdk-for-flutter-navigate-maploader-mapupdater-getcurrentmapversion(<wbr/>)
    → /sdk-for-flutter-navigate-maploader-mapversionhandle-class

</dt>
<dd>
  Returns a handle that contains the map version of the already downloaded and installed regions.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-mapupdater-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="retrieveCatalogsUpdateInfo">
/sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo(<wbr/>/sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Retrieves information of all catalogs that have newer version available.
  

</dd>
<dt class="callable" id="setVersionCommitPolicy">
/sdk-for-flutter-navigate-maploader-mapupdater-setversioncommitpolicy(<wbr/>/sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy versionCommitPolicy)
    → void

</dt>
<dd>
  Sets the map update version policy.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-mapupdater-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="updateCatalog">
/sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog(<wbr/>/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class catalogInfo, /sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class callback)
    → /sdk-for-flutter-navigate-maploader-catalogupdatetask-class

</dt>
<dd>
  Performs an asynchronous request for each catalog to update map data to the latest available version.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-maploader-mapupdater-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync(<wbr/>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback mapUpdaterConstructionCallback)
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
<li class="self-crumb">MapUpdater class</li>
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
