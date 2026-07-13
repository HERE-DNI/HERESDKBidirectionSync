---
title: "SegmentSpanData class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentspandata-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentSpanData-class-sidebar.html">

<div>

# <span class="kind-class">SegmentSpanData</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Contains attributes that are not necessarily constant on a full segment.

A Span is a portion of a Segment where the requested attributes are constant.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-segmentspandata">SegmentSpanData</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-administrativerules">administrativeRules</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a>?</span>  
The <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> for the segment, containing information about country code, state code, unit system, tolls, pre-trip planning and other administrative information. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadadministrativerules">SegmentDataLoaderOptions.loadAdministrativeRules</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> for the segment.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-allowedtransportmodes">allowedTransportModes</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class">AllowedTransportModes</a>?</span>  
The <a href="sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class">AllowedTransportModes</a> object representing the allowed transport modes. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtransportmodesaccess">SegmentDataLoaderOptions.loadTransportModesAccess</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class">AllowedTransportModes</a> object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-basespeedinmeterspersecond">baseSpeedInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The average speed expected for this segment span with a car or a similar vehicle. Will be loaded if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds">SegmentDataLoaderOptions.loadBaseSpeeds</a> is `true`. Gets the average speed for this segment span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-functionalroadclass">functionalRoadClass</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-functionalroadclass">FunctionalRoadClass</a>?</span>  
The <a href="sdk-for-flutter-navigate-routing-functionalroadclass">FunctionalRoadClass</a> object representing the polyline of this segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadfunctionalroadclass">SegmentDataLoaderOptions.loadFunctionalRoadClass</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-routing-functionalroadclass">FunctionalRoadClass</a> object representing the polyline of this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-isurban">isUrban</a></span> <span class="signature">→ bool?</span>  
The urban attribute of the segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadurban">SegmentDataLoaderOptions.loadUrban</a> is set to `false`. Gets the urban attribute of the segment.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-localroadcharacteristics">localRoadCharacteristics</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-localroadcharacteristic">LocalRoadCharacteristic</a></span>\></span>?</span>  
The local road characteristics of the segment: frontage, parking lot road, or POI access road. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadlocalroadcharacteristics">SegmentDataLoaderOptions.loadLocalRoadCharacteristics</a> is set to `false`. Gets the local road characteristics.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionbasespeedinmeterspersecond">negativeDirectionBaseSpeedInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The average speed expected for this segment in negative direction with a car or a similar vehicle. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds">SegmentDataLoaderOptions.loadBaseSpeeds</a> is set to `false`. Gets the average speed in the negative direction.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionspeedlimit">negativeDirectionSpeedLimit</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a>?</span>  
The <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span in the negative travel direction. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits">SegmentDataLoaderOptions.loadSpeedLimits</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-physicalattributes">physicalAttributes</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-physicalattributes-class">PhysicalAttributes</a>?</span>  
The physical attributes of the segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes">SegmentDataLoaderOptions.loadRoadAttributes</a> is set to `false`. Gets the physical attributes.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionbasespeedinmeterspersecond">positiveDirectionBaseSpeedInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The average speed expected for this segment in positive direction with a car or a similar vehicle. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds">SegmentDataLoaderOptions.loadBaseSpeeds</a> is set to `false`. Gets the average speed in the positive direction.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionspeedlimit">positiveDirectionSpeedLimit</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a>?</span>  
The <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span in the positive tavel direction. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits">SegmentDataLoaderOptions.loadSpeedLimits</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-roadnumbers">roadNumbers</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-localizedroadnumbers-class">LocalizedRoadNumbers</a>?</span>  
The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers">SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a> is set to `false`. Gets the road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-roadusages">roadUsages</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-roadusages-class">RoadUsages</a>?</span>  
The road usages of the segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes">SegmentDataLoaderOptions.loadRoadAttributes</a> is set to `false`. Gets the road usages.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-spanlengthinmeters">spanLengthInMeters</a></span> <span class="signature">→ int</span>  
The length of this span in meters. Gets the length of this span in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-specialspeedsituations">specialSpeedSituations</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class">SegmentSpecialSpeedSituation</a></span>\></span>?</span>  
The special speed situations of the segment. Will be loaded if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspecialspeedsituations">SegmentDataLoaderOptions.loadSpecialSpeedSituations</a> is `true`. **Note:** To get timezone offset and daylight saving time values for TimeRule, `sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules` must also be set to `true`. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class">SegmentSpecialSpeedSituation</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-speedlimit">speedLimit</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a>?</span>  
The <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span. Will be loaded if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits">SegmentDataLoaderOptions.loadSpeedLimits</a> is `true`. Gets the <a href="sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class">SegmentSpeedLimit</a> object representing the speed limit of this segment span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-startoffsetinmeters">startOffsetInMeters</a></span> <span class="signature">→ int</span>  
Start offset. The offset in meters from the beginning of the segment to the start of the span in positive direction or from the end of the segment to the start of the span in negative direction. Gets the start offset in meters of the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-streetnames">streetNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-localizedtexts-class">LocalizedTexts</a>?</span>  
The street names on the span. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers">SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a> is set to `false`. The street names on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-traveldirection">travelDirection</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a>?</span>  
The <a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a> object representing the allowed travel directions. Gets the <a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a> object for the portion of the segment. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtraveldirection">SegmentDataLoaderOptions.loadTravelDirection</a> is set to `false`. Gets the <a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspandata-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

