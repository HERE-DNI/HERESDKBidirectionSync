---
title: "Easing (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-animation-easing"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Easing.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.animation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.animation.Easing</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Easing</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Animation easing representing an easing function to be used during animations.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-easing-instantiationerrorcode" title="enum class in com.here.sdk.animation">Easing.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create an <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-easing-instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create an <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-easing#%3Cinit%3E(com.here.sdk.animation.EasingFunction)">Easing</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-animation-easingfunction" title="enum class in com.here.sdk.animation">EasingFunction</a> easingFunction)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a predefined easing function.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-animation-easing#%3Cinit%3E(java.util.List)">Easing</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a>&gt; points)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates an instance of customized <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a specified number of points describing an
 easing function.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.animation.EasingFunction)">
<h3>Easing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Easing</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-easingfunction" title="enum class in com.here.sdk.animation">EasingFunction</a> easingFunction)</span></div>
<div className="block"><p>Creates an instance of <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a predefined easing function.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>easingFunction</code> - <p>Easing function.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List)">
<h3>Easing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Easing</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a>&gt; points)</span>
       throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-animation-easing-instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></span></div>
<div className="block"><p>Creates an instance of customized <a href="sdk-for-android-navigate-com-here-sdk-animation-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a specified number of points describing an
 easing function.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>List of sampled data points that define an easing function.
     X describes normalized time values in the range [0, 1].
     Y describes normalized animated value changes. Values can fall outside of the range [0, 1]. During
     an animation run animated target value is multiplied with Y value. In case resulting animated target value
     falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for
     color animation).
     X values must increase monotonically.
     There must be at least 2 data points specified. The first point's X value must be 0, the last point's
     X value must be 1.
     During an animation run for any given time value X' from the animation engine that
     satisfies the relation X(i) &lt; X' &lt; X(i+1) for the given X data points the corresponding
     Y' value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points.
     The higher the sampling rate of the easing curve used for the data points the more precise the results.
     In order to achieve the same animation precision for animations with different durations
     (shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-animation-easing-instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></code> - <p>Instantiation error in case of invalid input parameters.</p></dd>
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
