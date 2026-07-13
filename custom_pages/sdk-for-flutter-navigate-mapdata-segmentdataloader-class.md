---
title: "SegmentDataLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentDataLoader-class-sidebar.html">

<div>

# <span class="kind-class">SegmentDataLoader</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides the abstract class for the access to the segments data available in the local OCM map.

Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader">SegmentDataLoader</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader-withengine">SegmentDataLoader.withEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile">downloadFile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-downloadFile-param-fileReferences" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-filereference-class">FileReference</a></span>\></span></span> <span class="parameter-name">fileReferences</span>, </span><span id="sdk-for-flutter-navigate-downloadFile-param-downloadingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class">DownloadingFileOptions</a></span> <span class="parameter-name">downloadingOptions</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">Uint8List</span>\></span></span> </span>  
Synchronously load the optional image providing guidance of a directed or non directed segment.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates">getSegmentsAroundCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getSegmentsAroundCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-getSegmentsAroundCoordinates-param-radiusInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">radiusInMeters</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a></span>\></span></span> </span>  
Loads the segments around a certain coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">loadData</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-loadData-param-segment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a></span> <span class="parameter-name">segment</span>, </span><span id="sdk-for-flutter-navigate-loadData-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span> </span>  
Synchronously load the data for the given map segment.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">loadDirectedSegmentData</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-loadDirectedSegmentData-param-segment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a></span> <span class="parameter-name">segment</span>, </span><span id="sdk-for-flutter-navigate-loadDirectedSegmentData-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span> </span>  
Synchronously load the data for the given map directed segment.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

