---
title: "TollFare (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-tollfare"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TollFare.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.TollFare</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TollFare</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>This struct presents all the fare data for a toll.
 <strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
 currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
 Additionally, this feature and related APIs may be updated in future releases
 without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
 is only available for the Navigate license. If you're using the
 <code>RoutingEngine</code>, this feature is considered to be stable.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#currency">currency</a></code></div>
<div className="col-last even-row-color">
<div className="block">The currency in which the toll is to be paid in ISO 4217 format, e.g.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#pass">pass</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Specifies whether this <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#paymentMethods">paymentMethods</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of accepted payment methods like cash and credit card.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#price">price</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The amount of the toll be paid.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#timeRule">timeRule</a></code></div>
<div className="col-last even-row-color">
<div className="block">The time domain when this fare is valid.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#transponders">transponders</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of available transponders.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#%3Cinit%3E(java.lang.String,double,java.util.List)">TollFare</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)">TollFare</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)">TollFare</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)">TollFare</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a> pass)</code></div>
<div className="col-last odd-row-color">
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
<section className="detail" id="currency">
<h3>currency</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">currency</span></div>
<div className="block"><p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></div>
</section>
</li>
<li>
<section className="detail" id="price">
<h3>price</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">price</span></div>
<div className="block"><p>The amount of the toll be paid.</p></div>
</section>
</li>
<li>
<section className="detail" id="paymentMethods">
<h3>paymentMethods</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt;</span> <span className="element-name">paymentMethods</span></div>
<div className="block"><p>The list of accepted payment methods like cash and credit card.</p></div>
</section>
</li>
<li>
<section className="detail" id="timeRule">
<h3>timeRule</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span className="element-name">timeRule</span></div>
<div className="block"><p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></div>
</section>
</li>
<li>
<section className="detail" id="transponders">
<h3>transponders</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">transponders</span></div>
<div className="block"><p>The list of available transponders.</p></div>
</section>
</li>
<li>
<section className="detail" id="pass">
<h3>pass</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></span> <span className="element-name">pass</span></div>
<div className="block"><p>Specifies whether this <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List)">
<h3>TollFare</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TollFare</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)">
<h3>TollFare</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TollFare</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
<dd><code>timeRule</code> - <p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)">
<h3>TollFare</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TollFare</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
<dd><code>timeRule</code> - <p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></dd>
<dd><code>transponders</code> - <p>The list of available transponders.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)">
<h3>TollFare</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TollFare</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a> pass)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
<dd><code>timeRule</code> - <p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></dd>
<dd><code>transponders</code> - <p>The list of available transponders.</p></dd>
<dd><code>pass</code> - <p>Specifies whether this <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</p></dd>
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
