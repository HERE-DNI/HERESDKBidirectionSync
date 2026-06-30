---
title: "Easing (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-animation-easing"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Easing.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.animation.Easing</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Easing</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Animation easing representing an easing function to be used during animations.</p></div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-easing.instantiationerrorcode" title="enum class in com.here.sdk.animation">Easing.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create an <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-easing.instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create an <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-animation-easing#%3Cinit%3E(com.here.sdk.animation.EasingFunction)">Easing</a><wbr/>(<a href="sdk-for-android-explore-easingfunction" title="enum class in com.here.sdk.animation">EasingFunction</a> easingFunction)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a predefined easing function.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-animation-easing#%3Cinit%3E(java.util.List)">Easing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a>&gt; points)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of customized <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a specified number of points describing an
 easing function.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.animation.EasingFunction)">
<h3>Easing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Easing</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-easingfunction" title="enum class in com.here.sdk.animation">EasingFunction</a> easingFunction)</span></div>
<div class="block"><p>Creates an instance of <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a predefined easing function.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>easingFunction</code> - <p>Easing function.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>Easing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Easing</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a>&gt; points)</span>
       throws <span class="exceptions"><a href="sdk-for-android-explore-easing.instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></span></div>
<div class="block"><p>Creates an instance of customized <a href="sdk-for-android-explore-easing" title="class in com.here.sdk.animation"><code>Easing</code></a> using a specified number of points describing an
 easing function.</p></div>
<dl class="notes">
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
<dd><code><a href="sdk-for-android-explore-easing.instantiationexception" title="class in com.here.sdk.animation">Easing.InstantiationException</a></code> - <p>Instantiation error in case of invalid input parameters.</p></dd>
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
