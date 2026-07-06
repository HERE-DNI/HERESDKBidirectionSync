---
title: "Waypoint (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-waypoint"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.Waypoint

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Waypoint</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a waypoint, used as input for route calculation.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#chargingStop" class="member-name-link"><code>chargingStop</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies of a user-planned charging stop.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#coordinates" class="member-name-link"><code>coordinates</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The waypoint's geographic coordinates.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#currentWeightChangeInKilograms" class="member-name-link"><code>currentWeightChangeInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Changes the value of vehicle\[currentWeight\] by this value.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#displayLocation" class="member-name-link"><code>displayLocation</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional coordinates to indicate physical location of the Points of
  Interest (PoI).

  </div>

  </div>

  <div class="col-first even-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#duration" class="member-name-link"><code>duration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The duration in seconds that should be spent at a waypoint of type
  WaypointType.STOPOVER .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#headingInDegrees" class="member-name-link"><code>headingInDegrees</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional heading angle referenced by true North, clockwise specifying
  the direction of travel.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`MatchSideOfStreet`](sdk-for-android-explore-com-here-sdk-routing-matchsideofstreet "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#matchSideOfStreet" class="member-name-link"><code>matchSideOfStreet</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies how the location set by sideOfStreetHint should be handled.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#minCourseDistanceInMeters" class="member-name-link"><code>minCourseDistanceInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional distance in meters during which the user wants to avoid
  taking actions.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#nameHint" class="member-name-link"><code>nameHint</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional name hint causes the router to look for the place with the
  most similar name.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#onRoadThresholdInMeters" class="member-name-link"><code>onRoadThresholdInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional threshold allows specifying a distance within which the
  waypoint could be considered as being on a
  highway/bridge/tunnel/sliproad.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`SegmentReference`](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#segmentHint" class="member-name-link"><code>segmentHint</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional segment hint causes the router to try and match to the
  specified segment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#sideOfStreetHint" class="member-name-link"><code>sideOfStreetHint</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional coordinates to indicate which side of the street should be
  used to reach the waypoint.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#transitRadiusInMeters" class="member-name-link"><code>transitRadiusInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The maximum allowed distance from the waypoint that the calculated
  route may pass through.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`WaypointType`](sdk-for-android-explore-com-here-sdk-routing-waypointtype "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines how a waypoint should be considered for route calculation.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      Waypoint(GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Waypoint(GeoCoordinates coordinates,
       WaypointType type,
       int transitRadiusInMeters,
       Double headingInDegrees,
       GeoCoordinates sideOfStreetHint,
       Integer minCourseDistanceInMeters,
       Duration duration)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Waypoint(GeoCoordinates coordinates,
       WaypointType type,
       int transitRadiusInMeters,
       Double headingInDegrees,
       GeoCoordinates sideOfStreetHint,
       Integer minCourseDistanceInMeters,
       String nameHint,
       Duration duration)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

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

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-coordinates"
    class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The waypoint's geographic coordinates.

    </div>

    </div>

  - <div id="sdk-for-android-explore-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[WaypointType](sdk-for-android-explore-com-here-sdk-routing-waypointtype "enum class in com.here.sdk.routing")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Defines how a waypoint should be considered for route calculation.
    The default waypoint type is WaypointType.STOPOVER .

    </div>

    </div>

  - <div id="sdk-for-android-explore-transitRadiusInMeters"
    class="section detail">

    ### transitRadiusInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">transitRadiusInMeters</span>

    </div>

    <div class="block">

    The maximum allowed distance from the waypoint that the calculated
    route may pass through. For example, to drive past a city without
    necessarily going into the city center, you can specify the
    coordinates of the center and a transit radius of 5000m. The default
    transit radius is zero. If the route should pass the waypoint as
    close as possible, the default value should be kept. Note that the
    waypoint will be map-matched to a road. Non-zero values allow a
    greater tolerance. Note that sideOfStreetHint option is ignored if
    the user sets this option with a value greater than zero.

    </div>

    </div>

  - <div id="sdk-for-android-explore-headingInDegrees"
    class="section detail">

    ### headingInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">headingInDegrees</span>

    </div>

    <div class="block">

    Optional heading angle referenced by true North, clockwise
    specifying the direction of travel. The heading direction may help
    the routing algorithm to select the best direction, for example,
    when multiple directions are possible at a road junction. North is 0
    degrees, East is 90 degrees, South is 180 degrees, and West is 270
    degrees. The value must be in the range \[0, 360\] when specified.
    By default, or when null is set, heading is ignored for route
    calculation.

    </div>

    </div>

  - <div id="sdk-for-android-explore-sideOfStreetHint"
    class="section detail">

    ### sideOfStreetHint

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">sideOfStreetHint</span>

    </div>

    <div class="block">

    Optional coordinates to indicate which side of the street should be
    used to reach the waypoint. For example, if the location is to the
    left of the street, the router will prefer using that side in case
    the street has dividers. Note that this option is ignored if the
    user sets transitRadiusInMeters option with a value greater than
    zero.

    </div>

    </div>

  - <div id="sdk-for-android-explore-displayLocation"
    class="section detail">

    ### displayLocation

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">displayLocation</span>

    </div>

    <div class="block">

    Optional coordinates to indicate physical location of the Points of
    Interest (PoI). It is different from coordinates and
    sideOfStreetHint which are generally expected to to be on the
    navigable road network and can be different from actual location of
    the PoI. display_location is used for visualization of the PoI
    regardless of road network.

    </div>

    </div>

  - <div id="sdk-for-android-explore-minCourseDistanceInMeters"
    class="section detail">

    ### minCourseDistanceInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">minCourseDistanceInMeters</span>

    </div>

    <div class="block">

    Optional distance in meters during which the user wants to avoid
    taking actions. For example, if the origin is set by a moving
    vehicle, the user might not have time to react to immediate actions
    such as a sharp right turn.

    </div>

    </div>

  - <div id="sdk-for-android-explore-nameHint" class="section detail">

    ### nameHint

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">nameHint</span>

    </div>

    <div class="block">

    Optional name hint causes the router to look for the place with the
    most similar name. This can e.g. include things like: North being
    used to differentiate between interstates I66 North and I66 South ,
    Downtown Avenue being used to correctly select a residential street.

    </div>

    </div>

  - <div id="sdk-for-android-explore-matchSideOfStreet"
    class="section detail">

    ### matchSideOfStreet

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[MatchSideOfStreet](sdk-for-android-explore-com-here-sdk-routing-matchsideofstreet "enum class in com.here.sdk.routing")</span> <span class="element-name">matchSideOfStreet</span>

    </div>

    <div class="block">

    Specifies how the location set by sideOfStreetHint should be
    handled. Note that this setting might affect the geometry of the
    resulting route.

    </div>

    </div>

  - <div id="sdk-for-android-explore-duration" class="section detail">

    ### duration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">duration</span>

    </div>

    <div class="block">

    The duration in seconds that should be spent at a waypoint of type
    WaypointType.STOPOVER . Impacts time-aware calculations. Ignored for
    waypoints of type WaypointType.PASS_THROUGH . The default duration
    is 0 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-segmentHint"
    class="section detail">

    ### segmentHint

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")</span> <span class="element-name">segmentHint</span>

    </div>

    <div class="block">

    Optional segment hint causes the router to try and match to the
    specified segment. Waypoint coordinates need to be on the segment,
    otherwise waypoint will be matched ignoring the segment hint. This
    parameter can be used when the waypoint is too close to more than
    one segment to force matching to a specific one. Only topology
    segment id and travel direction are used to define the segment hint
    Note: The feature is not supported by the OfflineRoutingEngine .

    </div>

    </div>

  - <div id="sdk-for-android-explore-onRoadThresholdInMeters"
    class="section detail">

    ### onRoadThresholdInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">onRoadThresholdInMeters</span>

    </div>

    <div class="block">

    Optional threshold allows specifying a distance within which the
    waypoint could be considered as being on a
    highway/bridge/tunnel/sliproad. Within this threshold, the
    attributes of the segments do not impact the matching. Outside the
    threshold only segments which aren't one of
    highway/bridge/tunnel/sliproad can be matched.

    </div>

    </div>

  - <div id="sdk-for-android-explore-chargingStop"
    class="section detail">

    ### chargingStop

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ChargingStop](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing")</span> <span class="element-name">chargingStop</span>

    </div>

    <div class="block">

    Specifies of a user-planned charging stop. The resulting Route may
    contain this waypoint as a RoutePlace with a non-null
    ChargingStation member when the provided specifications indicate
    that a stop is required to charge the EV battery. Note: If
    \[EVCarOptions.ensure_reachability\] is not set as true and
    \[ChargingStop.min_duration\] is not provided, route calculation may
    suggest a better charging stop instead of this stop.

    </div>

    </div>

  - <div id="sdk-for-android-explore-currentWeightChangeInKilograms"
    class="section detail">

    ### currentWeightChangeInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">currentWeightChangeInKilograms</span>

    </div>

    <div class="block">

    Changes the value of vehicle\[currentWeight\] by this value. Enables
    the support of scenarios where the vehicle takes additional cargo or
    unloads its cargo along the route. Changes to the configuration of
    the vehicle, such as adding a trailer, aren't supported. Relative
    value in kilograms. Available range: from -40000 to 40000
    (inclusive). Note: A route request with this parameter requires to
    set VehicleSpecification.currentWeightInKilograms and
    VehicleSpecification.grossWeightInKilograms . This feature is
    supported in transport modes of TransportMode.CAR ,
    TransportMode.TAXI , or TransportMode.TRUCK . Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### Waypoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Waypoint</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The waypoint's geographic coordinates.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,com.here.time.Duration)"
    class="section detail">

    ### Waypoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Waypoint</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [WaypointType](sdk-for-android-explore-com-here-sdk-routing-waypointtype "enum class in com.here.sdk.routing") type,
    int transitRadiusInMeters, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> headingInDegrees,
    @Nullable
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") sideOfStreetHint,
    @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
    @NonNull
    [Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") duration)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The waypoint's geographic coordinates.

    `type` -

    Defines how a waypoint should be considered for route calculation.
    The default waypoint type is
    [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `transitRadiusInMeters` -

    The maximum allowed distance from the waypoint that the calculated
    route may pass through. For example, to drive past a city without
    necessarily going into the city center, you can specify the
    coordinates of the center and a transit radius of 5000m. The default
    transit radius is zero. If the route should pass the waypoint as
    close as possible, the default value should be kept. Note that the
    waypoint will be map-matched to a road. Non-zero values allow a
    greater tolerance. Note that
    [`sideOfStreetHint`](sdk-for-android-explore-com-here-sdk-routing-waypoint#sideOfStreetHint)
    option is ignored if the user sets this option with a value greater
    than zero.

    `headingInDegrees` -

    Optional heading angle referenced by true North, clockwise
    specifying the direction of travel. The heading direction may help
    the routing algorithm to select the best direction, for example,
    when multiple directions are possible at a road junction. North is 0
    degrees, East is 90 degrees, South is 180 degrees, and West is 270
    degrees. The value must be in the range \[0, 360\] when specified.
    By default, or when `null` is set, heading is ignored for route
    calculation.

    `sideOfStreetHint` -

    Optional coordinates to indicate which side of the street should be
    used to reach the waypoint. For example, if the location is to the
    left of the street, the router will prefer using that side in case
    the street has dividers. Note that this option is ignored if the
    user sets
    [`transitRadiusInMeters`](sdk-for-android-explore-com-here-sdk-routing-waypoint#transitRadiusInMeters)
    option with a value greater than zero.

    `minCourseDistanceInMeters` -

    Optional distance in meters during which the user wants to avoid
    taking actions. For example, if the origin is set by a moving
    vehicle, the user might not have time to react to immediate actions
    such as a sharp right turn.

    `duration` -

    The duration in seconds that should be spent at a waypoint of type
    [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).
    Impacts time-aware calculations. Ignored for waypoints of type
    [`WaypointType.PASS_THROUGH`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#PASS_THROUGH).
    The default duration is 0 seconds.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,java.lang.String,com.here.time.Duration)"
    class="section detail">

    ### Waypoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Waypoint</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [WaypointType](sdk-for-android-explore-com-here-sdk-routing-waypointtype "enum class in com.here.sdk.routing") type,
    int transitRadiusInMeters, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> headingInDegrees,
    @Nullable
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") sideOfStreetHint,
    @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
    @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> nameHint,
    @NonNull
    [Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") duration)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The waypoint's geographic coordinates.

    `type` -

    Defines how a waypoint should be considered for route calculation.
    The default waypoint type is
    [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `transitRadiusInMeters` -

    The maximum allowed distance from the waypoint that the calculated
    route may pass through. For example, to drive past a city without
    necessarily going into the city center, you can specify the
    coordinates of the center and a transit radius of 5000m. The default
    transit radius is zero. If the route should pass the waypoint as
    close as possible, the default value should be kept. Note that the
    waypoint will be map-matched to a road. Non-zero values allow a
    greater tolerance. Note that
    [`sideOfStreetHint`](sdk-for-android-explore-com-here-sdk-routing-waypoint#sideOfStreetHint)
    option is ignored if the user sets this option with a value greater
    than zero.

    `headingInDegrees` -

    Optional heading angle referenced by true North, clockwise
    specifying the direction of travel. The heading direction may help
    the routing algorithm to select the best direction, for example,
    when multiple directions are possible at a road junction. North is 0
    degrees, East is 90 degrees, South is 180 degrees, and West is 270
    degrees. The value must be in the range \[0, 360\] when specified.
    By default, or when `null` is set, heading is ignored for route
    calculation.

    `sideOfStreetHint` -

    Optional coordinates to indicate which side of the street should be
    used to reach the waypoint. For example, if the location is to the
    left of the street, the router will prefer using that side in case
    the street has dividers. Note that this option is ignored if the
    user sets
    [`transitRadiusInMeters`](sdk-for-android-explore-com-here-sdk-routing-waypoint#transitRadiusInMeters)
    option with a value greater than zero.

    `minCourseDistanceInMeters` -

    Optional distance in meters during which the user wants to avoid
    taking actions. For example, if the origin is set by a moving
    vehicle, the user might not have time to react to immediate actions
    such as a sharp right turn.

    `nameHint` -

    Optional name hint causes the router to look for the place with the
    most similar name. This can e.g. include things like: `North` being
    used to differentiate between interstates `I66 North` and
    `I66 South, Downtown Avenue` being used to correctly select a
    residential street.

    `duration` -

    The duration in seconds that should be spent at a waypoint of type
    [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).
    Impacts time-aware calculations. Ignored for waypoints of type
    [`WaypointType.PASS_THROUGH`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#PASS_THROUGH).
    The default duration is 0 seconds.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

