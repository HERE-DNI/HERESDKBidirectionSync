---
title: "SegmentSpanData class abstract"
slug: "sdk-for-flutter-navigate-mapdata-segmentspandata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentSpanData-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/SegmentSpanData-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/SegmentSpanData/SegmentSpanData.html">SegmentSpanData</a></li>
<li class="section-title">
<a href="mapdata/SegmentSpanData-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/SegmentSpanData/administrativeRules.html">administrativeRules</a></li>
<li><a href="mapdata/SegmentSpanData/allowedTransportModes.html">allowedTransportModes</a></li>
<li><a href="mapdata/SegmentSpanData/baseSpeedInMetersPerSecond.html">baseSpeedInMetersPerSecond</a></li>
<li><a href="mapdata/SegmentSpanData/functionalRoadClass.html">functionalRoadClass</a></li>
<li class="inherited"><a href="mapdata/SegmentSpanData/hashCode.html">hashCode</a></li>
<li><a href="mapdata/SegmentSpanData/isUrban.html">isUrban</a></li>
<li><a href="mapdata/SegmentSpanData/localRoadCharacteristics.html">localRoadCharacteristics</a></li>
<li><a href="mapdata/SegmentSpanData/negativeDirectionBaseSpeedInMetersPerSecond.html">negativeDirectionBaseSpeedInMetersPerSecond</a></li>
<li><a href="mapdata/SegmentSpanData/negativeDirectionSpeedLimit.html">negativeDirectionSpeedLimit</a></li>
<li><a href="mapdata/SegmentSpanData/physicalAttributes.html">physicalAttributes</a></li>
<li><a href="mapdata/SegmentSpanData/positiveDirectionBaseSpeedInMetersPerSecond.html">positiveDirectionBaseSpeedInMetersPerSecond</a></li>
<li><a href="mapdata/SegmentSpanData/positiveDirectionSpeedLimit.html">positiveDirectionSpeedLimit</a></li>
<li><a href="mapdata/SegmentSpanData/roadNumbers.html">roadNumbers</a></li>
<li><a href="mapdata/SegmentSpanData/roadUsages.html">roadUsages</a></li>
<li class="inherited"><a href="mapdata/SegmentSpanData/runtimeType.html">runtimeType</a></li>
<li><a href="mapdata/SegmentSpanData/spanLengthInMeters.html">spanLengthInMeters</a></li>
<li><a href="mapdata/SegmentSpanData/specialSpeedSituations.html">specialSpeedSituations</a></li>
<li><a href="mapdata/SegmentSpanData/speedLimit.html">speedLimit</a></li>
<li><a href="mapdata/SegmentSpanData/startOffsetInMeters.html">startOffsetInMeters</a></li>
<li><a href="mapdata/SegmentSpanData/streetNames.html">streetNames</a></li>
<li><a href="mapdata/SegmentSpanData/travelDirection.html">travelDirection</a></li>
<li class="section-title inherited"><a href="mapdata/SegmentSpanData-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/SegmentSpanData/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/SegmentSpanData/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapdata/SegmentSpanData-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapdata/SegmentSpanData/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentSpanData class</li>
</ol>
<div class="self-name">SegmentSpanData</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentSpanData-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SegmentSpanData class abstract</h1></div>
<section class="desc markdown">
<p>Contains attributes that are not necessarily constant on a full segment.</p>
<p>A Span is a portion of a Segment where the requested attributes are constant.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SegmentSpanData">
/sdk-for-flutter-navigate-mapdata-segmentspandata-segmentspandata()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="administrativeRules">
/sdk-for-flutter-navigate-mapdata-segmentspandata-administrativerules
→ /sdk-for-flutter-navigate-mapdata-administrativerules-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-administrativerules-class for the segment, containing information
about country code, state code, unit system, tolls, pre-trip planning and other
administrative information.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadadministrativerules is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-mapdata-administrativerules-class for the segment.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="allowedTransportModes">
/sdk-for-flutter-navigate-mapdata-segmentspandata-allowedtransportmodes
→ /sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class object representing the allowed transport modes.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtransportmodesaccess is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="baseSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-mapdata-segmentspandata-basespeedinmeterspersecond
→ double?
</dt>
<dd>
  The average speed expected for this segment span with a car or a similar vehicle.
Will be loaded if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds is <code>true</code>.
Gets the average speed for this segment span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="functionalRoadClass">
/sdk-for-flutter-navigate-mapdata-segmentspandata-functionalroadclass
→ /sdk-for-flutter-navigate-routing-functionalroadclass?
</dt>
<dd>
  The /sdk-for-flutter-navigate-routing-functionalroadclass object representing the polyline of this segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadfunctionalroadclass is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-routing-functionalroadclass object representing the polyline of this section.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapdata-segmentspandata-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isUrban">
/sdk-for-flutter-navigate-mapdata-segmentspandata-isurban
→ bool?
</dt>
<dd>
  The urban attribute of the segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadurban is set to <code>false</code>.
Gets the urban attribute of the segment.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="localRoadCharacteristics">
/sdk-for-flutter-navigate-mapdata-segmentspandata-localroadcharacteristics
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-localroadcharacteristic&gt;?
</dt>
<dd>
  The local road characteristics of the segment: frontage, parking lot road, or POI access road.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadlocalroadcharacteristics is set to <code>false</code>.
Gets the local road characteristics.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="negativeDirectionBaseSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionbasespeedinmeterspersecond
→ double?
</dt>
<dd>
  The average speed expected for this segment in negative direction with a car or a similar
vehicle.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds is set to <code>false</code>.
Gets the average speed in the negative direction.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="negativeDirectionSpeedLimit">
/sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionspeedlimit
→ /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span in the negative
travel direction.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="physicalAttributes">
/sdk-for-flutter-navigate-mapdata-segmentspandata-physicalattributes
→ /sdk-for-flutter-navigate-mapdata-physicalattributes-class?
</dt>
<dd>
  The physical attributes of the segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes is set to <code>false</code>.
Gets the physical attributes.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="positiveDirectionBaseSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionbasespeedinmeterspersecond
→ double?
</dt>
<dd>
  The average speed expected for this segment in positive direction with a car or a similar
vehicle.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds is set to <code>false</code>.
Gets the average speed in the positive direction.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="positiveDirectionSpeedLimit">
/sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionspeedlimit
→ /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span in the positive
tavel direction.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadNumbers">
/sdk-for-flutter-navigate-mapdata-segmentspandata-roadnumbers
→ /sdk-for-flutter-navigate-routing-localizedroadnumbers-class?
</dt>
<dd>
  The road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers is set to <code>false</code>.
Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadUsages">
/sdk-for-flutter-navigate-mapdata-segmentspandata-roadusages
→ /sdk-for-flutter-navigate-mapdata-roadusages-class?
</dt>
<dd>
  The road usages of the segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes is set to <code>false</code>.
Gets the road usages.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-segmentspandata-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="spanLengthInMeters">
/sdk-for-flutter-navigate-mapdata-segmentspandata-spanlengthinmeters
→ int
</dt>
<dd>
  The length of this span in meters.
Gets the length of this span in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="specialSpeedSituations">
/sdk-for-flutter-navigate-mapdata-segmentspandata-specialspeedsituations
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class&gt;?
</dt>
<dd>
  The special speed situations of the segment.
Will be loaded if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspecialspeedsituations is <code>true</code>.
<strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, <code>sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules</code> must also be set to <code>true</code>.
Gets the list of /sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="speedLimit">
/sdk-for-flutter-navigate-mapdata-segmentspandata-speedlimit
→ /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span.
Will be loaded if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits is <code>true</code>.
Gets the /sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class object representing the speed limit of this segment span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="startOffsetInMeters">
/sdk-for-flutter-navigate-mapdata-segmentspandata-startoffsetinmeters
→ int
</dt>
<dd>
  Start offset.
The offset in meters from the beginning of the segment to the start of the span
in positive direction or from the end of the segment to the start of the span in negative direction.
Gets the start offset in meters of the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="streetNames">
/sdk-for-flutter-navigate-mapdata-segmentspandata-streetnames
→ /sdk-for-flutter-navigate-core-localizedtexts-class?
</dt>
<dd>
  The street names on the span.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers is set to <code>false</code>.
The street names on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="travelDirection">
/sdk-for-flutter-navigate-mapdata-segmentspandata-traveldirection
→ /sdk-for-flutter-navigate-routing-traveldirection?
</dt>
<dd>
  The /sdk-for-flutter-navigate-routing-traveldirection object representing the allowed travel directions.
Gets the /sdk-for-flutter-navigate-routing-traveldirection object for the portion of the segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtraveldirection is set to <code>false</code>.
Gets the /sdk-for-flutter-navigate-routing-traveldirection.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-segmentspandata-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-segmentspandata-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapdata-segmentspandata-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentSpanData class</li>
</ol>
<h5>mapdata library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
