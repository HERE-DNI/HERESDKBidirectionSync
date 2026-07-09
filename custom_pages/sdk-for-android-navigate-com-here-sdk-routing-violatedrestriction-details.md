---
title: "ViolatedRestriction.Details (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ViolatedRestriction.Details.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.ViolatedRestriction.Details</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">ViolatedRestriction.Details</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.
 For example, if the vehicle violates the maximum allowed height during the trip, then the member <code>max_height_in_centimeters</code> will
 be set with the maximum allowed height value.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenAxleCount">forbiddenAxleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">The restriction to trucks with axles number within specified range during the trip.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenHazardousGoods">forbiddenHazardousGoods</a></code></div>
<div className="col-last odd-row-color">
<div className="block">There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
 for the route calculation provided using <a href="sdk-for-android-navigate-vehiclespecification#hazardousMaterials"><code>VehicleSpecification.hazardousMaterials</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTrailerCount">forbiddenTrailerCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">Constrains the restriction to trucks with number of trailer within specified range during the trip.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckCategory">forbiddenTruckCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a>
 parameter used for route calculation.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckRoadTypes">forbiddenTruckRoadTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Contains violated restrictions for truck road types.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#forbiddenTruckType">forbiddenTruckType</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxHeightInCentimeters">maxHeightInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max permitted height during the trip, in centimeters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxKingpinToRearAxleDistanceInCentimeters">maxKingpinToRearAxleDistanceInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Contains the maximum permitted distance from kingpin to the rear axle in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxLengthInCentimeters">maxLengthInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max permitted length during the trip, in centimeters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxNumberOfTires">maxNumberOfTires</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Contains the maximum permitted number of tires.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxPayloadCapacityInKilograms">maxPayloadCapacityInKilograms</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max permitted payload capacity during the trip, in kilograms.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxTunnelCategory">maxTunnelCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Tunnel category to restrict transport of specific goods during the trip.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeight">maxWeight</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeightPerAxleGroupInKilograms">maxWeightPerAxleGroupInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Max permitted weight per axle group during the trip, in kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWeightPerAxleInKilograms">maxWeightPerAxleInKilograms</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max permitted weight per axle during the trip, in kilograms.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#maxWidthInCentimeters">maxWidthInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Max permitted width during the trip, in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#routingZoneReference">routingZoneReference</a></code></div>
<div className="col-last even-row-color">
<div className="block">Contains the restricted routing zone reference
 This property will be set if the <a href="sdk-for-android-navigate-avoidanceoptions#zoneCategories"><code>AvoidanceOptions.zoneCategories</code></a> is not empty</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#timeRule">timeRule</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Time intervals during which restrictions are enforced.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details#%3Cinit%3E()">Details</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="maxWeightPerAxleInKilograms">
<h3>maxWeightPerAxleInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxWeightPerAxleInKilograms</span></div>
<div className="block"><p>Max permitted weight per axle during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#weightPerAxleInKilograms"><code>VehicleSpecification.weightPerAxleInKilograms</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxWeightPerAxleGroupInKilograms">
<h3>maxWeightPerAxleGroupInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></span> <span className="element-name">maxWeightPerAxleGroupInKilograms</span></div>
<div className="block"><p>Max permitted weight per axle group during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#weightPerAxleGroup"><code>VehicleSpecification.weightPerAxleGroup</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxHeightInCentimeters">
<h3>maxHeightInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxHeightInCentimeters</span></div>
<div className="block"><p>Max permitted height during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxWidthInCentimeters">
<h3>maxWidthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxWidthInCentimeters</span></div>
<div className="block"><p>Max permitted width during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxLengthInCentimeters">
<h3>maxLengthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxLengthInCentimeters</span></div>
<div className="block"><p>Max permitted length during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenAxleCount">
<h3>forbiddenAxleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">forbiddenAxleCount</span></div>
<div className="block"><p>The restriction to trucks with axles number within specified range during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#axleCount"><code>VehicleSpecification.axleCount</code></a>
 is within this range.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenTrailerCount">
<h3>forbiddenTrailerCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">forbiddenTrailerCount</span></div>
<div className="block"><p>Constrains the restriction to trucks with number of trailer within specified range during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#trailerCount"><code>VehicleSpecification.trailerCount</code></a>
 is within this range.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenHazardousGoods">
<h3>forbiddenHazardousGoods</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span className="element-name">forbiddenHazardousGoods</span></div>
<div className="block"><p>There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
 for the route calculation provided using <a href="sdk-for-android-navigate-vehiclespecification#hazardousMaterials"><code>VehicleSpecification.hazardousMaterials</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>.
 This property is the intersection of the two lists.
 <strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
 indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxTunnelCategory">
<h3>maxTunnelCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span className="element-name">maxTunnelCategory</span></div>
<div className="block"><p>Tunnel category to restrict transport of specific goods during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#tunnelCategory"><code>VehicleSpecification.tunnelCategory</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenTruckType">
<h3>forbiddenTruckType</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span className="element-name">forbiddenTruckType</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0. Use <code>forbidden_truck_category</code> instead.</p></div>
</div>
<div className="block"><p>This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport"><code>TruckType</code></a>
 parameter used for route calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenTruckCategory">
<h3>forbiddenTruckCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span className="element-name">forbiddenTruckCategory</span></div>
<div className="block"><p>This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a>
 parameter used for route calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="forbiddenTruckRoadTypes">
<h3>forbiddenTruckRoadTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</span> <span className="element-name">forbiddenTruckRoadTypes</span></div>
<div className="block"><p>Contains violated restrictions for truck road types.</p></div>
</section>
</li>
<li>
<section className="detail" id="routingZoneReference">
<h3>routingZoneReference</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">routingZoneReference</span></div>
<div className="block"><p>Contains the restricted routing zone reference
 This property will be set if the <a href="sdk-for-android-navigate-avoidanceoptions#zoneCategories"><code>AvoidanceOptions.zoneCategories</code></a> is not empty</p></div>
</section>
</li>
<li>
<section className="detail" id="maxPayloadCapacityInKilograms">
<h3>maxPayloadCapacityInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxPayloadCapacityInKilograms</span></div>
<div className="block"><p>Max permitted payload capacity during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#payloadCapacityInKilograms"><code>VehicleSpecification.payloadCapacityInKilograms</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="timeRule">
<h3>timeRule</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span className="element-name">timeRule</span></div>
<div className="block"><p>Time intervals during which restrictions are enforced.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxWeight">
<h3>maxWeight</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></span> <span className="element-name">maxWeight</span></div>
<div className="block"><p>Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>
 parameter used for route calculation exceeds this value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxNumberOfTires">
<h3>maxNumberOfTires</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxNumberOfTires</span></div>
<div className="block"><p>Contains the maximum permitted number of tires.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#tiresCount"><code>VehicleSpecification.tiresCount</code></a> exceeds the specified value.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxKingpinToRearAxleDistanceInCentimeters">
<h3>maxKingpinToRearAxleDistanceInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxKingpinToRearAxleDistanceInCentimeters</span></div>
<div className="block"><p>Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
 This property will be set if the
 <a href="sdk-for-android-navigate-vehiclespecification#kingpinToRearAxleDistanceInCentimeters"><code>VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</code></a>
 exceeds the specified value.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
