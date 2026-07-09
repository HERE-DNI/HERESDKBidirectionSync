---
title: "ViolatedRestriction.Details (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.ViolatedRestriction.Details → com.here.sdk.routing.ViolatedRestriction.Details

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">ViolatedRestriction.Details</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member max_height_in_centimeters will be set with the maximum allowed height value.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenAxleCount" class="member-name-link"><code>forbiddenAxleCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The restriction to trucks with axles number within specified range during the trip.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">`HazardousMaterial`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenHazardousGoods" class="member-name-link"><code>forbiddenHazardousGoods</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using VehicleSpecification.hazardousMaterials from TransportSpecification.vehicleSpecification from RoutingOptions.transportSpecification .

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTrailerCount" class="member-name-link"><code>forbiddenTrailerCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constrains the restriction to trucks with number of trailer within specified range during the trip.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">`TruckCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckCategory" class="member-name-link"><code>forbiddenTruckCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  This property will be set if a restriction applies to the value of TruckCategory parameter used for route calculation.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">`TruckRoadType`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckRoadTypes" class="member-name-link"><code>forbiddenTruckRoadTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Contains violated restrictions for truck road types.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">`TruckType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckType" class="member-name-link"><code>forbiddenTruckType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.27.0.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxHeightInCentimeters" class="member-name-link"><code>maxHeightInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Max permitted height during the trip, in centimeters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxKingpinToRearAxleDistanceInCentimeters" class="member-name-link"><code>maxKingpinToRearAxleDistanceInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Contains the maximum permitted distance from kingpin to the rear axle in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxLengthInCentimeters" class="member-name-link"><code>maxLengthInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Max permitted length during the trip, in centimeters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxNumberOfTires" class="member-name-link"><code>maxNumberOfTires</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Contains the maximum permitted number of tires.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxPayloadCapacityInKilograms" class="member-name-link"><code>maxPayloadCapacityInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Max permitted payload capacity during the trip, in kilograms.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">`TunnelCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxTunnelCategory" class="member-name-link"><code>maxTunnelCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Tunnel category to restrict transport of specific goods during the trip.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">`VehicleRestrictionMaxWeight`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeight" class="member-name-link"><code>maxWeight</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-maxaxlegroupweight" title="class in com.here.sdk.routing">`MaxAxleGroupWeight`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeightPerAxleGroupInKilograms" class="member-name-link"><code>maxWeightPerAxleGroupInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Max permitted weight per axle group during the trip, in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeightPerAxleInKilograms" class="member-name-link"><code>maxWeightPerAxleInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Max permitted weight per axle during the trip, in kilograms.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWidthInCentimeters" class="member-name-link"><code>maxWidthInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Max permitted width during the trip, in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#routingZoneReference" class="member-name-link"><code>routingZoneReference</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Contains the restricted routing zone reference This property will be set if the AvoidanceOptions.zoneCategories is not empty

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">`TimeRule`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#timeRule" class="member-name-link"><code>timeRule</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Time intervals during which restrictions are enforced.

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

      Details ()

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

  - <div id="sdk-for-android-navigate-maxWeightPerAxleInKilograms" class="section detail">

    ### maxWeightPerAxleInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxWeightPerAxleInKilograms</span>

    </div>

    <div class="block">

    Max permitted weight per axle during the trip, in kilograms. This property will be set if the VehicleSpecification.weightPerAxleInKilograms exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxWeightPerAxleGroupInKilograms" class="section detail">

    ### maxWeightPerAxleGroupInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></span> <span class="element-name">maxWeightPerAxleGroupInKilograms</span>

    </div>

    <div class="block">

    Max permitted weight per axle group during the trip, in kilograms. This property will be set if the VehicleSpecification.weightPerAxleGroup exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxHeightInCentimeters" class="section detail">

    ### maxHeightInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxHeightInCentimeters</span>

    </div>

    <div class="block">

    Max permitted height during the trip, in centimeters. This property will be set if the VehicleSpecification.heightInCentimeters exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxWidthInCentimeters" class="section detail">

    ### maxWidthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxWidthInCentimeters</span>

    </div>

    <div class="block">

    Max permitted width during the trip, in centimeters. This property will be set if the VehicleSpecification.widthInCentimeters exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxLengthInCentimeters" class="section detail">

    ### maxLengthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxLengthInCentimeters</span>

    </div>

    <div class="block">

    Max permitted length during the trip, in centimeters. This property will be set if the VehicleSpecification.lengthInCentimeters exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenAxleCount" class="section detail">

    ### forbiddenAxleCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">forbiddenAxleCount</span>

    </div>

    <div class="block">

    The restriction to trucks with axles number within specified range during the trip. This property will be set if the VehicleSpecification.axleCount is within this range.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenTrailerCount" class="section detail">

    ### forbiddenTrailerCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">forbiddenTrailerCount</span>

    </div>

    <div class="block">

    Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the VehicleSpecification.trailerCount is within this range.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenHazardousGoods" class="section detail">

    ### forbiddenHazardousGoods

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>\></span> <span class="element-name">forbiddenHazardousGoods</span>

    </div>

    <div class="block">

    There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using VehicleSpecification.hazardousMaterials from TransportSpecification.vehicleSpecification from RoutingOptions.transportSpecification . This property is the intersection of the two lists. Note RoadSignWarning events and RouteViolations are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxTunnelCategory" class="section detail">

    ### maxTunnelCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span class="element-name">maxTunnelCategory</span>

    </div>

    <div class="block">

    Tunnel category to restrict transport of specific goods during the trip. This property will be set if the VehicleSpecification.tunnelCategory from TransportSpecification.vehicleSpecification from RoutingOptions.transportSpecification exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenTruckType" class="section detail">

    ### forbiddenTruckType

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span class="element-name">forbiddenTruckType</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Use `forbidden_truck_category` instead.

    </div>

    </div>

    <div class="block">

    This property will be set if a restriction applies to the value of TruckType parameter used for route calculation.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenTruckCategory" class="section detail">

    ### forbiddenTruckCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span class="element-name">forbiddenTruckCategory</span>

    </div>

    <div class="block">

    This property will be set if a restriction applies to the value of TruckCategory parameter used for route calculation.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-forbiddenTruckRoadTypes" class="section detail">

    ### forbiddenTruckRoadTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>\></span> <span class="element-name">forbiddenTruckRoadTypes</span>

    </div>

    <div class="block">

    Contains violated restrictions for truck road types.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-routingZoneReference" class="section detail">

    ### routingZoneReference

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">routingZoneReference</span>

    </div>

    <div class="block">

    Contains the restricted routing zone reference This property will be set if the AvoidanceOptions.zoneCategories is not empty

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxPayloadCapacityInKilograms" class="section detail">

    ### maxPayloadCapacityInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxPayloadCapacityInKilograms</span>

    </div>

    <div class="block">

    Max permitted payload capacity during the trip, in kilograms. This property will be set if the VehicleSpecification.payloadCapacityInKilograms exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeRule" class="section detail">

    ### timeRule

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span>

    </div>

    <div class="block">

    Time intervals during which restrictions are enforced.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxWeight" class="section detail">

    ### maxWeight

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></span> <span class="element-name">maxWeight</span>

    </div>

    <div class="block">

    Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the VehicleSpecification.grossWeightInKilograms parameter used for route calculation exceeds this value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxNumberOfTires" class="section detail">

    ### maxNumberOfTires

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxNumberOfTires</span>

    </div>

    <div class="block">

    Contains the maximum permitted number of tires. This property will be set if the VehicleSpecification.tiresCount exceeds the specified value.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxKingpinToRearAxleDistanceInCentimeters" class="section detail">

    ### maxKingpinToRearAxleDistanceInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxKingpinToRearAxleDistanceInCentimeters</span>

    </div>

    <div class="block">

    Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the VehicleSpecification.kingpinToRearAxleDistanceInCentimeters exceeds the specified value.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

