---
title: "MapLoaderError enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-maploadererror"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapLoaderError-enum-sidebar.html">

<div>

# <span class="kind-enum">MapLoaderError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that may result from map downloading/prefetching.

</div>

## Values

<span class="name">resourceNotFound</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The requested resource is not found.

<span class="name">notReady</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
There's a problem with an ongoing download or update: If an operation is in a paused state, you can resume or cancel it. If no operation is in a paused state: Either wait for active downloads to finish, or cancel existing `sdk.maploader.MapDownloader` requests and call `sdk.maploader.MapDownloader.get_initial_persistent_map_status`. If there is a problem, call `sdk.maploader.MapDownloader.repair_persistent_map` to repair before continuing with other `sdk.maploader.MapDownloader` operations. This error may occur when an on-going or paused operation prevents the requested task.

<span class="name">invalidArgument</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The request passed invalid arguments.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The request was cancelled (usually by the user).

<span class="name">alreadyInstalled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
All tiles of requested regions were already installed, no need for any download.

<span class="name">timeOut</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The request exceeded the timeout limit.

<span class="name">serviceUnavailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The requested service is unavailable.

<span class="name">accessDenied</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The access is denied due to invalid credentials.

<span class="name">requestLimitReached</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Request limit reached for set a credentials for a particular period of time.

<span class="name">networkConnectionError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
A network connection error has happened.

<span class="name">forbidden</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The operation is forbidden, make sure your credentials grant the necessary permissions.

<span class="name">mapDataError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Downloaded map data is invalid or a `sdk.maploader.RegionId` passed to the method `sdk.maploader.MapDownloader.delete_regions` is incorrect.

<span class="name">unexpectedServerResponse</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Received unexpected response from the backend. It means the response is malformed or server returned an internal error. Try repeating the request.

<span class="name">mapManagerError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Error occurred inside the map manager and might be related to network issues. Try repeating the request.

<span class="name">incompleteData</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The data to process is incomplete, failed decoding the tile.

<span class="name">serviceAccessFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
The conditions to access the service are not satisfied. Check if correct `sdk.maploader.RegionId` was passed to `sdk.maploader.MapDownloader.download_regions` or download for passed `sdk.maploader.RegionId` already started. Further control for started download must be performed through `sdk.maploader.MapDownloaderTask`.

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Internal error occurred.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Online operation is not permitted because offline mode is enabled.

<span class="name">cacheIoError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
A cache IO error occurred.

<span class="name">protectedCacheCorrupted</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Protected cache is corrupted. It can be a result of downloading the map in the background and the OS killing the application at that time. Use method `sdk.maploader.MapDownloader.get_initial_persistent_map_status` to get the status of the map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is broken.

<span class="name">migrationRequired</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Operation on the protected cache cannot be done due to required migration. Call `sdk.maploader.MapDownloader.repair_persistent_map` to perform migration.

<span class="name">operationAfterDispose</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Method is invoked on object connected to the disposed SDKNativeEngine.

<span class="name">catalogConfigurationError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Misconfiguration of catalogs. This error may occur when `sdk.core.engine.CatalogConfiguration` is misconfigured and cannot be used for any operation with `MapDownloader` or `MapUpdater`. Verify <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-catalogconfigurations">SDKOptions.catalogConfigurations</a>.

<span class="name">pendingUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Map regions update was interrupted. Indicates that the cache state is wrong after an update that was finished not in correct way (e.g sudden app shutdown). Prefetching or removing of map regions are blocked until the update has been completed successfully.

<span class="name">updateBlockedAsAnotherPending</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state. Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.

<span class="name">brokenUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

<span class="name">parallelRequest</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Proxy server unreachable.

<span class="name">notEnoughSpace</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
There's no sufficient space on the disk to finish operation. For offline maps operation (download or update), it means that there's not enough space on the device. For prefetch operations, it means that there's not enough space in the mutable cache to store the prefetched data.

<span class="name">onlineNavigateOnly</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
This version of HERE SDK does not support the ability to download maps. Contact the sales team to get access to the full version.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

