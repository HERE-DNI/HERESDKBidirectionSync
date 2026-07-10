---
title: "SegmentSpanData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapdata.SegmentSpanData → com.here.NativeBase com.here.sdk.mapdata.SegmentSpanData → com.here.sdk.mapdata.SegmentSpanData

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentSpanData</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata">`AdministrativeRules`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAdministrativeRules ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the AdministrativeRules for the segment.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata">`AllowedTransportModes`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAllowedTransportModes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the AllowedTransportModes object.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBaseSpeedInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the average speed for this segment span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">`FunctionalRoadClass`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFunctionalRoadClass ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the FunctionalRoadClass object representing the polyline of this section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-localroadcharacteristic" title="enum class in com.here.sdk.mapdata">`LocalRoadCharacteristic`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLocalRoadCharacteristics ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the local road characteristics.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNegativeDirectionBaseSpeedInMetersPerSecond ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the average speed in the negative direction.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNegativeDirectionSpeedLimit ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the SegmentSpeedLimit object representing the speed limit of this segment span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes" title="class in com.here.sdk.mapdata">`PhysicalAttributes`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPhysicalAttributes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the physical attributes.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPositiveDirectionBaseSpeedInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the average speed in the positive direction.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPositiveDirectionSpeedLimit ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the SegmentSpeedLimit object representing the speed limit of this segment span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">`LocalizedRoadNumbers`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadNumbers ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the road numbers on the span enriched with information specific to route numbers of a road such as I-10, US-50, or A3.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-roadusages" title="class in com.here.sdk.mapdata">`RoadUsages`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadUsages ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the road usages.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpanLengthInMeters ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this span in meters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata">`SegmentSpecialSpeedSituation`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpecialSpeedSituations ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of SegmentSpecialSpeedSituation .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedLimit ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the SegmentSpeedLimit object representing the speed limit of this segment span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStartOffsetInMeters ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the start offset in meters of the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">`LocalizedTexts`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStreetNames ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The street names on the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">`TravelDirection`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTravelDirection ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the TravelDirection .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang"><code>Boolean</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isUrban ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the urban attribute of the segment.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getStartOffsetInMeters" class="section detail">

    ### getStartOffsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getStartOffsetInMeters</span>()

    </div>

    <div class="block">

    Gets the start offset in meters of the span. The offset in meters from the beginning of the segment to the start of the span in positive direction or from the end of the segment to the start of the span in negative direction.

    </div>

    Returns:  
    Start offset.

    </div>

  - <div id="sdk-for-android-navigate-getSpanLengthInMeters" class="section detail">

    ### getSpanLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSpanLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this span in meters.

    </div>

    Returns:  
    The length of this span in meters.

    </div>

  - <div id="sdk-for-android-navigate-getTravelDirection" class="section detail">

    ### getTravelDirection

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span class="element-name">getTravelDirection</span>()

    </div>

    <div class="block">

    Gets the TravelDirection . Gets the TravelDirection object for the portion of the segment. Returns null if SegmentDataLoaderOptions.loadTravelDirection is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">`TravelDirection`</a> object representing the allowed travel directions.

    </div>

  - <div id="sdk-for-android-navigate-getAllowedTransportModes" class="section detail">

    ### getAllowedTransportModes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata">AllowedTransportModes</a></span> <span class="element-name">getAllowedTransportModes</span>()

    </div>

    <div class="block">

    Gets the AllowedTransportModes object. Returns null if SegmentDataLoaderOptions.loadTransportModesAccess is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata">`AllowedTransportModes`</a> object representing the allowed transport modes.

    </div>

  - <div id="sdk-for-android-navigate-getFunctionalRoadClass" class="section detail">

    ### getFunctionalRoadClass

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span class="element-name">getFunctionalRoadClass</span>()

    </div>

    <div class="block">

    Gets the FunctionalRoadClass object representing the polyline of this section. Returns null if SegmentDataLoaderOptions.loadFunctionalRoadClass is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">`FunctionalRoadClass`</a> object representing the polyline of this segment.

    </div>

  - <div id="sdk-for-android-navigate-getPositiveDirectionSpeedLimit" class="section detail">

    ### getPositiveDirectionSpeedLimit

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getPositiveDirectionSpeedLimit</span>()

    </div>

    <div class="block">

    Gets the SegmentSpeedLimit object representing the speed limit of this segment span. Returns null if SegmentDataLoaderOptions.loadSpeedLimits is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span in the positive tavel direction.

    </div>

  - <div id="sdk-for-android-navigate-getNegativeDirectionSpeedLimit" class="section detail">

    ### getNegativeDirectionSpeedLimit

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getNegativeDirectionSpeedLimit</span>()

    </div>

    <div class="block">

    Gets the SegmentSpeedLimit object representing the speed limit of this segment span. Returns null if SegmentDataLoaderOptions.loadSpeedLimits is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span in the negative travel direction.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedLimit" class="section detail">

    ### getSpeedLimit

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getSpeedLimit</span>()

    </div>

    <div class="block">

    Gets the SegmentSpeedLimit object representing the speed limit of this segment span. Will be loaded if SegmentDataLoaderOptions.loadSpeedLimits is true .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">`SegmentSpeedLimit`</a> object representing the speed limit of this segment span.

    </div>

  - <div id="sdk-for-android-navigate-getPositiveDirectionBaseSpeedInMetersPerSecond" class="section detail">

    ### getPositiveDirectionBaseSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getPositiveDirectionBaseSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the average speed in the positive direction. Returns null if SegmentDataLoaderOptions.loadBaseSpeeds is set to false .

    </div>

    Returns:  
    The average speed expected for this segment in positive direction with a car or a similar vehicle.

    </div>

  - <div id="sdk-for-android-navigate-getNegativeDirectionBaseSpeedInMetersPerSecond" class="section detail">

    ### getNegativeDirectionBaseSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getNegativeDirectionBaseSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the average speed in the negative direction. Returns null if SegmentDataLoaderOptions.loadBaseSpeeds is set to false .

    </div>

    Returns:  
    The average speed expected for this segment in negative direction with a car or a similar vehicle.

    </div>

  - <div id="sdk-for-android-navigate-getBaseSpeedInMetersPerSecond" class="section detail">

    ### getBaseSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getBaseSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the average speed for this segment span. Will be loaded if SegmentDataLoaderOptions.loadBaseSpeeds is true .

    </div>

    Returns:  
    The average speed expected for this segment span with a car or a similar vehicle.

    </div>

  - <div id="sdk-for-android-navigate-getLocalRoadCharacteristics" class="section detail">

    ### getLocalRoadCharacteristics

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-localroadcharacteristic" title="enum class in com.here.sdk.mapdata">LocalRoadCharacteristic</a>\></span> <span class="element-name">getLocalRoadCharacteristics</span>()

    </div>

    <div class="block">

    Gets the local road characteristics. Returns null if SegmentDataLoaderOptions.loadLocalRoadCharacteristics is set to false .

    </div>

    Returns:  
    The local road characteristics of the segment: frontage, parking lot road, or POI access road.

    </div>

  - <div id="sdk-for-android-navigate-getStreetNames" class="section detail">

    ### getStreetNames

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getStreetNames</span>()

    </div>

    <div class="block">

    The street names on the span. Returns null if SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers is set to false .

    </div>

    Returns:  
    The street names on the span.

    </div>

  - <div id="sdk-for-android-navigate-getRoadNumbers" class="section detail">

    ### getRoadNumbers

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span class="element-name">getRoadNumbers</span>()

    </div>

    <div class="block">

    Gets the road numbers on the span enriched with information specific to route numbers of a road such as I-10, US-50, or A3. Returns null if SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers is set to false .

    </div>

    Returns:  
    The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3.

    </div>

  - <div id="sdk-for-android-navigate-getPhysicalAttributes" class="section detail">

    ### getPhysicalAttributes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes" title="class in com.here.sdk.mapdata">PhysicalAttributes</a></span> <span class="element-name">getPhysicalAttributes</span>()

    </div>

    <div class="block">

    Gets the physical attributes. Returns null if SegmentDataLoaderOptions.loadRoadAttributes is set to false .

    </div>

    Returns:  
    The physical attributes of the segment.

    </div>

  - <div id="sdk-for-android-navigate-getRoadUsages" class="section detail">

    ### getRoadUsages

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-roadusages" title="class in com.here.sdk.mapdata">RoadUsages</a></span> <span class="element-name">getRoadUsages</span>()

    </div>

    <div class="block">

    Gets the road usages. Returns null if SegmentDataLoaderOptions.loadRoadAttributes is set to false .

    </div>

    Returns:  
    The road usages of the segment.

    </div>

  - <div id="sdk-for-android-navigate-getAdministrativeRules" class="section detail">

    ### getAdministrativeRules

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span class="element-name">getAdministrativeRules</span>()

    </div>

    <div class="block">

    Gets the AdministrativeRules for the segment. Returns null if SegmentDataLoaderOptions.loadAdministrativeRules is set to false .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata">`AdministrativeRules`</a> for the segment, containing information about country code, state code, unit system, tolls, pre-trip planning and other administrative information.

    </div>

  - <div id="sdk-for-android-navigate-isUrban" class="section detail">

    ### isUrban

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isUrban</span>()

    </div>

    <div class="block">

    Gets the urban attribute of the segment. Returns null if SegmentDataLoaderOptions.loadUrban is set to false .

    </div>

    Returns:  
    The urban attribute of the segment.

    </div>

  - <div id="sdk-for-android-navigate-getSpecialSpeedSituations" class="section detail">

    ### getSpecialSpeedSituations

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata">SegmentSpecialSpeedSituation</a>\></span> <span class="element-name">getSpecialSpeedSituations</span>()

    </div>

    <div class="block">

    Gets the list of SegmentSpecialSpeedSituation . Will be loaded if SegmentDataLoaderOptions.loadSpecialSpeedSituations is true . Note: To get timezone offset and daylight saving time values for TimeRule, \[sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules\] must also be set to true .

    </div>

    Returns:  
    The special speed situations of the segment.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

