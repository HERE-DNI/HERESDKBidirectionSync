---
title: "TollFare (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-tollfare"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TollFare.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.TollFare</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TollFare</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>This struct presents all the fare data for a toll.
 </p><p><strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
 currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
 Additionally, this feature and related APIs may be updated in future releases
 without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
 is only available for the Navigate license. If you're using the
 <code>RoutingEngine</code>, this feature is considered to be stable.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#currency">currency</a></code></div>
<div class="col-last even-row-color">
<div class="block">The currency in which the toll is to be paid in ISO 4217 format, e.g.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#pass">pass</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies whether this <a href="sdk-for-android-navigate-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#paymentMethods">paymentMethods</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of accepted payment methods like cash and credit card.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#price">price</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The amount of the toll be paid.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timeRule">timeRule</a></code></div>
<div class="col-last even-row-color">
<div class="block">The time domain when this fare is valid.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#transponders">transponders</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of available transponders.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String,double,java.util.List)">TollFare</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)">TollFare</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)">TollFare</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)">TollFare</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders,
 <a href="sdk-for-android-navigate-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a> pass)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="currency">
<h3>currency</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">currency</span></div>
<div class="block"><p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></div>
</section>
</li>
<li>
<section class="detail" id="price">
<h3>price</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">price</span></div>
<div class="block"><p>The amount of the toll be paid.</p></div>
</section>
</li>
<li>
<section class="detail" id="paymentMethods">
<h3>paymentMethods</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt;</span> <span class="element-name">paymentMethods</span></div>
<div class="block"><p>The list of accepted payment methods like cash and credit card.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeRule">
<h3>timeRule</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span></div>
<div class="block"><p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></div>
</section>
</li>
<li>
<section class="detail" id="transponders">
<h3>transponders</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">transponders</span></div>
<div class="block"><p>The list of available transponders.</p></div>
</section>
</li>
<li>
<section class="detail" id="pass">
<h3>pass</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></span> <span class="element-name">pass</span></div>
<div class="block"><p>Specifies whether this <a href="sdk-for-android-navigate-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List)">
<h3>TollFare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)">
<h3>TollFare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)">
<h3>TollFare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)">
<h3>TollFare</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currency,
 double price,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>&gt; paymentMethods,
 @Nullable
 <a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; transponders,
 @Nullable
 <a href="sdk-for-android-navigate-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a> pass)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>currency</code> - <p>The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</p></dd>
<dd><code>price</code> - <p>The amount of the toll be paid.</p></dd>
<dd><code>paymentMethods</code> - <p>The list of accepted payment methods like cash and credit card.</p></dd>
<dd><code>timeRule</code> - <p>The time domain when this fare is valid.
 If this field is missing, it means the fare is always valid.
 For a detailed description of the Time Domain specification and usage in routing services, please refer to
 the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p></dd>
<dd><code>transponders</code> - <p>The list of available transponders.</p></dd>
<dd><code>pass</code> - <p>Specifies whether this <a href="sdk-for-android-navigate-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> is a multi-travel pass, and its characteristics.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
