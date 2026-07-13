---
title: "Region class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-region-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Region-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/Region-class-sidebar.html">

<div>

# <span class="kind-class">Region</span> class

</div>

<div class="section desc markdown">

Defines an area, especially part of a country or the world that can be downloaded.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-region">Region</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-regionId" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span> <span class="parameter-name">regionId</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-childregions">childRegions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-region-class">Region</a></span>\></span>?</span>  
All child regions for current region. Note that each child can again contain multiple children. A downloadable region will contain the content of all children.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-name">name</a></span> <span class="signature">↔ String</span>  
Name of region. Language is determined by the requested <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>. By default, it is in <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode.enUs</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-navigability">navigability</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-maploader-navigabilitytype">NavigabilityType</a></span>  
Indicates the navigability type of this region.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-regionid">regionId</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>  
Unique identifier specifying a region.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-sizeondiskinbytes">sizeOnDiskInBytes</a></span> <span class="signature">↔ int</span>  
Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk. This value is a theoretical maximum for the region's size allocation. Note: If overlapping regions exist or data is already present on the disk, the actual size occupied might be less than this value due to shared or reused map data.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-sizeonnetworkinbytes">sizeOnNetworkInBytes</a></span> <span class="signature">↔ int</span>  
Region size, for downloading/during network operations, in bytes. Regions are downloaded in compressed form and hence they have reduced size on network. Note: This value represents the theoretical maximum size required for the region during transfer. If overlapping data already exists, the actual size downloaded may be smaller due to map data reuse.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
