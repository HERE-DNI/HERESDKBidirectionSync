---
title: "Point2DKeyframe (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Point2DKeyframe.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.animation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.animation.Point2DKeyframe</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Point2DKeyframe</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A Point2D keyframe. A keyframe consists of a value and an animation duration.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe#duration">duration</a></code></div>
<div className="col-last even-row-color">
<div className="block">Relative animation duration for reaching the keyframe value.</div>
</div>
<div className="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe#value">value</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Point2D keyframe value.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-point2dkeyframe#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.time.Duration)">Point2DKeyframe</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> value,
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a Point2DKeyframe from the value and offset.</div>
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
<section className="detail" id="value">
<h3>value</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span className="element-name">value</span></div>
<div className="block"><p>Point2D keyframe value.</p></div>
</section>
</li>
<li>
<section className="detail" id="duration">
<h3>duration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">duration</span></div>
<div className="block"><p>Relative animation duration for reaching the keyframe value.
 Negative duration value gets clamped to 0.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.Point2D,com.here.time.Duration)">
<h3>Point2DKeyframe</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Point2DKeyframe</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> value,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div className="block"><p>Constructs a Point2DKeyframe from the value and offset.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Point2D keyframe value.</p></dd>
<dd><code>duration</code> - <p>Relative animation duration for reaching the keyframe value.
     Negative duration value gets clamped to 0.</p></dd>
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
