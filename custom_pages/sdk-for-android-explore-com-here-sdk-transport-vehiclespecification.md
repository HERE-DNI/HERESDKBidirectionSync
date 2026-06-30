---
title: "VehicleSpecification (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-vehiclespecification"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VehicleSpecification.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.transport.VehicleSpecification</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleSpecification</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Contains vehicle related attributes. Examples: Dimensions, weight, axle count.
 Only the fields that are set are considered for restriction handling.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-busbuilder" title="class in com.here.sdk.transport">VehicleSpecification.BusBuilder</a></code></div>
<div class="col-last even-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a bus.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-carbuilder" title="class in com.here.sdk.transport">VehicleSpecification.CarBuilder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a car.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-privatebusbuilder" title="class in com.here.sdk.transport">VehicleSpecification.PrivateBusBuilder</a></code></div>
<div class="col-last even-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a private bus.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-scooterbuilder" title="class in com.here.sdk.transport">VehicleSpecification.ScooterBuilder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a scooter.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-taxibuilder" title="class in com.here.sdk.transport">VehicleSpecification.TaxiBuilder</a></code></div>
<div class="col-last even-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a taxi.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-truckbuilder" title="class in com.here.sdk.transport">VehicleSpecification.TruckBuilder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This class constructs a <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> for a truck.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount">axleCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines total number of axles in the vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#currentWeightInKilograms">currentWeightInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#emptyWeightInKilograms">emptyWeightInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#engineSizeInCubicCentimeters">engineSizeInCubicCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Engine size of the scooter in cubic centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#grossWeightInKilograms">grossWeightInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#hazardousMaterials">hazardousMaterials</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies a list of hazardous materials shipped in the vehicle.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#heightInCentimeters">heightInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicle height in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#isCommercial">isCommercial</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies whether the vehicle is a commercial or a non-commercial vehicle.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#isTruckLight">isTruckLight</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#kingpinToRearAxleDistanceInCentimeters">kingpinToRearAxleDistanceInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines the kingpin to rear axle distance, in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#lastCharacterOfLicensePlate">lastCharacterOfLicensePlate</a></code></div>
<div class="col-last even-row-color">
<div class="block">Last character of license plate in String format.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#lengthInCentimeters">lengthInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicle length in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#occupancy">occupancy</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the number of occupants in the vehicle, including driver,
 can affect the vehicle's ability to use HOV/carpool restricted lanes.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#payloadCapacityInKilograms">payloadCapacityInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Allowed payload capacity, including trailers, specified in kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#tiresCount">tiresCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount">trailerAxleCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines total number of axles across all the trailers attached to the vehicle.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerCount">trailerCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines number of trailers attached to the vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckCategory">truckCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines the truck category.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckType">truckType</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#tunnelCategory">tunnelCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the tunnel categories to restrict certain route links.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-transport-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleGroup">weightPerAxleGroup</a></code></div>
<div class="col-last even-row-color">
<div class="block">Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms"><code>weightPerAxleInKilograms</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms">weightPerAxleInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Heaviest weight per axle, regardless of axle type or axle group.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#widthInCentimeters">widthInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicle width in centimeters.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#%3Cinit%3E()">VehicleSpecification</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="heightInCentimeters">
<h3>heightInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">heightInCentimeters</span></div>
<div class="block"><p>Vehicle height in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="widthInCentimeters">
<h3>widthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">widthInCentimeters</span></div>
<div class="block"><p>Vehicle width in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="lengthInCentimeters">
<h3>lengthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">lengthInCentimeters</span></div>
<div class="block"><p>Vehicle length in centimeters. The provided value must be in the range [0, 30000].
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="axleCount">
<h3>axleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">axleCount</span></div>
<div class="block"><p>Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
 By default, it is not set.
 Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
 Rendering: When set, truck restriction icons for an axle count greater than <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"><code>axleCount</code></a> will not be displayed.
 When specifying <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"><code>axleCount</code></a> is required and must be greater than <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"><code>trailerAxleCount</code></a>.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerCount">
<h3>trailerCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerCount</span></div>
<div class="block"><p>Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
 By default, it is not set.
 When specifying <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerCount"><code>trailerCount</code></a> is required and must be greater than 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckType">
<h3>truckType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span class="element-name">truckType</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Use <code>VehicleSpecification.truckCategory</code> instead.</p></div>
</div>
<div class="block"><p>Will be replaced with <code>truckCategory</code> when the <code>TruckSpecification</code> will be replaced by <code>VehicleSpecification</code>.
 Defines the type of truck.
 Defaults to <a href="sdk-for-android-explore-trucktype#STRAIGHT"><code>TruckType.STRAIGHT</code></a>.
 Rendering <code>sdk.mapview.TruckProfile</code>: <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckType"><code>truckType</code></a> is ignored and has no effect.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckCategory">
<h3>truckCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span class="element-name">truckCategory</span></div>
<div class="block"><p>Defines the truck category.
 By default, it is not set.
 Rendering: <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckCategory"><code>truckCategory</code></a> is ignored and has no effect.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTruckLight">
<h3>isTruckLight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTruckLight</span></div>
<div class="block"><p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
 The flag should not be set to <code>true</code> in other countries than Japan.
 Defaults to <code>false</code>.
 A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
 the vehicle can access, which access restrictions apply, and which speed limits are applicable.
 Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
 not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.
 In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to <code>true</code>,
 you will get, for example, the same speed limits as for cars. Make sure to set the flag only to <code>true</code>, when
 a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.
 When on <code>MapContentSettings</code>, then this flag will be ignored and has no effect.
 <strong>Notes:</strong>
<ul>
<li>This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
 experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.</li>
<li>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</li>
<li>Supported only in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> transport mode.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="payloadCapacityInKilograms">
<h3>payloadCapacityInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">payloadCapacityInKilograms</span></div>
<div class="block"><p>Allowed payload capacity, including trailers, specified in kilograms. The provided value
 must be greater then or equal to 0.
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta)
 transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerAxleCount">
<h3>trailerAxleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerAxleCount</span></div>
<div class="block"><p>Defines total number of axles across all the trailers attached to the vehicle.
 This number is included in <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"><code>axleCount</code></a>, hence <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"><code>trailerAxleCount</code></a> must be less than <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"><code>axleCount</code></a>
 and greater than or equal to 1. <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"><code>axleCount</code></a> and <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerCount"><code>trailerCount</code></a> are required to specify <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"><code>trailerAxleCount</code></a>.
 By default, it is not set.
 <strong>Note:</strong>: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p></div>
</section>
</li>
<li>
<section class="detail" id="kingpinToRearAxleDistanceInCentimeters">
<h3>kingpinToRearAxleDistanceInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">kingpinToRearAxleDistanceInCentimeters</span></div>
<div class="block"><p>Defines the kingpin to rear axle distance, in centimeters.
 <strong>NOTE:</strong> Currently, the KPRA restrictions are only present in California and Idaho.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="emptyWeightInKilograms">
<h3>emptyWeightInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">emptyWeightInKilograms</span></div>
<div class="block"><p>Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
 The provided value must be greater than or equal to 0.
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="grossWeightInKilograms">
<h3>grossWeightInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">grossWeightInKilograms</span></div>
<div class="block"><p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#currentWeightInKilograms"><code>currentWeightInKilograms</code></a>.
 By default, it is not set.
 <strong>Notes:</strong>
<ul>
<li>Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 4250 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 7550 kg.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="currentWeightInKilograms">
<h3>currentWeightInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">currentWeightInKilograms</span></div>
<div class="block"><p>Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#grossWeightInKilograms"><code>grossWeightInKilograms</code></a>.
 By default, it is not set.
 <strong>Notes:</strong>
<ul>
<li>Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#currentWeightInKilograms"><code>currentWeightInKilograms</code></a> above <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#grossWeightInKilograms"><code>grossWeightInKilograms</code></a> may result in
 non-compliant or invalid routes.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="weightPerAxleInKilograms">
<h3>weightPerAxleInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">weightPerAxleInKilograms</span></div>
<div class="block"><p>Heaviest weight per axle, regardless of axle type or axle group.
 It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
 The provided value must be greater or equal to 0.
 By default, it is not set.
 <strong>Notes:</strong>
<ul>
<li><a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms"><code>weightPerAxleInKilograms</code></a> and <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleGroup"><code>weightPerAxleGroup</code></a> are incompatible.
 When available for your edition, if both attributes are set, during online <code>RoutingEngine</code> an <code>RoutingError.INVALID_PARAMETER</code>
 error is generated. Otherwise, when offline <code>RoutingEngine</code> is in place, both parameters are evaluated and the
 maximum value between them will be used.</li>
<li>Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="weightPerAxleGroup">
<h3>weightPerAxleGroup</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-transport-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></span> <span class="element-name">weightPerAxleGroup</span></div>
<div class="block"><p>Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms"><code>weightPerAxleInKilograms</code></a>.
 This is relevant in countries with signs and regulations that specify different limits for different axle
 groups, like the USA and Sweden.
 By default is not set.
 <strong>Notes:</strong>
<ul>
<li><a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms"><code>weightPerAxleInKilograms</code></a> and <a href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleGroup"><code>weightPerAxleGroup</code></a> are incompatible.
 When available for your edition, if both attributes are set, during online <code>RoutingEngine</code> an <code>RoutingError.INVALID_PARAMETER</code>
 error is generated. Otherwise, when offline <code>RoutingEngine</code> is in place, both parameters are evaluated and
 the maximum value between them will be used.</li>
<li>Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="isCommercial">
<h3>isCommercial</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCommercial</span></div>
<div class="block"><p>Specifies whether the vehicle is a commercial or a non-commercial vehicle.
 Defaults to <code>false</code>.
 <strong>Notes</strong>
<ul>
<li>Only supported for online routing.</li>
<li>This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
<li>Not used for offline calculations.</li>
<li>Supported for <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a>, <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a> and <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a>.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="lastCharacterOfLicensePlate">
<h3>lastCharacterOfLicensePlate</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">lastCharacterOfLicensePlate</span></div>
<div class="block"><p>Last character of license plate in String format. This value can be used to
 evaluate restrictions in environmental zones.
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="engineSizeInCubicCentimeters">
<h3>engineSizeInCubicCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">engineSizeInCubicCentimeters</span></div>
<div class="block"><p>Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535.
 Default value is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the
 road.
 <strong>Notes</strong>
<ul>
<li>For now, this option is only relevant in Japan and will be ignored for other countries. Currently,
 map data for this option is only available for Japan.</li>
<li>Supported only in <a href="sdk-for-android-explore-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> (Alpha) transport mode.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="tiresCount">
<h3>tiresCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">tiresCount</span></div>
<div class="block"><p>The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
 By default, it is not set.
 Otherwise it is guaranteed to be in the range [1, 255].
 <strong>Note</strong>: This parameter is not supported in isoline routing.</p></div>
</section>
</li>
<li>
<section class="detail" id="tunnelCategory">
<h3>tunnelCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span class="element-name">tunnelCategory</span></div>
<div class="block"><p>Specifies the tunnel categories to restrict certain route links.
 The route will pass only through tunnels of a less strict category.
 Refer to <a href="sdk-for-android-explore-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport"><code>TunnelCategory</code></a> for the available options.
 By default, it is not set.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="hazardousMaterials">
<h3>hazardousMaterials</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span class="element-name">hazardousMaterials</span></div>
<div class="block"><p>Specifies a list of hazardous materials shipped in the vehicle.
 Refer to <a href="sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport"><code>HazardousMaterial</code></a> for the available options.
 By default, it is an empty list.
 <strong>Note:</strong> Supported in <a href="sdk-for-android-explore-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>, <a href="sdk-for-android-explore-transportmode#BUS"><code>TransportMode.BUS</code></a>, <a href="sdk-for-android-explore-transportmode#PRIVATE_BUS"><code>TransportMode.PRIVATE_BUS</code></a>,
 <a href="sdk-for-android-explore-transportmode#CAR"><code>TransportMode.CAR</code></a> (Beta), <a href="sdk-for-android-explore-transportmode#TAXI"><code>TransportMode.TAXI</code></a> (Beta) transport modes.</p></div>
</section>
</li>
<li>
<section class="detail" id="occupancy">
<h3>occupancy</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">occupancy</span></div>
<div class="block"><p>Specifies the number of occupants in the vehicle, including driver,
 can affect the vehicle's ability to use HOV/carpool restricted lanes.
 Should not be less than 1 or greater than 255.
 By default, it is not set.</p></div>
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
<h3>VehicleSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleSpecification</span>()</div>
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






</div>
`
}</HTMLBlock>
