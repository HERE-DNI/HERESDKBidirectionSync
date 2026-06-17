---
title: "TMCData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TMCData.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.trafficbroadcast.TMCData</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TMCData</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents the traffic events in RDS-TMC format.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#additionalEvents">additionalEvents</a></code></div>
<div class="col-last even-row-color">
<div class="block">Additional traffic events.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#additionalLocations">additionalLocations</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Additional traffic locations.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#direction">direction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Street direction.</div>
</div>
<div class="col-first odd-row-color"><code>short</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#diversionAdvice">diversionAdvice</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Diversion advice.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#durationPersistence">durationPersistence</a></code></div>
<div class="col-last even-row-color">
<div class="block">Duration persitence.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#event">event</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic event data.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#extent">extent</a></code></div>
<div class="col-last even-row-color">
<div class="block">Extent.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#location">location</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic event location.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#numberOfGroups">numberOfGroups</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of groups (1 to 5).</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(short,short,short,short,short,int,long,java.util.List,java.util.List)">TMCData</a><wbr/>(short numberOfGroups,
 short extent,
 short direction,
 short diversionAdvice,
 short durationPersistence,
 int event,
 long location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; additionalEvents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; additionalLocations)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="numberOfGroups">
<h3>numberOfGroups</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">numberOfGroups</span></div>
<div class="block"><p>Number of groups (1 to 5).</p></div>
</section>
</li>
<li>
<section class="detail" id="extent">
<h3>extent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">extent</span></div>
<div class="block"><p>Extent.</p></div>
</section>
</li>
<li>
<section class="detail" id="direction">
<h3>direction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">direction</span></div>
<div class="block"><p>Street direction.</p></div>
</section>
</li>
<li>
<section class="detail" id="diversionAdvice">
<h3>diversionAdvice</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">diversionAdvice</span></div>
<div class="block"><p>Diversion advice.</p></div>
</section>
</li>
<li>
<section class="detail" id="durationPersistence">
<h3>durationPersistence</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">durationPersistence</span></div>
<div class="block"><p>Duration persitence.</p></div>
</section>
</li>
<li>
<section class="detail" id="event">
<h3>event</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">event</span></div>
<div class="block"><p>Traffic event data.</p></div>
</section>
</li>
<li>
<section class="detail" id="location">
<h3>location</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">location</span></div>
<div class="block"><p>Traffic event location.</p></div>
</section>
</li>
<li>
<section class="detail" id="additionalEvents">
<h3>additionalEvents</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">additionalEvents</span></div>
<div class="block"><p>Additional traffic events.</p></div>
</section>
</li>
<li>
<section class="detail" id="additionalLocations">
<h3>additionalLocations</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt;</span> <span class="element-name">additionalLocations</span></div>
<div class="block"><p>Additional traffic locations.</p></div>
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
<section class="detail" id="&lt;init&gt;(short,short,short,short,short,int,long,java.util.List,java.util.List)">
<h3>TMCData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TMCData</span><wbr/><span class="parameters">(short numberOfGroups,
 short extent,
 short direction,
 short diversionAdvice,
 short durationPersistence,
 int event,
 long location,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; additionalEvents,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; additionalLocations)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>numberOfGroups</code> - <p>Number of groups (1 to 5).</p></dd>
<dd><code>extent</code> - <p>Extent.</p></dd>
<dd><code>direction</code> - <p>Street direction.</p></dd>
<dd><code>diversionAdvice</code> - <p>Diversion advice.</p></dd>
<dd><code>durationPersistence</code> - <p>Duration persitence.</p></dd>
<dd><code>event</code> - <p>Traffic event data.</p></dd>
<dd><code>location</code> - <p>Traffic event location.</p></dd>
<dd><code>additionalEvents</code> - <p>Additional traffic events.</p></dd>
<dd><code>additionalLocations</code> - <p>Additional traffic locations.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
