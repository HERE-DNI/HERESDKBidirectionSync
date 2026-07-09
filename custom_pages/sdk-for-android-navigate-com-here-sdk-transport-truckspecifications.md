---
title: "TruckSpecifications (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-transport-truckspecifications"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TruckSpecifications.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.transport</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.transport.TruckSpecifications</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public final class </span><span className="element-name type-name-label">TruckSpecifications</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.</p></div>
</div>
<div className="block"><p>Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
 Only the fields that are set are considered for restriction handling.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount">axleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines total number of axles in the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#currentWeightInKilograms">currentWeightInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#grossWeightInKilograms">grossWeightInKilograms</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#heightInCentimeters">heightInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Truck height in centimeters.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#isTruckLight">isTruckLight</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#lengthInCentimeters">lengthInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Truck length in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#payloadCapacityInKilograms">payloadCapacityInKilograms</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Allowed payload capacity, including trailers, specified in kilograms.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount">trailerAxleCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines total number of axles across all the trailers attached to the vehicle.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerCount">trailerCount</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines number of trailers attached to the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#truckType">truckType</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines the type of truck.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#weightPerAxleGroup">weightPerAxleGroup</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#weightPerAxleInKilograms">weightPerAxleInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Heaviest weight per axle, regardless of axle type or axle group.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#widthInCentimeters">widthInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Truck width in centimeters.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#%3Cinit%3E()">TruckSpecifications</a>()</code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
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
<section className="detail" id="grossWeightInKilograms">
<h3>grossWeightInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">grossWeightInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#currentWeightInKilograms"><code>currentWeightInKilograms</code></a>. By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="currentWeightInKilograms">
<h3>currentWeightInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">currentWeightInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#grossWeightInKilograms"><code>grossWeightInKilograms</code></a>. By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="weightPerAxleInKilograms">
<h3>weightPerAxleInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">weightPerAxleInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Heaviest weight per axle, regardless of axle type or axle group.
 It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
 The provided value must be greater or equal to 0.
 By default, it is not set.
 <strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
 When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div>
</section>
</li>
<li>
<section className="detail" id="weightPerAxleGroup">
<h3>weightPerAxleGroup</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></span> <span className="element-name">weightPerAxleGroup</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
 This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
 By default is not set.
 <strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
 When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div>
</section>
</li>
<li>
<section className="detail" id="heightInCentimeters">
<h3>heightInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">heightInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Truck height in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="widthInCentimeters">
<h3>widthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">widthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Truck width in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="lengthInCentimeters">
<h3>lengthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">lengthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Truck length in centimeters. The provided value must be in the range [0, 30000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="axleCount">
<h3>axleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">axleCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines total number of axles in the vehicle. The provided value must be greater than or
 equal to 2. By default, it is not set.
 Route calculation: When not set, possible axle count restrictions will not be
 taken into consideration.
 Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
 greater than <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount"><code>axleCount</code></a> will not be displayed.
 When specifying <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount"><code>axleCount</code></a> is required and must be greater than <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerCount">
<h3>trailerCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">trailerCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines number of trailers attached to the vehicle. The provided value must be in the range
 [0, 255]. By default, it is not set.
 When specifying <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerCount"><code>trailerCount</code></a> is required and must be greater than 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckType">
<h3>truckType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span className="element-name">truckType</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines the type of truck. By default, it is <a href="sdk-for-android-navigate-trucktype#STRAIGHT"><code>TruckType.STRAIGHT</code></a>.
 Rendering <code>sdk.mapview.TruckProfile</code>: <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#truckType"><code>truckType</code></a> is ignored and has no effect.</p></div>
</section>
</li>
<li>
<section className="detail" id="isTruckLight">
<h3>isTruckLight</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTruckLight</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
 The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.
 A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
 the vehicle can access, which access restrictions apply, and which speed limits are applicable.
 Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
 not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.
 In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
 you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
 a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.
 When <code>TruckSpecifications</code> are set as part of <code>MapContentSettings</code>, then this flag will be ignored and
 has no effect.
 <strong>Note:</strong>
 This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
 experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases with a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="payloadCapacityInKilograms">
<h3>payloadCapacityInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">payloadCapacityInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Allowed payload capacity, including trailers, specified in kilograms. The provided value
 must be greater then or equal to 0. By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerAxleCount">
<h3>trailerAxleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">trailerAxleCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines total number of axles across all the trailers attached to the vehicle.
 This number is included in <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount"><code>axleCount</code></a>, hence <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount"><code>trailerAxleCount</code></a> must be less than <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount"><code>axleCount</code></a>
 and greater than or equal to 1. <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#axleCount"><code>axleCount</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerCount"><code>trailerCount</code></a> are required to specify <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>.
 By default, it is not set.
 Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p></div>
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
<h3>TruckSpecifications</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TruckSpecifications</span>()</div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
