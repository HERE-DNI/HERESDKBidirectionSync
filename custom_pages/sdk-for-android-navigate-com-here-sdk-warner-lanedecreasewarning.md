---
title: "LaneDecreaseWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LaneDecreaseWarning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.warner.LaneDecreaseWarning</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LaneDecreaseWarning</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.
 Lane decrease warnings are generated when the road ahead has fewer lanes
 than the previous road segment provided by <code>sdk.electronic_horizon.ElectronicHorizonEngine</code>,
 requiring drivers to merge or change lanes.
 Lane decrease is provided only on highways and motorways. It will not be provided for junctions,
 when maneuver is given for the lane decrease situation or when the <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation"><code>TrafficMergeWarning</code></a>
 is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation
 if the according options are set in <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#distanceInMeters">distanceInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The distance from the current location to the Lane decrease event.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#distanceType">distanceType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates if the specified event is ahead of the vehicle or has just passed by.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#id">id</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unique identifier for this lane decrease warning instance.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#lanesDecreasedFromLeft">lanesDecreasedFromLeft</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of lanes decreased on the left side of the road,
 <code>null</code> if the left-side change is unknown or not applicable.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#lanesDecreasedFromRight">lanesDecreasedFromRight</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of lanes decreased on the right side of the road,
 <code>null</code> if the right-side change is unknown or not applicable.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#newLaneNumber">newLaneNumber</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of lanes after the lane decrease event.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#previousLaneNumber">previousLaneNumber</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of lanes before the lane decrease event.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#%3Cinit%3E(double,com.here.sdk.navigation.DistanceType)">LaneDecreaseWarning</a><wbr/>(double distanceInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
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
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">id</span></div>
<div className="block"><p>Unique identifier for this lane decrease warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section className="detail" id="previousLaneNumber">
<h3>previousLaneNumber</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">previousLaneNumber</span></div>
<div className="block"><p>Number of lanes before the lane decrease event.</p></div>
</section>
</li>
<li>
<section className="detail" id="newLaneNumber">
<h3>newLaneNumber</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">newLaneNumber</span></div>
<div className="block"><p>Number of lanes after the lane decrease event.</p></div>
</section>
</li>
<li>
<section className="detail" id="lanesDecreasedFromLeft">
<h3>lanesDecreasedFromLeft</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">lanesDecreasedFromLeft</span></div>
<div className="block"><p>Number of lanes decreased on the left side of the road,
 <code>null</code> if the left-side change is unknown or not applicable.</p></div>
</section>
</li>
<li>
<section className="detail" id="lanesDecreasedFromRight">
<h3>lanesDecreasedFromRight</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">lanesDecreasedFromRight</span></div>
<div className="block"><p>Number of lanes decreased on the right side of the road,
 <code>null</code> if the right-side change is unknown or not applicable.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceInMeters">
<h3>distanceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceInMeters</span></div>
<div className="block"><p>The distance from the current location to the Lane decrease event.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceType">
<h3>distanceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span className="element-name">distanceType</span></div>
<div className="block"><p>Indicates if the specified event is ahead of the vehicle or has just passed by. If it is
 ahead, then <a href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.DistanceType)">
<h3>LaneDecreaseWarning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LaneDecreaseWarning</span><wbr/><span className="parameters">(double distanceInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>distanceInMeters</code> - <p>The distance from the current location to the Lane decrease event.</p></dd>
<dd><code>distanceType</code> - <p>Indicates if the specified event is ahead of the vehicle or has just passed by. If it is
 ahead, then <a href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></dd>
</dl>
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
