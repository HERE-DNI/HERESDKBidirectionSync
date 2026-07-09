---
title: "CarSpecifications (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-transport-carspecifications"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CarSpecifications.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.transport</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.transport.CarSpecifications</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public final class </span><span className="element-name type-name-label">CarSpecifications</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.</p></div>
</div>
<div className="block"><p>Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
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
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#axleCount">axleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines total number of axles in the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#grossWeightInKilograms">grossWeightInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Car weight including trailers and shipped goods in kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#heightInCentimeters">heightInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Car height in centimeters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#lengthInCentimeters">lengthInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Car length in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount">trailerAxleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines total number of axles across all the trailers attached to the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerCount">trailerCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines number of trailers attached to the vehicle.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#widthInCentimeters">widthInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Car width in centimeters.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#%3Cinit%3E()">CarSpecifications</a>()</code></div>
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
<div className="block"><p>Car weight including trailers and shipped goods in kilograms. The provided value
 must be greater than or equal to 0. By default, it is not set.
 <strong>Note:</strong>
 This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.</p></div>
</section>
</li>
<li>
<section className="detail" id="heightInCentimeters">
<h3>heightInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">heightInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Car height in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="widthInCentimeters">
<h3>widthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">widthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Car width in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="lengthInCentimeters">
<h3>lengthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">lengthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Car length in centimeters. The provided value must be in the range [0, 30000].
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
 When specifying <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#axleCount"><code>axleCount</code></a> is required and must be greater than <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerCount">
<h3>trailerCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">trailerCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines number of trailers attached to the vehicle. The provided value must be in the range
 [0, 1]. By default, it is not set.
 When specifying <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerCount"><code>trailerCount</code></a> is required and must be greater than 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerAxleCount">
<h3>trailerAxleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">trailerAxleCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines total number of axles across all the trailers attached to the vehicle.
 This number is included in <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#axleCount"><code>axleCount</code></a>, hence <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount"><code>trailerAxleCount</code></a> must be less than <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#axleCount"><code>axleCount</code></a>
 and greater than or equal to 1. <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#axleCount"><code>axleCount</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerCount"><code>trailerCount</code></a> are required to specify <a href="sdk-for-android-navigate-com-here-sdk-transport-carspecifications#trailerAxleCount"><code>trailerAxleCount</code></a>.
 By default, it is not set.</p></div>
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
<h3>CarSpecifications</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CarSpecifications</span>()</div>
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
