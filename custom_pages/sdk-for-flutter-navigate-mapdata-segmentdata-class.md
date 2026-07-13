---
title: "SegmentData class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentData-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentData-class-sidebar.html">

<div>

# <span class="kind-class">SegmentData</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Contains the requested information for a segment

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-segmentdata">SegmentData</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-lengthinmeters">lengthInMeters</a></span> <span class="signature">→ int</span>  
The length of this segment in meters. This information is based on map data. It can differ from the length of <a href="sdk-for-flutter-navigate-mapdata-segmentdata-polyline">SegmentData.polyline</a> due to approximations of the polyline. Gets the length of this segment in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-ocmsegmentid">ocmSegmentId</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a></span>  
The <a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a> object representing the segment Gets the <a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a> object representing the the segment.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-polyline">polyline</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>  
The <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this segment. Gets the <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this segment.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-railwaycrossings">railwayCrossings</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-class">RailwayCrossing</a></span>\></span>?</span>  
The list of <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-class">RailwayCrossing</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadrailwaycrossings">SegmentDataLoaderOptions.loadRailwayCrossings</a> is set to `false`. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-class">RailwayCrossing</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-roadsigns">roadSigns</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadsign-class">RoadSign</a></span>\></span>?</span>  
The list of <a href="sdk-for-flutter-navigate-navigation-roadsign-class">RoadSign</a> of the given segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadsigns">SegmentDataLoaderOptions.loadRoadSigns</a> is set to `false`. Gets the list of <a href="sdk-for-flutter-navigate-navigation-roadsign-class">RoadSign</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-segmentreference">segmentReference</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>  
The <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a> object representing the segment Gets the <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a> object representing the the segment.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-spans">spans</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-class">SegmentSpanData</a></span>\></span></span>  
The list of <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-class">SegmentSpanData</a> of the given segment for the requested attributes **Note:** If no span attributes is requested, the list will be empty. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-class">SegmentSpanData</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-tollpoints">tollPoints</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-tollpoint-class">TollPoint</a></span>\></span>?</span>  
The list of <a href="sdk-for-flutter-navigate-mapdata-tollpoint-class">TollPoint</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtollpoints">SegmentDataLoaderOptions.loadTollPoints</a> is set to `false` or the <a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a> is not initialized using <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a>. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-tollpoint-class">TollPoint</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals">trafficSignals</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a></span>\></span>?</span>  
The list of <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals">SegmentDataLoaderOptions.loadTrafficSignals</a> is set to `false`. The <a href="sdk-for-flutter-navigate-mapdata-trafficsignallocation">TrafficSignalLocation</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead. The <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-offsetinmeters">TrafficSignal.offsetInMeters</a> is the location along the segment, while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
