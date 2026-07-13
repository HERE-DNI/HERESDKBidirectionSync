---
title: "CatalogUpdateState enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogupdatestate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateState.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/CatalogUpdateState-enum-sidebar.html">

<div>

# <span class="kind-enum">CatalogUpdateState</span> enum

</div>

<div class="section desc markdown">

Represents the state of catalog map updates.

</div>

## Values

<span class="name">updateAvailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
Previously downloaded catalog version can be updated to their latest version.

<span class="name">pendingUpdate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
Previous catalog downloading is ongoing or interrupted.

<span class="name">updateBlockedAsAnotherPending</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
When more than one catalog is used or configured, and the update process for it fails, then that specific catalog goes in PENDING_UPDATE state. A user should not update any other catalog until the catalog in PENDING_UPDATE state is updated. Other catalogs will be set to UPDATE_BLOCKED_AS_ANOTHER_PENDING until the update process has been completed.

<span class="name">unknownState</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
State is not fetched, so unknown

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
