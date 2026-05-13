---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-maploadererror"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapLoaderError.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapLoaderError"></a>
<a title="MapLoaderError Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapLoaderError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapLoaderError</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapLoaderError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLoaderError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Specifies possible errors that may result from map downloading/prefetching.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO16resourceNotFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/resourceNotFound"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO16resourceNotFoundyA2CmF">resourceNotFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The requested resource is not found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">resourceNotFound</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO8notReadyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notReady"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO8notReadyyA2CmF">notReady</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>There’s a problem with an ongoing download or update: If an operation is in a paused state,
you can resume or cancel it. If no operation is in a paused state: Either wait for active
downloads to finish, or cancel existing <code>sdk.maploader.MapDownloader</code> requests and
call <code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code>. If there is a
problem, call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to repair before
continuing with other <code>sdk.maploader.MapDownloader</code> operations.
This error may occur when an on-going or paused operation prevents the requested task.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notReady</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO15invalidArgumentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidArgument"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO15invalidArgumentyA2CmF">invalidArgument</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request passed invalid arguments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidArgument</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationCancelled"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF">operationCancelled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request was cancelled (usually by the user).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationCancelled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO16alreadyInstalledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/alreadyInstalled"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO16alreadyInstalledyA2CmF">alreadyInstalled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All tiles of requested regions were already installed, no need for any download.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">alreadyInstalled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO7timeOutyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/timeOut"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO7timeOutyA2CmF">timeOut</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request exceeded the timeout limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">timeOut</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO18serviceUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serviceUnavailable"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO18serviceUnavailableyA2CmF">serviceUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The requested service is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serviceUnavailable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO12accessDeniedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/accessDenied"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO12accessDeniedyA2CmF">accessDenied</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The access is denied due to invalid credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">accessDenied</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO19requestLimitReachedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/requestLimitReached"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO19requestLimitReachedyA2CmF">requestLimitReached</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Request limit reached for set a credentials for a particular period of time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">requestLimitReached</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO017networkConnectionD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/networkConnectionError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO017networkConnectionD0yA2CmF">networkConnectionError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A network connection error has happened.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">networkConnectionError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO9forbiddenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/forbidden"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO9forbiddenyA2CmF">forbidden</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The operation is forbidden, make sure your credentials grant the necessary permissions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">forbidden</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO07mapDataD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapDataError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO07mapDataD0yA2CmF">mapDataError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloaded map data is invalid or a <code>sdk.maploader.RegionId</code> passed to the method
<code>sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapDataError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO24unexpectedServerResponseyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unexpectedServerResponse"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO24unexpectedServerResponseyA2CmF">unexpectedServerResponse</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Received unexpected response from the backend. It means the response is malformed or
server returned an internal error. Try repeating the request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unexpectedServerResponse</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO010mapManagerD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapManagerError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO010mapManagerD0yA2CmF">mapManagerError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error occurred inside the map manager and might be related to network issues. Try
repeating the request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapManagerError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO14incompleteDatayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/incompleteData"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO14incompleteDatayA2CmF">incompleteData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The data to process is incomplete, failed decoding the tile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">incompleteData</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serviceAccessFailed"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF">serviceAccessFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The conditions to access the service are not satisfied. Check if correct
<code>sdk.maploader.RegionId</code> was passed to <code>sdk.maploader.MapDownloader.download_regions</code> or
download for passed <code>sdk.maploader.RegionId</code> already started. Further control for
started download must be performed through <code>sdk.maploader.MapDownloaderTask</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serviceAccessFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF">internalError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal error occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO7offlineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offline"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO7offlineyA2CmF">offline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Online operation is not permitted because offline mode is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">offline</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO07cacheIoD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cacheIoError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO07cacheIoD0yA2CmF">cacheIoError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A cache IO error occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cacheIoError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO23protectedCacheCorruptedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/protectedCacheCorrupted"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO23protectedCacheCorruptedyA2CmF">protectedCacheCorrupted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protected cache is corrupted. It can be a result of downloading the map in the background
and the OS killing the application at that time. Use method
<code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code> to get the status of the
map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is
broken.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">protectedCacheCorrupted</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO17migrationRequiredyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/migrationRequired"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO17migrationRequiredyA2CmF">migrationRequired</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Operation on the protected cache cannot be done due to required migration.
Call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to perform migration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">migrationRequired</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO21operationAfterDisposeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationAfterDispose"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO21operationAfterDisposeyA2CmF">operationAfterDispose</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Method is invoked on object connected to the disposed SDKNativeEngine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationAfterDispose</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO020catalogConfigurationD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/catalogConfigurationError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO020catalogConfigurationD0yA2CmF">catalogConfigurationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Misconfiguration of catalogs.
This error may occur when <code>sdk.core.engine.CatalogConfiguration</code> is misconfigured and
cannot be used for any operation with <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapdownloader">MapDownloader</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapupdater">MapUpdater</a></code>.
Verify <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp">SDKOptions.catalogConfigurations</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">catalogConfigurationError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO13pendingUpdateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pendingUpdate"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO13pendingUpdateyA2CmF">pendingUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map regions update was interrupted. Indicates that the cache state is wrong after an
update that was finished not in correct way (e.g sudden app shutdown).
Prefetching or removing of map regions are blocked until
the update has been completed successfully.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pendingUpdate</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO29updateBlockedAsAnotherPendingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/updateBlockedAsAnotherPending"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO29updateBlockedAsAnotherPendingyA2CmF">updateBlockedAsAnotherPending</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.
Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">updateBlockedAsAnotherPending</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO12brokenUpdateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/brokenUpdate"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO12brokenUpdateyA2CmF">brokenUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unrecoverable error during construction of pending update parameters.
Operations such as catalog updates or region downloads will fail.
The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">brokenUpdate</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO15parallelRequestyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parallelRequest"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO15parallelRequestyA2CmF">parallelRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">parallelRequest</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO25proxyAuthenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyAuthenticationFailed"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO25proxyAuthenticationFailedyA2CmF">proxyAuthenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy is not authenticated. Check your proxy credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">proxyAuthenticationFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO22proxyServerUnreachableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyServerUnreachable"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO22proxyServerUnreachableyA2CmF">proxyServerUnreachable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy server unreachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">proxyServerUnreachable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notEnoughSpace"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF">notEnoughSpace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>There’s no sufficient space on the disk to finish operation.
For offline maps operation (download or update), it means that
there’s not enough space on the device.
For prefetch operations, it means that there’s not enough space
in the mutable cache to store the prefetched data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notEnoughSpace</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO18onlineNavigateOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineNavigateOnly"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO18onlineNavigateOnlyyA2CmF">onlineNavigateOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This version of HERE SDK does not support the ability to download maps.
Contact the sales team to get access to the full version.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">onlineNavigateOnly</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
