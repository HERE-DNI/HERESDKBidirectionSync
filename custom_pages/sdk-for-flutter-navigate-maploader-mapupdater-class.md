---
title: "MapUpdater class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdater-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapUpdater-class-sidebar.html">

<div>

# <span class="kind-class">MapUpdater</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A class for updating regions previously downloaded using the <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.

First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> to check for available updates for any downloaded regions.

If updates are available, regions can be updated asynchronously using <a href="sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog">MapUpdater.updateCatalog</a>. The <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class">MapUpdateProgressListener</a> provides update progress for each region.

Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with `LayerConfiguration` changes made via `SDKOptions`.

Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.

In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later.

During the update process, <a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a> internally retries failed downloads until a timeout occurs. If this happens, it is reported via <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class">MapUpdateProgressListener</a>.

If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete">MapUpdateProgressListener.onComplete</a>.

Note that a <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notReady</a> occurs when the <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a> is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-mapupdater">MapUpdater</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-taskcount">taskCount</a></span> <span class="signature">↔ int</span>  
The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-updatestatistics">updateStatistics</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-maploader-updatestatistics-class">UpdateStatistics</a></span>  
Map update statistics for the current application session. In the event of binary updates, patches are downloaded and applied. This property helps to determine the success or failure rate of applied patches. Map update statistics for the ongoing session of the current application.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-getcurrentmapversion">getCurrentMapVersion</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-mapversionhandle-class">MapVersionHandle</a></span> </span>  
Returns a handle that contains the map version of the already downloaded and installed regions.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">retrieveCatalogsUpdateInfo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-retrieveCatalogsUpdateInfo-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Retrieves information of all catalogs that have newer version available.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-setversioncommitpolicy">setVersionCommitPolicy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setVersionCommitPolicy-param-versionCommitPolicy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></span> <span class="parameter-name">versionCommitPolicy</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the map update version policy.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog">updateCatalog</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateCatalog-param-catalogInfo" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a></span> <span class="parameter-name">catalogInfo</span>, </span><span id="sdk-for-flutter-navigate-updateCatalog-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class">CatalogUpdateProgressListener</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a></span> </span>  
Performs an asynchronous request for each catalog to update map data to the latest available version.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync">fromSdkEngineAsync</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromSdkEngineAsync-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-fromSdkEngineAsync-param-mapUpdaterConstructionCallback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback">MapUpdaterConstructionCallback</a></span> <span class="parameter-name">mapUpdaterConstructionCallback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Gets a single instance of this class per provided <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
