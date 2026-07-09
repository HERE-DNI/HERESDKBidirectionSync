---
title: "SectionNotice (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-sectionnotice"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SectionNotice.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.SectionNotice</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SectionNotice</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Explains an issue encountered in a <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice#code">code</a></code></div>
<div className="col-last even-row-color">
<div className="block">The notice code.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-noticeseverity" title="enum class in com.here.sdk.routing">NoticeSeverity</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice#severity">severity</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The notice severity.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice#violatedRestrictions">violatedRestrictions</a></code></div>
<div className="col-last even-row-color">
<div className="block">The following property <code>violated_restrictions</code> contains the notice detail information.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice#%3Cinit%3E(com.here.sdk.routing.SectionNoticeCode,com.here.sdk.routing.NoticeSeverity)">SectionNotice</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a> code,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-noticeseverity" title="enum class in com.here.sdk.routing">NoticeSeverity</a> severity)</code></div>
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
<section className="detail" id="code">
<h3>code</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span className="element-name">code</span></div>
<div className="block"><p>The notice code.</p></div>
</section>
</li>
<li>
<section className="detail" id="severity">
<h3>severity</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-noticeseverity" title="enum class in com.here.sdk.routing">NoticeSeverity</a></span> <span className="element-name">severity</span></div>
<div className="block"><p>The notice severity.</p></div>
</section>
</li>
<li>
<section className="detail" id="violatedRestrictions">
<h3>violatedRestrictions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a>&gt;</span> <span className="element-name">violatedRestrictions</span></div>
<div className="block"><p>The following property <code>violated_restrictions</code> contains the notice detail information.
 Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction.
 There is no one-to-one match of the <code>SectionNotice.code</code> and these three restriction types. For example, if <code>SectionNotice.code</code> is
 <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_VEHICLE_RESTRICTION"><code>SectionNoticeCode.VIOLATED_VEHICLE_RESTRICTION</code></a>, then it can be either vehicle restriction or transport mode restriction. If <code>SectionNotice.code</code> is
 <a href="sdk-for-android-navigate-sectionnoticecode#SEASONAL_CLOSURE"><code>SectionNoticeCode.SEASONAL_CLOSURE</code></a>, then it is time dependent restriction.
 If the section notice is none of the above-mentioned three types, then this will be an empty list.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.SectionNoticeCode,com.here.sdk.routing.NoticeSeverity)">
<h3>SectionNotice</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SectionNotice</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a> code,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-noticeseverity" title="enum class in com.here.sdk.routing">NoticeSeverity</a> severity)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>code</code> - <p>The notice code.</p></dd>
<dd><code>severity</code> - <p>The notice severity.</p></dd>
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
