---
title: "MapUpdaterMapUpdateVersionCommitPolicy enum - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapUpdaterMapUpdateVersionCommitPolicy-enum-sidebar.html">

<div>

# <span class="kind-enum">MapUpdaterMapUpdateVersionCommitPolicy</span> enum

</div>

<div class="section desc markdown">

Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely.

This influences the required size of the storage during an update. Regardless of the set policy, during an update, the previous region data is kept until the new region data is committed successfully to the persisted storage. This allows to revert to the previous version in case the update fails. With <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onComplete</a>, more data has to be kept until the update process finishes, while <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a> allows to make faster use of the downloaded region and requires less disk space as only the currently updated region is kept until the process completes. However, with an <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a> policy the overall process can be less reliable and bears a higher risk of errors.

</div>

## Values

<span class="name">onFirstRegion</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></span>  
Updates the cache and the persisted storage once the first region was fully downloaded. If only one region was requested, this setting is equivalent to <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onComplete</a>. If more regions or subregions are requested, then the policy will apply. For example, if Germany is requested to be updated, then the cache and the persisted storage will be updated as soon as any contained subregion such as Berlin or Brandenburg has been fully downloaded. The previous data for a region will be removed once that specific region has been updated successfully. However, the <a href="sdk-for-flutter-navigate-maploader-mapversionhandle-class">MapVersionHandle</a> will be updated once the first region has been installed. This inconsistency will be gone, once the update process completes. In case of errors, or an aborted update process, <a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> indicates that still an update is available until the process was successfully repeated.

<span class="name">onComplete</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></span>  
Commits the new map version to the cache and the persisted storage once all previously installed regions have been updated. For example, if Germany needs an update, then all previous data is kept until Germany including all subregions has been downloaded. This update process is more reliable than <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a>, but requires more free storage space until the process completes. Besides, users need to wait longer until they can use all updated regions.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

