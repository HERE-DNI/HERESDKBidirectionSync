---
title: "AngleRange (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-anglerange"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AngleRange.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.AngleRange</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AngleRange</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents angle ranges as a circular sector by using an absolute start angle
 and a relative range angle called extent. They both define a sector on a
 circle. All angles are in degrees and are clockwise-oriented.
 By default, the AngleRange represents the entire circle, the value is in the range of [0, 360].
 Values will be corrected during construction using normalization
 for the start angle and clamping for the extent angle, ensuring a valid range
 for all possible inputs.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-anglerange#extent">extent</a></code></div>
<div className="col-last even-row-color">
<div className="block">The angle range extent, running clockwise, in degrees from start.</div>
</div>
<div className="col-first odd-row-color"><code>final double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-anglerange#start">start</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Start angle, running clockwise, in degrees from north.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-anglerange#%3Cinit%3E()">AngleRange</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a range covering a full circle.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-anglerange#%3Cinit%3E(double,double)">AngleRange</a><wbr/>(double start,
 double extent)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs an AngleRange from the provided start and extent angles.</div>
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
<section className="detail" id="start">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">start</span></div>
<div className="block"><p>Start angle, running clockwise, in degrees from north.
 The value is in the range of [0, 360) degrees.</p></div>
</section>
</li>
<li>
<section className="detail" id="extent">
<h3>extent</h3>
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">extent</span></div>
<div className="block"><p>The angle range extent, running clockwise, in degrees from start.
 The value is in the range of [0, 360] degrees.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,double)">
<h3>AngleRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AngleRange</span><wbr/><span className="parameters">(double start,
 double extent)</span></div>
<div className="block"><p>Constructs an AngleRange from the provided start and extent angles.
 Corrects values if they exceed the ranges.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>start</code> - <p>Start angle, running clockwise, in degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>extent</code> - <p>The range's extent, running clockwise, in degrees from start.
     The value will be clamped to the range of [0, 360] degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>AngleRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AngleRange</span>()</div>
<div className="block"><p>Constructs a range covering a full circle.</p></div>
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
<li>
<section className="detail" id="fromMinMaxDegreesClockwise(double,double)">
<h3>fromMinMaxDegreesClockwise</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span className="element-name">fromMinMaxDegreesClockwise</span><wbr/><span className="parameters">(double min,
 double max)</span></div>
<div className="block"><p>Constructs an AngleRange from the provided minimum and maximum angles.
 Corrects values if they exceed the ranges. The angles are always
 interpreted in clockwise orientation.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - <p>Angle where to start the circular sector, running clockwise, in
     degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>max</code> - <p>Angle where the circular sector ends, running clockwise, in
     degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dt>Returns:</dt>
<dd><p>Created AngleRange from the provided minimum and maximum angles.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromDirectionDegreesClockwise(double,double)">
<h3>fromDirectionDegreesClockwise</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span className="element-name">fromDirectionDegreesClockwise</span><wbr/><span className="parameters">(double center,
 double extent)</span></div>
<div className="block"><p>Constructs an AngleRange from the provided center angle defining the
 direction and an angular width to extent the range by 50% clockwise and
 50% counter-clockwise from its center angle.
 Corrects values if they exceed the ranges.
 Example: direction = 90, extent = 10 means the circle sector is pointing
 east, with an extent of 5 degrees north-wards and 5 degrees south-wards.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>center</code> - <p>Start angle, running clockwise, in degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>extent</code> - <p>The range's extent, running clockwise, in degrees from start.
     The value will be clamped to the range of [0, 360] degrees.</p></dd>
<dt>Returns:</dt>
<dd><p>Created AngleRange from the provided center angle and the range's extent.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="inRange(double)">
<h3>inRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">inRange</span><wbr/><span className="parameters">(double angleClockwiseInDegreesFromNorth)</span></div>
<div className="block"><p>Check if a given angle in degrees, clockwise from north is in range or not.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>angleClockwiseInDegreesFromNorth</code> - <p>An angle in degrees from north. Will be normalized before testing.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code>, if an angle is in range, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="closestInRange(double)">
<h3>closestInRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">closestInRange</span><wbr/><span className="parameters">(double angleClockwiseInDegreesFromNorth)</span></div>
<div className="block"><p>Get the angle that is closest to the given one and in range. If the
 angle to both ends of the range is the same, the value in the clockwise
 direction is returned. If the given angle is in range already,
 it will be returned as normalized angle.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>angleClockwiseInDegreesFromNorth</code> - <p>An angle in degrees from north. Will be normalized.</p></dd>
<dt>Returns:</dt>
<dd><p>The closest, normalized in-range angle in degrees, clockwise from north.
     If the given angle is in range already, the given angle will be returned as
     normalized angle in degree, clockwise from north.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="max()">
<h3>max</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">max</span>()</div>
<div className="block"><p>Get the maximum angle defined by the range in degrees, clockwise from north,
 normalized to [0,360).</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Maximum angle of the range in degrees, clockwise from north, normalized to
     [0,360).</p></dd>
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
