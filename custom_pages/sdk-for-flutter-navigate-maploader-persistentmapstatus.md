---
title: "PersistentMapStatus enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-persistentmapstatus"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/PersistentMapStatus-enum-sidebar.html">

<div>

# <span class="kind-enum">PersistentMapStatus</span> enum

</div>

<div class="section desc markdown">

Specifies possible statuses of the already downloaded map regions as a whole.

Note: This can be valid only for a single region in case of a <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus.corrupted</a> state.

</div>

## Values

<span class="name">ok</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
All downloaded regions are in a workable state, no issues found.

<span class="name">corrupted</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
One or more downloaded regions failed to open and a repair action should be performed to mitigate this issue. All map download and map update operations (except for `sdk.maploader.MapDownloader.repair_persistent_map`) will return `sdk.maploader.MapLoaderError.NOT_READY`.

<span class="name">brokenUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

<span class="name">migrationNeeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Indicates that the downloaded regions need to be migrated to a new internal format by calling `sdk.maploader.MapDownloader.repair_persistent_map`. This error is not a result of a data loss, nor any data will be lost when performing the repair operation and the map version will stay unchanged afterwards.

<span class="name">pendingUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
A map update operation initiated by a user has been interrupted. Calls to `sdk.maploader.MapDownloader.download_regions` and `sdk.maploader.MapDownloader.delete_regions` will fail with `sdk.maploader.MapLoaderError.INTERNAL_ERROR`. To repair a map, call again `sdk.maploader.MapUpdater.update_catalog` for the affected catalog. `sdk.maploader.MapUpdater.retrieve_catalogs_update_info` returns a list of `sdk.maploader.CatalogUpdateInfo` items: The affected catalog can be identified by the state, which is set to `sdk.maploader.CatalogUpdateState.PENDING_UPDATE`. To know if a map needs to be repaired, check if `sdk.maploader.MapLoaderError.PENDING_UPDATE` has occurred.

<span class="name">invalidPath</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Unreachable <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a> or <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>. Make sure that <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> has accessible <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a> and <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>

<span class="name">invalidState</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Unrecoverable error during construction of internal map access object. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

<span class="name">storageClosed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

