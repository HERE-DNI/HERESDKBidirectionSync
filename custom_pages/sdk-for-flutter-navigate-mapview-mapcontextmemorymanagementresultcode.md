---
title: "MapContextMemoryManagementResultCode enum - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapContextMemoryManagementResultCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContextMemoryManagementResultCode-enum-sidebar.html">

<div>

# <span class="kind-enum">MapContextMemoryManagementResultCode</span> enum

</div>

<div class="section desc markdown">

The memory management result code.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">applied</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
The memory management options were successfully applied.

<span class="name">tileCacheCpuMemoryLimitExceeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
The requested memory limit exceeds the maximum allowed limit for CPU tile cache. Previous value of CPU tile cache limit is preserved. Video memory limit applied correctly.

<span class="name">videoMemoryLimitExceeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
The requested memory limit exceeds the maximum allowed limit for video memory. Previous value of video memory limit is preserved. CPU tile cache limit applied correctly.

<span class="name">failedBothMemoryLimitsExceeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
Both video memory and CPU tile cache limits were exceeded and limits were not applied. Previous values of video memory and CPU tile cache limits are preserved.

<span class="name">failed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
The memory management options could not be applied due to other errors.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
