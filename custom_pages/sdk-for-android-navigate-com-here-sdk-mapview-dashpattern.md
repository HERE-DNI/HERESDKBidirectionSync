---
title: "DashPattern (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-dashpattern"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DashPattern.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.DashPattern</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">DashPattern</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a dash pattern for map polyline.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-dashpattern#firstDashLength">firstDashLength</a></code></div>
<div className="col-last even-row-color">
<div className="block">Length of first dash in pixels.</div>
</div>
<div className="col-first odd-row-color"><code>final double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-dashpattern#firstGapLength">firstGapLength</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Length of first gap in pixels.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-dashpattern#%3Cinit%3E(double)">DashPattern</a><wbr/>(double dashLength)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a uniform dash pattern in which the length of a gap is the same
 as the length of a dash.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-dashpattern#%3Cinit%3E(double,double)">DashPattern</a><wbr/>(double gapLength,
 double dashLength)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a simple dash pattern in which the lengths of a dash and gap can be different.</div>
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
<section className="detail" id="firstGapLength">
<h3>firstGapLength</h3>
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">firstGapLength</span></div>
<div className="block"><p>Length of first gap in pixels.</p></div>
</section>
</li>
<li>
<section className="detail" id="firstDashLength">
<h3>firstDashLength</h3>
<div className="member-signature"><span className="modifiers">public final</span> <span className="return-type">double</span> <span className="element-name">firstDashLength</span></div>
<div className="block"><p>Length of first dash in pixels.</p></div>
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
<section className="detail" id="&lt;init&gt;(double)">
<h3>DashPattern</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashPattern</span><wbr/><span className="parameters">(double dashLength)</span></div>
<div className="block"><p>Creates a uniform dash pattern in which the length of a gap is the same
 as the length of a dash.
 This allows for patterns like <code>' — — — —'</code> or <code>' ——— ——— ———'</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>dashLength</code> - <p>The length of a dash in pixels. The gap will have the same length.
     Clamped to the range of [1, 500].</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double,double)">
<h3>DashPattern</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashPattern</span><wbr/><span className="parameters">(double gapLength,
 double dashLength)</span></div>
<div className="block"><p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.
 This allows for patterns like <code>' — — — —'</code> or <code>' ——— ——— ———'</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>gapLength</code> - <p>The length of a gap in pixels. Clamped to the range of [1, 500].</p></dd>
<dd><code>dashLength</code> - <p>The length of a dash in pixels. Clamped to the range of [1, 500].</p></dd>
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
