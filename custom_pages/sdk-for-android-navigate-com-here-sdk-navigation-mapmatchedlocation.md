---
title: "MapMatchedLocation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.MapMatchedLocation → com.here.sdk.navigation.MapMatchedLocation

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapMatchedLocation</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Describes a map-matched location in the world at a given time.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#bearingInDegrees" class="member-name-link"><code>bearingInDegrees</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#confidence" class="member-name-link"><code>confidence</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Confidence level (between 0 and 1) of the matched location.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#coordinates" class="member-name-link"><code>coordinates</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The geographic coordinates of the map-matched location.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#horizontalAccuracyInMeters" class="member-name-link"><code>horizontalAccuracyInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Horizontal accuracy measure of location.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#isDrivingInTheWrongWay" class="member-name-link"><code>isDrivingInTheWrongWay</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Determines if the travel direction on a one-way street is against the allowed traffic direction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#segmentOffsetInCentimeters" class="member-name-link"><code>segmentOffsetInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Offset from start of segment in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">`SegmentReference`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#segmentReference" class="member-name-link"><code>segmentReference</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Reference to the current segment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#speedInMetersPerSecond" class="member-name-link"><code>speedInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Speed in meters per second.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#timestamp" class="member-name-link"><code>timestamp</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Timestamp of the map matched position.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      MapMatchedLocation ( GeoCoordinates coordinates, Double bearingInDegrees)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-coordinates" class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The geographic coordinates of the map-matched location.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-bearingInDegrees" class="section detail">

    ### bearingInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingInDegrees</span>

    </div>

    <div class="block">

    The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it's equal to 0, for northeast it's equal to 45, for east it's equal to 90, and so on. If it cannot be determined, the value is null . Otherwise, it is guaranteed to be in the range \<a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">0, 360).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-segmentReference" class="section detail">

    ### segmentReference

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[SegmentReference</a></span> <span class="element-name">segmentReference</span>

    </div>

    <div class="block">

    Reference to the current segment. The ratio of segmentOffsetInCentimeters to the segment length is between SegmentReference.offsetStart and SegmentReference.offsetEnd .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-segmentOffsetInCentimeters" class="section detail">

    ### segmentOffsetInCentimeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">segmentOffsetInCentimeters</span>

    </div>

    <div class="block">

    Offset from start of segment in centimeters.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-confidence" class="section detail">

    ### confidence

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">confidence</span>

    </div>

    <div class="block">

    Confidence level (between 0 and 1) of the matched location. A low confidence value means that the map-matched vehicle location is not reliable and it may not be clear which part of the road the vehicle has taken. This can happen when the accuracy or frequency of the provided location updates is poor. If the confidence level is too small then, for example, overspeed warnings may be also inaccurate.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isDrivingInTheWrongWay" class="section detail">

    ### isDrivingInTheWrongWay

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingInTheWrongWay</span>

    </div>

    <div class="block">

    Determines if the travel direction on a one-way street is against the allowed traffic direction. For two-way streets, this value is always false . This feature is supported in tracking mode and when deviating from a route. Note that the travel direction is determined based on the map-matched location.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-horizontalAccuracyInMeters" class="section detail">

    ### horizontalAccuracyInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">horizontalAccuracyInMeters</span>

    </div>

    <div class="block">

    Horizontal accuracy measure of location. Estimated based on accuracy of input location and confidence of this map-matched location. Currently this value is not being provided by the Navigator.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-speedInMetersPerSecond" class="section detail">

    ### speedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedInMetersPerSecond</span>

    </div>

    <div class="block">

    Speed in meters per second. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timestamp" class="section detail">

    ### timestamp

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">timestamp</span>

    </div>

    <div class="block">

    Timestamp of the map matched position. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoCoordinates-java-lang-Double" class="section detail">

    ### MapMatchedLocation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMatchedLocation</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> bearingInDegrees)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the map-matched location.

    `bearingInDegrees` -

    The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it's equal to 0, for northeast it's equal to 45, for east it's equal to 90, and so on. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \[0, 360).

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

