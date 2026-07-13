---
title: "OfflineSearchIndexError enum - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexerror"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OfflineSearchIndexError-enum-sidebar.html">

<div>

# <span class="kind-enum">OfflineSearchIndexError</span> enum

</div>

<div class="section desc markdown">

Error corresponding to the offline search operation.

</div>

## Values

<span class="name">invalidPersistentPath</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>  
Unreachable `SDKOptions.persistentMapStoragePath` or lacking required permission to generate index inside.

<span class="name">mapError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>  
Failed to get installed regions in protected cache. Any previous available index would be deleted when this error occurs. Use method `MapDownloader.getInitialPersistentMapStatus` to get the status of the map and check `maploader.PersistentMapStatus` for exact healing procedure for specific status.

<span class="name">databaseError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>  
Unable to generate index due to failed database operation. Any previous available index would be deleted when this error occurs. Call `MapDownloader.repairPersistentMap` to retry index generation.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>  
Indexing operation cancelled due to OS killing the application or when a new indexing operation is invoked by SDK after finishing a map operation while the previous indexing operation was in progress. Any previous available index would be deleted when this error occurs. In later case, SDK would finish the latest indexing operation successfully and it can be tracked through `OfflineSearchIndexListener`, otherwise call `MapDownloader.repairPersistentMap` to retry index generation.

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>  
Internal error occurred.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

