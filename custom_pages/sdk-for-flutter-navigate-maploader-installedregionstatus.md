---
title: "InstalledRegionStatus enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-installedregionstatus"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/InstalledRegionStatus-enum-sidebar.html">

<div>

# <span class="kind-enum">InstalledRegionStatus</span> enum

</div>

<div class="section desc markdown">

Represents download status of region in the persistent map storage.

</div>

## Values

<span class="name">installed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus</a></span>  
Region is ready to be used.

<span class="name">pending</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus</a></span>  
Download is not finished yet. Either try to download this region again and, eventually, the progress will continue where it was left off - or you can cancel this download or delete this region. The following reasons can lead to this status: An ongoing or paused download or an abrupt end, for example, when the app was closed. Ongoing or paused downloads can be resumed with the <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a>.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

