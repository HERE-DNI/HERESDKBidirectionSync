---
title: "ViolatedRestriction.Details (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction-details"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ViolatedRestriction.Details.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.ViolatedRestriction.Details</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">ViolatedRestriction.Details</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.
 For example, if the vehicle violates the maximum allowed height during the trip, then the member <code>max_height_in_centimeters</code> will
 be set with the maximum allowed height value.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenAxleCount">forbiddenAxleCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">The restriction to trucks with axles number within specified range during the trip.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenHazardousGoods">forbiddenHazardousGoods</a></code></div>
<div class="col-last odd-row-color">
<div class="block">There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
 for the route calculation provided using <a href="sdk-for-android-navigate-vehiclespecification#hazardousMaterials"><code>VehicleSpecification.hazardousMaterials</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenTrailerCount">forbiddenTrailerCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constrains the restriction to trucks with number of trailer within specified range during the trip.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenTruckCategory">forbiddenTruckCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a>
 parameter used for route calculation.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenTruckRoadTypes">forbiddenTruckRoadTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains violated restrictions for truck road types.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#forbiddenTruckType">forbiddenTruckType</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxHeightInCentimeters">maxHeightInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Max permitted height during the trip, in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxKingpinToRearAxleDistanceInCentimeters">maxKingpinToRearAxleDistanceInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains the maximum permitted distance from kingpin to the rear axle in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxLengthInCentimeters">maxLengthInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Max permitted length during the trip, in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxNumberOfTires">maxNumberOfTires</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains the maximum permitted number of tires.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxPayloadCapacityInKilograms">maxPayloadCapacityInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Max permitted payload capacity during the trip, in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxTunnelCategory">maxTunnelCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tunnel category to restrict transport of specific goods during the trip.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxWeight">maxWeight</a></code></div>
<div class="col-last even-row-color">
<div class="block">Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxWeightPerAxleGroupInKilograms">maxWeightPerAxleGroupInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Max permitted weight per axle group during the trip, in kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxWeightPerAxleInKilograms">maxWeightPerAxleInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Max permitted weight per axle during the trip, in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxWidthInCentimeters">maxWidthInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Max permitted width during the trip, in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#routingZoneReference">routingZoneReference</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains the restricted routing zone reference
 This property will be set if the <a href="sdk-for-android-navigate-avoidanceoptions#zoneCategories"><code>AvoidanceOptions.zoneCategories</code></a> is not empty</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timeRule">timeRule</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Time intervals during which restrictions are enforced.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">Details</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="maxWeightPerAxleInKilograms">
<h3>maxWeightPerAxleInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxWeightPerAxleInKilograms</span></div>
<div class="block"><p>Max permitted weight per axle during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#weightPerAxleInKilograms"><code>VehicleSpecification.weightPerAxleInKilograms</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxWeightPerAxleGroupInKilograms">
<h3>maxWeightPerAxleGroupInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></span> <span class="element-name">maxWeightPerAxleGroupInKilograms</span></div>
<div class="block"><p>Max permitted weight per axle group during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#weightPerAxleGroup"><code>VehicleSpecification.weightPerAxleGroup</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxHeightInCentimeters">
<h3>maxHeightInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxHeightInCentimeters</span></div>
<div class="block"><p>Max permitted height during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxWidthInCentimeters">
<h3>maxWidthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxWidthInCentimeters</span></div>
<div class="block"><p>Max permitted width during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxLengthInCentimeters">
<h3>maxLengthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxLengthInCentimeters</span></div>
<div class="block"><p>Max permitted length during the trip, in centimeters.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenAxleCount">
<h3>forbiddenAxleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">forbiddenAxleCount</span></div>
<div class="block"><p>The restriction to trucks with axles number within specified range during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#axleCount"><code>VehicleSpecification.axleCount</code></a>
 is within this range.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenTrailerCount">
<h3>forbiddenTrailerCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">forbiddenTrailerCount</span></div>
<div class="block"><p>Constrains the restriction to trucks with number of trailer within specified range during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#trailerCount"><code>VehicleSpecification.trailerCount</code></a>
 is within this range.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenHazardousGoods">
<h3>forbiddenHazardousGoods</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span class="element-name">forbiddenHazardousGoods</span></div>
<div class="block"><p>There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
 for the route calculation provided using <a href="sdk-for-android-navigate-vehiclespecification#hazardousMaterials"><code>VehicleSpecification.hazardousMaterials</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>.
 This property is the intersection of the two lists.
 </p><p><strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
 indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxTunnelCategory">
<h3>maxTunnelCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span class="element-name">maxTunnelCategory</span></div>
<div class="block"><p>Tunnel category to restrict transport of specific goods during the trip.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#tunnelCategory"><code>VehicleSpecification.tunnelCategory</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-routingoptions#transportSpecification"><code>RoutingOptions.transportSpecification</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenTruckType">
<h3>forbiddenTruckType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span class="element-name">forbiddenTruckType</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Use <code>forbidden_truck_category</code> instead.</p></div>
</div>
<div class="block"><p>This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-trucktype" title="enum class in com.here.sdk.transport"><code>TruckType</code></a>
 parameter used for route calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenTruckCategory">
<h3>forbiddenTruckCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span class="element-name">forbiddenTruckCategory</span></div>
<div class="block"><p>This property will be set if a restriction applies to the value of <a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a>
 parameter used for route calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="forbiddenTruckRoadTypes">
<h3>forbiddenTruckRoadTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</span> <span class="element-name">forbiddenTruckRoadTypes</span></div>
<div class="block"><p>Contains violated restrictions for truck road types.</p></div>
</section>
</li>
<li>
<section class="detail" id="routingZoneReference">
<h3>routingZoneReference</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">routingZoneReference</span></div>
<div class="block"><p>Contains the restricted routing zone reference
 This property will be set if the <a href="sdk-for-android-navigate-avoidanceoptions#zoneCategories"><code>AvoidanceOptions.zoneCategories</code></a> is not empty</p></div>
</section>
</li>
<li>
<section class="detail" id="maxPayloadCapacityInKilograms">
<h3>maxPayloadCapacityInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxPayloadCapacityInKilograms</span></div>
<div class="block"><p>Max permitted payload capacity during the trip, in kilograms.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#payloadCapacityInKilograms"><code>VehicleSpecification.payloadCapacityInKilograms</code></a>
 exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeRule">
<h3>timeRule</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span></div>
<div class="block"><p>Time intervals during which restrictions are enforced.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxWeight">
<h3>maxWeight</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></span> <span class="element-name">maxWeight</span></div>
<div class="block"><p>Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>
 parameter used for route calculation exceeds this value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxNumberOfTires">
<h3>maxNumberOfTires</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxNumberOfTires</span></div>
<div class="block"><p>Contains the maximum permitted number of tires.
 This property will be set if the <a href="sdk-for-android-navigate-vehiclespecification#tiresCount"><code>VehicleSpecification.tiresCount</code></a> exceeds the specified value.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxKingpinToRearAxleDistanceInCentimeters">
<h3>maxKingpinToRearAxleDistanceInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxKingpinToRearAxleDistanceInCentimeters</span></div>
<div class="block"><p>Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
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
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
