---
title: "Angle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-angle"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Angle.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.Angle</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Angle</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents an angle independent of the unit of measurement.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="fromDegrees(double)">
<h3>fromDegrees</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a></span> <span className="element-name">fromDegrees</span><wbr/><span className="parameters">(double angle)</span></div>
<div className="block"><p>Creates a new angle object based on the supplied angle value in degrees.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>angle</code> - <p>Angle value in degrees.</p></dd>
<dt>Returns:</dt>
<dd><p>The angle as specified by input in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromRadians(double)">
<h3>fromRadians</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-angle" title="class in com.here.sdk.core">Angle</a></span> <span className="element-name">fromRadians</span><wbr/><span className="parameters">(double angle)</span></div>
<div className="block"><p>Creates a new angle object based on the supplied angle value in radians.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>angle</code> - <p>Angle value in radians.</p></dd>
<dt>Returns:</dt>
<dd><p>The angle as specified by input in radians.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDegrees()">
<h3>getDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getDegrees</span>()</div>
<div className="block"><p>Gets the value of this angle in degrees.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The value of this angle in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRadians()">
<h3>getRadians</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getRadians</span>()</div>
<div className="block"><p>Gets the value of this angle in radians.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The value of this angle in radians.</p></dd>
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
