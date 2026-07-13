---
title: "CatalogUpdateInfo class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateinfo-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateInfo-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/CatalogUpdateInfo-class-sidebar.html">

<div>

# <span class="kind-class">CatalogUpdateInfo</span> class

</div>

<div class="section desc markdown">

Holds information for the catalog update intent.

Provides information regarding installed catalog and its latest available version.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-catalogupdateinfo">CatalogUpdateInfo</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-installedCatalog" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-installedcatalog-class">InstalledCatalog</a></span> <span class="parameter-name">installedCatalog</span>, </span><span id="sdk-for-flutter-navigate-param-latestVersion" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">latestVersion</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-disksizeinbytes">diskSizeInBytes</a></span> <span class="signature">↔ int</span>  
Estimates the size of the offline maps after an update. **Note** In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with `disk_size_in_bytes + temporary_disk_requirement_in_bytes`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-installedcatalog">installedCatalog</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-maploader-installedcatalog-class">InstalledCatalog</a></span>  
Installed catalog.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-latestversion">latestVersion</a></span> <span class="signature">↔ int</span>  
Latest version available for a catalog.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-networksizeinbytes">networkSizeInBytes</a></span> <span class="signature">↔ int</span>  
Total size in bytes that needs to be downloaded over the network to update the installed catalog.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-state">state</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
State of current catalog update.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-temporarydiskrequirementinbytes">temporaryDiskRequirementInBytes</a></span> <span class="signature">↔ int</span>  
Performing an update requires additional storage on top of existing offline maps. This space is used to store intermittent copy of map content according to the specified <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a>. **Note** In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with `disk_size_in_bytes + temporary_disk_requirement_in_bytes`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
