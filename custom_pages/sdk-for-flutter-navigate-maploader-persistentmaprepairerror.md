---
title: "PersistentMapRepairError enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-persistentmaprepairerror"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/PersistentMapRepairError-enum-sidebar.html">

<div>

# <span class="kind-enum">PersistentMapRepairError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that may result after a map repair operation has been completed.

</div>

## Values

<span class="name">partiallyRestored</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
Persistent map is repaired, but some map data is lost. Lost regions marked with a PENDING status.

<span class="name">invalidPath</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
Invalid persistent map path. The provided path to store the persistent map data doesn't own the required Read/Write (RW) permissions. Try to choose a different path with RW permissions.

<span class="name">brokenDb</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
The persisted map data can't be recovered and all map data was fully deleted. It is recommended, to ask the user if they want to try to download the lost regions again.

<span class="name">noOfflineVersion</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
The map data version was not cached. The region list data will be cleared from the persisted storage. It is recommended to download the list of downloadable regions again. After this it is recommended to try to repair the corrupted map data again.

<span class="name">noJournal</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
It is not possible to retrieve the list of downloaded regions. The region list data will be cleared from the persisted storage. It is recommended to download the list of downloadable regions again. After this it is recommended to try to repair the corrupted map data again.

<span class="name">brokenUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

<span class="name">operationAfterDispose</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
Repair is invoked on object connected to the disposed <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>

<span class="name">unknown</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
An unknown error occurred. Try to clear the persisted storage by calling `sdk.maploader.MapDownloader.clear_persistent_map_storage`. It is recommended, to ask the user if they want to try to download the lost regions again.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

