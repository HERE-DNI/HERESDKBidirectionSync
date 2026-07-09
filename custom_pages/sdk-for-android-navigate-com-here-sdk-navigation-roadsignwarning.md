---
title: "RoadSignWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.RoadSignWarning → com.here.sdk.navigation.RoadSignWarning

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoadSignWarning</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A road sign. The main field describing the sign is type . Some road types are standardized, others can be country specific. A valid road sign contains known type or category . Use RoadSignWarningListener to get notifications with current road signs.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">`RoadSignCategory`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#category" class="member-name-link"><code>category</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The main category to which the road sign belongs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceToRoadSignInMeters" class="member-name-link"><code>distanceToRoadSignInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Distance to the road sign in meters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">`DistanceType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceType" class="member-name-link"><code>distanceType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The distance type for the warning, e.g.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#duration" class="member-name-link"><code>duration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional length information during which the warning is applicable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">`GeneralWarningRoadSignType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#generalWarningType" class="member-name-link"><code>generalWarningType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies the general warning to which the road sign belongs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#id" class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Unique identifier for this specific road sign warning instance.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#isPrioritySign" class="member-name-link"><code>isPrioritySign</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Flag indicating if the road sign is a priority sign.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#preWarning" class="member-name-link"><code>preWarning</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional pre-warning in terms of distance, of the upcoming warning or regulation.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">`SegmentReference`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#roadSignSegment" class="member-name-link"><code>roadSignSegment</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The reference to the segment where the road sign is located.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#signValue" class="member-name-link"><code>signValue</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">`RoadSignType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Type of the road sign.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#validityTime" class="member-name-link"><code>validityTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">`RoadSignVehicleType`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#vehicleTypes" class="member-name-link"><code>vehicleTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies a list of vehicle types for which the road sign is applicable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">`WeatherType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#weatherType" class="member-name-link"><code>weatherType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies the weather type for which the sign is applicable.

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

      RoadSignWarning (double distanceToRoadSignInMeters, RoadSignType type, RoadSignCategory category, GeneralWarningRoadSignType generalWarningType,
       boolean isPrioritySign, List < RoadSignVehicleType > vehicleTypes, WeatherType weatherType, SegmentReference roadSignSegment, DistanceType distanceType)

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

  - <div id="sdk-for-android-navigate-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Unique identifier for this specific road sign warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceToRoadSignInMeters" class="section detail">

    ### distanceToRoadSignInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToRoadSignInMeters</span>

    </div>

    <div class="block">

    Distance to the road sign in meters.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Type of the road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-category" class="section detail">

    ### category

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span class="element-name">category</span>

    </div>

    <div class="block">

    The main category to which the road sign belongs.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-generalWarningType" class="section detail">

    ### generalWarningType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span class="element-name">generalWarningType</span>

    </div>

    <div class="block">

    Specifies the general warning to which the road sign belongs.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isPrioritySign" class="section detail">

    ### isPrioritySign

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrioritySign</span>

    </div>

    <div class="block">

    Flag indicating if the road sign is a priority sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-vehicleTypes" class="section detail">

    ### vehicleTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>\></span> <span class="element-name">vehicleTypes</span>

    </div>

    <div class="block">

    Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-weatherType" class="section detail">

    ### weatherType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weatherType</span>

    </div>

    <div class="block">

    Specifies the weather type for which the sign is applicable. If weather type is WeatherType.UNKNOWN , the sign is actual for all weather types.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-signValue" class="section detail">

    ### signValue

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">signValue</span>

    </div>

    <div class="block">

    Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-preWarning" class="section detail">

    ### preWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">preWarning</span>

    </div>

    <div class="block">

    Optional pre-warning in terms of distance, of the upcoming warning or regulation. The pre-warning information is given as printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-duration" class="section detail">

    ### duration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">duration</span>

    </div>

    <div class="block">

    Optional length information during which the warning is applicable. Usually, this information is shown on a separate shield below the main shield. For example, a sign may warn on playing children for a length of 100 m, starting from the location of the warning sign. The length information (most likely with units) is given as printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-validityTime" class="section detail">

    ### validityTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">validityTime</span>

    </div>

    <div class="block">

    Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable. The time information is given as printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-roadSignSegment" class="section detail">

    ### roadSignSegment

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">roadSignSegment</span>

    </div>

    <div class="block">

    The reference to the segment where the road sign is located. It can be used to identify the location of the road sign. It allows to compare the road sign location with the MapMatchedLocation.segment_reference provided by the NavigableLocationListener or with the Span.getSegmentReference() available in the Route's Span. By combining it with the geometry of the segment, that can be loaded using SegmentDataLoader , it is possible to identify the road sign's coordinates.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceType" class="section detail">

    ### distanceType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span>

    </div>

    <div class="block">

    The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for passing a road sign. Since the road sign warning is given relative to a single position on the route, DistanceType.REACHED will never be given for this warning.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-com-here-sdk-navigation-RoadSignType-com-here-sdk-navigation-RoadSignCategory-com-here-sdk-navigation-GeneralWarningRoadSignType-boolean-java-util-List-com-here-sdk-navigation-WeatherType-com-here-sdk-routing-SegmentReference-com-here-sdk-navigation-DistanceType" class="section detail">

    ### RoadSignWarning

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoadSignWarning</span><wbr></wbr><span class="parameters">(double distanceToRoadSignInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> type, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> category, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType, boolean isPrioritySign, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>\> vehicleTypes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> roadSignSegment, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `distanceToRoadSignInMeters` -

    Distance to the road sign in meters.

    `type` -

    Type of the road sign.

    `category` -

    The main category to which the road sign belongs.

    `generalWarningType` -

    Specifies the general warning to which the road sign belongs.

    `isPrioritySign` -

    Flag indicating if the road sign is a priority sign.

    `vehicleTypes` -

    Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

    `weatherType` -

    Specifies the weather type for which the sign is applicable. If weather type is `WeatherType.UNKNOWN`, the sign is actual for all weather types.

    `roadSignSegment` -

    The reference to the segment where the road sign is located. It can be used to identify the location of the road sign. It allows to compare the road sign location with the `MapMatchedLocation.segment_reference` provided by the `NavigableLocationListener` or with the [](sdk-for-android-navigate-com-here-sdk-routing-span#getSegmentReference())

        Span.getSegmentReference()

    </a> available in the Route's Span. By combining it with the geometry of the segment, that can be loaded using <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader" title="class in com.here.sdk.mapdata">`SegmentDataLoader`</a>, it is possible to identify the road sign's coordinates.

    </p>

    `distanceType` -

    The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for passing a road sign. Since the road sign warning is given relative to a single position on the route, <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype#REACHED">`DistanceType.REACHED`</a> will never be given for this warning.

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

