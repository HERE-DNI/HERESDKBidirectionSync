---
title: "Span (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-span"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.Span → com.here.NativeBase com.here.sdk.routing.Span → com.here.sdk.routing.Span

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Span</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A span is a part of the Section which is traversable or navigable. Each span usually has some geometry associated with it.

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

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBaseDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time duration necessary to traverse the span, using the speed provided in getDynamicSpeedInfo() without taking into consideration the delays caused by the traffic.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">`AccessAttributes`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCarAttributes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of car access attributes on the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getConsumptionInKilowattHours ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the power consumption in kilowatt per hour necessary to traverse the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCountryCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the country code of the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the time duration necessary to traverse the span, using the speed provided in getDynamicSpeedInfo() .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-dynamicspeedinfo" title="class in com.here.sdk.routing">`DynamicSpeedInfo`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDynamicSpeedInfo ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The dynamic speed information on the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">`FunctionalRoadClass`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFunctionalRoadClass ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the functional road class of the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">`GeoPolyline`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the GeoPolyline object representing the polyline of this span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this span in meters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNoThroughRestrictionsIndexes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the list of indexes to Section.getNoThroughRestrictions() the parent section owns.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNoticeIndexes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of indexes to Section.getSectionNotices() the parent section owns.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">`LocalizedRoadNumbers`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadNumbers ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the road numbers on the span enriched with information specific to route numbers of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification ( RouteType ).

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">`AccessAttributes`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getScooterAttributes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of scooter access attributes on the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSectionPolylineOffset ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the position of the span inside the section's geometry, given as an offset.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">`SegmentReference`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSegmentReference ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the segment reference of this span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getShieldText ( LocalizedRoadNumber roadNumber)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts full route number to the value to be displayed on the road shield.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedLimitInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the speed limit in meters per second on the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStateCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the state code of the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-streetattributes" title="enum class in com.here.sdk.routing">`StreetAttributes`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStreetAttributes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of street attributes on the span.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">`LocalizedTexts`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStreetNames ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The street names on the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficIncidentIndexes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The indexes of traffic incidents from the field Section.getTrafficIncidents() of the parent Section .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">`AccessAttributes`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTruckAttributes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of truck access attributes on the span.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-walkattributes" title="enum class in com.here.sdk.routing">`WalkAttributes`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWalkAttributes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of walk attributes on the span.

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

  - <div id="sdk-for-android-navigate-getShieldText-com-here-sdk-routing-LocalizedRoadNumber" class="section detail">

    ### getShieldText

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getShieldText</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumber" title="class in com.here.sdk.routing">LocalizedRoadNumber</a> roadNumber)</span>

    </div>

    <div class="block">

    Converts full route number to the value to be displayed on the road shield. The results are based on country code and state code of Span object and route type of passed road_number argument.

    </div>

    Parameters:  
    `roadNumber` -

    Route number to convert to shield text.

    Returns:  
    Text on the road shield to display.

    </div>

  - <div id="sdk-for-android-navigate-getGeometry" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets the GeoPolyline object representing the polyline of this span.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">`GeoPolyline`</a> object representing the polyline of this span.

    </div>

  - <div id="sdk-for-android-navigate-getLengthInMeters" class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this span in meters.

    </div>

    Returns:  
    The length of this span in meters.

    </div>

  - <div id="sdk-for-android-navigate-getNoticeIndexes" class="section detail">

    ### getNoticeIndexes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">getNoticeIndexes</span>()

    </div>

    <div class="block">

    Gets the list of indexes to Section.getSectionNotices() the parent section owns. In case the list is not empty, the user must judge all the indexed SectionNotice 's carefully before proceeding.

    </div>

    Returns:  
    The list of indexes to [](sdk-for-android-navigate-com-here-sdk-routing-section#getSectionNotices())

        Section.getSectionNotices()

    </a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing">`SectionNotice`</a>s carefully before proceeding.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-getSegmentReference" class="section detail">

    ### getSegmentReference

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">getSegmentReference</span>()

    </div>

    <div class="block">

    Gets the segment reference of this span.

    </div>

    Returns:  
    The segment reference of this span.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficIncidentIndexes" class="section detail">

    ### getTrafficIncidentIndexes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">getTrafficIncidentIndexes</span>()

    </div>

    <div class="block">

    The indexes of traffic incidents from the field Section.getTrafficIncidents() of the parent Section . Each matching incident takes at least a whole getGeometry() . The same incident can take other spans and an area out of the built route as well.

    </div>

    Returns:  
    The indexes of traffic incidents from the field [](sdk-for-android-navigate-com-here-sdk-routing-section#getTrafficIncidents())

        Section.getTrafficIncidents()

    </a> of the parent <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing">`Section`</a>. Each matching incident takes at least a whole [](sdk-for-android-navigate-com-here-sdk-routing-span#getGeometry())

        getGeometry()

    </a>. The same incident can take other spans and an area out of the built route as well.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-getSectionPolylineOffset" class="section detail">

    ### getSectionPolylineOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSectionPolylineOffset</span>()

    </div>

    <div class="block">

    Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.

    </div>

    Returns:  
    The position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.

    </div>

  - <div id="sdk-for-android-navigate-getDynamicSpeedInfo" class="section detail">

    ### getDynamicSpeedInfo

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-dynamicspeedinfo" title="class in com.here.sdk.routing">DynamicSpeedInfo</a></span> <span class="element-name">getDynamicSpeedInfo</span>()

    </div>

    <div class="block">

    The dynamic speed information on the span.

    </div>

    Returns:  
    The dynamic speed information on the span.

    </div>

  - <div id="sdk-for-android-navigate-getStreetAttributes" class="section detail">

    ### getStreetAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-streetattributes" title="enum class in com.here.sdk.routing">StreetAttributes</a>\></span> <span class="element-name">getStreetAttributes</span>()

    </div>

    <div class="block">

    The list of street attributes on the span.

    </div>

    Returns:  
    The list of street attributes on the span.

    </div>

  - <div id="sdk-for-android-navigate-getCarAttributes" class="section detail">

    ### getCarAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>\></span> <span class="element-name">getCarAttributes</span>()

    </div>

    <div class="block">

    The list of car access attributes on the span.

    </div>

    Returns:  
    The list of car access attributes on the span.

    </div>

  - <div id="sdk-for-android-navigate-getTruckAttributes" class="section detail">

    ### getTruckAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>\></span> <span class="element-name">getTruckAttributes</span>()

    </div>

    <div class="block">

    The list of truck access attributes on the span.

    </div>

    Returns:  
    The list of truck access attributes on the span.

    </div>

  - <div id="sdk-for-android-navigate-getScooterAttributes" class="section detail">

    ### getScooterAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>\></span> <span class="element-name">getScooterAttributes</span>()

    </div>

    <div class="block">

    The list of scooter access attributes on the span.

    </div>

    Returns:  
    The list of scooter access attributes on the span.

    </div>

  - <div id="sdk-for-android-navigate-getWalkAttributes" class="section detail">

    ### getWalkAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-walkattributes" title="enum class in com.here.sdk.routing">WalkAttributes</a>\></span> <span class="element-name">getWalkAttributes</span>()

    </div>

    <div class="block">

    The list of walk attributes on the span.

    </div>

    Returns:  
    The list of walk attributes on the span.

    </div>

  - <div id="sdk-for-android-navigate-getStreetNames" class="section detail">

    ### getStreetNames

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getStreetNames</span>()

    </div>

    <div class="block">

    The street names on the span.

    </div>

    Returns:  
    The street names on the span.

    </div>

  - <div id="sdk-for-android-navigate-getRoadNumbers" class="section detail">

    ### getRoadNumbers

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span class="element-name">getRoadNumbers</span>()

    </div>

    <div class="block">

    Gets the road numbers on the span enriched with information specific to route numbers of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification ( RouteType ).

    </div>

    Returns:  
    The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`).

    </div>

  - <div id="sdk-for-android-navigate-getSpeedLimitInMetersPerSecond" class="section detail">

    ### getSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedLimitInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the speed limit in meters per second on the span.

    </div>

    Returns:  
    The speed limit in meters per second on the span.

    </div>

  - <div id="sdk-for-android-navigate-getConsumptionInKilowattHours" class="section detail">

    ### getConsumptionInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()

    </div>

    <div class="block">

    Gets the power consumption in kilowatt per hour necessary to traverse the span.

    </div>

    Returns:  
    The power consumption in kilowatt per hour necessary to traverse the span.

    </div>

  - <div id="sdk-for-android-navigate-getFunctionalRoadClass" class="section detail">

    ### getFunctionalRoadClass

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span class="element-name">getFunctionalRoadClass</span>()

    </div>

    <div class="block">

    Gets the functional road class of the span.

    </div>

    Returns:  
    The functional road class of the span.

    </div>

  - <div id="sdk-for-android-navigate-getDuration" class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the time duration necessary to traverse the span, using the speed provided in getDynamicSpeedInfo() . This duration takes also into consideration the delays caused by the traffic.

    </div>

    Returns:  
    The time duration necessary to traverse the span, using the speed provided in [](sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo())

        getDynamicSpeedInfo()

    </a>. This duration takes also into consideration the delays caused by the traffic.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-getBaseDuration" class="section detail">

    ### getBaseDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getBaseDuration</span>()

    </div>

    <div class="block">

    Gets the time duration necessary to traverse the span, using the speed provided in getDynamicSpeedInfo() without taking into consideration the delays caused by the traffic.

    </div>

    Returns:  
    The time duration necessary to traverse the span, using the speed provided in [](sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo())

        getDynamicSpeedInfo()

    </a> without taking into consideration the delays caused by the traffic.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-getCountryCode" class="section detail">

    ### getCountryCode

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getCountryCode</span>()

    </div>

    <div class="block">

    Gets the country code of the span. The value is null when no data is available.

    </div>

    Returns:  
    The country code of the span. The value is `null` when no data is available.

    </div>

  - <div id="sdk-for-android-navigate-getStateCode" class="section detail">

    ### getStateCode

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getStateCode</span>()

    </div>

    <div class="block">

    Gets the state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is null when no data is available.

    </div>

    Returns:  
    The state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `null` when no data is available.

    </div>

  - <div id="sdk-for-android-navigate-getNoThroughRestrictionsIndexes" class="section detail">

    ### getNoThroughRestrictionsIndexes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">getNoThroughRestrictionsIndexes</span>()

    </div>

    <div class="block">

    Get the list of indexes to Section.getNoThroughRestrictions() the parent section owns. In case the list is not empty, the user must judge all the indexed Section.getNoThroughRestrictions() 's carefully before proceeding.

    </div>

    Returns:  
    The list of indexes to [](sdk-for-android-navigate-com-here-sdk-routing-section#getNoThroughRestrictions())

        Section.getNoThroughRestrictions()

    </a> the parent section owns. In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's carefully before proceeding.

    </p>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

