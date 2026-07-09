---
title: "MapSceneLights.Direction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSceneLights.Direction.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapSceneLights.Direction</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapSceneLights.Direction</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The direction of lights as a pair of azimuth and altitude angles.
 See https://en.wikipedia.org/wiki/Horizontal_coordinate_system</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#altitude">altitude</a></code></div>
<div className="col-last even-row-color">
<div className="block">Direction altitude value in degrees in the range [0, 90].</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#azimuth">azimuth</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Direction azimuth value in degrees in the range [0, 360).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#%3Cinit%3E()">Direction</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#%3Cinit%3E(double,double)">Direction</a><wbr/>(double azimuth,
 double altitude)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a Direction from the values.</div>
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
<section className="detail" id="azimuth">
<h3>azimuth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">azimuth</span></div>
<div className="block"><p>Direction azimuth value in degrees in the range [0, 360).
 The default value is 0.0.
 The azimuth range is half-open, meaning the maximum value is not included in the range.
 If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
 Specifically, values less than 0 will be increased by 360 until they fall within the range,
 and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
 By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
 Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p></div>
</section>
</li>
<li>
<section className="detail" id="altitude">
<h3>altitude</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">altitude</span></div>
<div className="block"><p>Direction altitude value in degrees in the range [0, 90].
 The default value is 0.0.
 The altitude value is clamped to this range.
 If the value falls outside its supported range, it will be adjusted to stay within the range.
 Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
 Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
 For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
 When both azimuth and altitude values are provided, they are adjusted independently:
 For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p></div>
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
<h3>Direction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Direction</span>()</div>
<div className="block"><p>Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double,double)">
<h3>Direction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Direction</span><wbr/><span className="parameters">(double azimuth,
 double altitude)</span></div>
<div className="block"><p>Constructs a Direction from the values.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>azimuth</code> - <p>Direction azimuth value in degrees in the range [0, 360).
 The default value is 0.0.
 The azimuth range is half-open, meaning the maximum value is not included in the range.
 If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
 Specifically, values less than 0 will be increased by 360 until they fall within the range,
 and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
 By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
 Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p></dd>
<dd><code>altitude</code> - <p>Direction altitude value in degrees in the range [0, 90].
 The default value is 0.0.
 The altitude value is clamped to this range.
 If the value falls outside its supported range, it will be adjusted to stay within the range.
 Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
 Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
 For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
 When both azimuth and altitude values are provided, they are adjusted independently:
 For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p></dd>
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
