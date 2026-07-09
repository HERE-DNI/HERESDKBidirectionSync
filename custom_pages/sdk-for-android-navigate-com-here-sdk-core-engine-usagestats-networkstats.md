---
title: "UsageStats.NetworkStats (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- UsageStats.NetworkStats.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.engine.UsageStats.NetworkStats</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats" title="class in com.here.sdk.core.engine">UsageStats</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">UsageStats.NetworkStats</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Provides network statistics in bytes per method.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats#methodCall">methodCall</a></code></div>
<div className="col-last even-row-color">
<div className="block">Name or description of the method being called.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats#receivedBytes">receivedBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of bytes received from the network.</div>
</div>
<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats#requestCounter">requestCounter</a></code></div>
<div className="col-last even-row-color">
<div className="block">Amount of calls for particular family of methodCall.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats#sentBytes">sentBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of bytes sent over the network.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-usagestats-networkstats#%3Cinit%3E(long,long,java.lang.String,long)">NetworkStats</a><wbr/>(long sentBytes,
 long receivedBytes,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodCall,
 long requestCounter)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="sentBytes">
<h3>sentBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">sentBytes</span></div>
<div className="block"><p>Number of bytes sent over the network.</p></div>
</section>
</li>
<li>
<section className="detail" id="receivedBytes">
<h3>receivedBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">receivedBytes</span></div>
<div className="block"><p>Number of bytes received from the network.</p></div>
</section>
</li>
<li>
<section className="detail" id="methodCall">
<h3>methodCall</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">methodCall</span></div>
<div className="block"><p>Name or description of the method being called.</p></div>
</section>
</li>
<li>
<section className="detail" id="requestCounter">
<h3>requestCounter</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">requestCounter</span></div>
<div className="block"><p>Amount of calls for particular family of methodCall.
 methodCall in this case is considered as base request,
 additional query params are ignored, all calculated as one request.
 e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2
 will be considered as 1 methodCall, and requestCounter is 2.</p></div>
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
<section className="detail" id="&lt;init&gt;(long,long,java.lang.String,long)">
<h3>NetworkStats</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">NetworkStats</span><wbr/><span className="parameters">(long sentBytes,
 long receivedBytes,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> methodCall,
 long requestCounter)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sentBytes</code> - <p>Number of bytes sent over the network.</p></dd>
<dd><code>receivedBytes</code> - <p>Number of bytes received from the network.</p></dd>
<dd><code>methodCall</code> - <p>Name or description of the method being called.</p></dd>
<dd><code>requestCounter</code> - <p>Amount of calls for particular family of methodCall.
 methodCall in this case is considered as base request,
 additional query params are ignored, all calculated as one request.
 e.g. https://search.hereapi.com/someparams and https://search.hereapi.com/someparams2
 will be considered as 1 methodCall, and requestCounter is 2.</p></dd>
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
