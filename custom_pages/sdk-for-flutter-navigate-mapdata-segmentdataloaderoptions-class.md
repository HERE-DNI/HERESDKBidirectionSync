---
title: "SegmentDataLoaderOptions class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentDataLoaderOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentDataLoaderOptions-class-sidebar.html">

<div>

# <span class="kind-class">SegmentDataLoaderOptions</span> class

</div>

<div class="section desc markdown">

Specifies which data should be loaded by the <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> function.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-segmentdataloaderoptions">SegmentDataLoaderOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadadministrativerules">loadAdministrativeRules</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-administrativerules">SegmentSpanData.administrativeRules</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds">loadBaseSpeeds</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionbasespeedinmeterspersecond">SegmentSpanData.positiveDirectionBaseSpeedInMetersPerSecond</a>, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionbasespeedinmeterspersecond">SegmentSpanData.negativeDirectionBaseSpeedInMetersPerSecond</a> and <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-basespeedinmeterspersecond">SegmentSpanData.baseSpeedInMetersPerSecond</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadfunctionalroadclass">loadFunctionalRoadClass</a></span> <span class="signature">↔ bool</span>  
If it is true, the <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-functionalroadclass">SegmentSpanData.functionalRoadClass</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadlocalroadcharacteristics">loadLocalRoadCharacteristics</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-localroadcharacteristics">SegmentSpanData.localRoadCharacteristics</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadrailwaycrossings">loadRailwayCrossings</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentdata-railwaycrossings">SegmentData.railwayCrossings</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes">loadRoadAttributes</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-physicalattributes">SegmentSpanData.physicalAttributes</a> and <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-roadusages">SegmentSpanData.roadUsages</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadsigns">loadRoadSigns</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentdata-roadsigns">SegmentData.roadSigns</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspecialspeedsituations">loadSpecialSpeedSituations</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-specialspeedsituations">SegmentSpanData.specialSpeedSituations</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> is called. **Note:** To get timezone offset and daylight saving time values for TimeRule, `sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules` must also be set to `true`. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits">loadSpeedLimits</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionspeedlimit">SegmentSpanData.positiveDirectionSpeedLimit</a>, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionspeedlimit">SegmentSpanData.negativeDirectionSpeedLimit</a> and <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-speedlimit">SegmentSpanData.speedLimit</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers">loadStreetNamesAndRoadNumbers</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-streetnames">SegmentSpanData.streetNames</a> and <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-roadnumbers">SegmentSpanData.roadNumbers</a> and will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtollpoints">loadTollPoints</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentdata-tollpoints">SegmentData.tollPoints</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals">loadTrafficSignals</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals">SegmentData.trafficSignals</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtransportmodesaccess">loadTransportModesAccess</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-allowedtransportmodes">SegmentSpanData.allowedTransportModes</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtraveldirection">loadTravelDirection</a></span> <span class="signature">↔ bool</span>  
If it is true, the <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-traveldirection">SegmentSpanData.travelDirection</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> or <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">SegmentDataLoader.loadDirectedSegmentData</a> is called.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadurban">loadUrban</a></span> <span class="signature">↔ bool</span>  
If it is true, <a href="sdk-for-flutter-navigate-mapdata-segmentspandata-isurban">SegmentSpanData.isUrban</a> will be loaded when <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">SegmentDataLoader.loadData</a> is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
