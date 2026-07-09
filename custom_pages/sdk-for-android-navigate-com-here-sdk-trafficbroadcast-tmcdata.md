---
title: "TMCData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TMCData.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.trafficbroadcast.TMCData</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TMCData</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents the traffic events in RDS-TMC format.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#additionalEvents">additionalEvents</a></code></div>
<div className="col-last even-row-color">
<div className="block">Additional traffic events.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#additionalLocations">additionalLocations</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Additional traffic locations.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#direction">direction</a></code></div>
<div className="col-last even-row-color">
<div className="block">Street direction.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#diversionAdvice">diversionAdvice</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Diversion advice.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#durationPersistence">durationPersistence</a></code></div>
<div className="col-last even-row-color">
<div className="block">Duration persitence.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#event">event</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Traffic event data.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#extent">extent</a></code></div>
<div className="col-last even-row-color">
<div className="block">Extent.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#location">location</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Traffic event location.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#numberOfGroups">numberOfGroups</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of groups (1 to 5).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#%3Cinit%3E(short,short,short,short,short,int,long,java.util.List,java.util.List)">TMCData</a><wbr/>(short numberOfGroups,
 short extent,
 short direction,
 short diversionAdvice,
 short durationPersistence,
 int event,
 long location,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; additionalEvents,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; additionalLocations)</code></div>
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
<section className="detail" id="numberOfGroups">
<h3>numberOfGroups</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">numberOfGroups</span></div>
<div className="block"><p>Number of groups (1 to 5).</p></div>
</section>
</li>
<li>
<section className="detail" id="extent">
<h3>extent</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">extent</span></div>
<div className="block"><p>Extent.</p></div>
</section>
</li>
<li>
<section className="detail" id="direction">
<h3>direction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">direction</span></div>
<div className="block"><p>Street direction.</p></div>
</section>
</li>
<li>
<section className="detail" id="diversionAdvice">
<h3>diversionAdvice</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">diversionAdvice</span></div>
<div className="block"><p>Diversion advice.</p></div>
</section>
</li>
<li>
<section className="detail" id="durationPersistence">
<h3>durationPersistence</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">durationPersistence</span></div>
<div className="block"><p>Duration persitence.</p></div>
</section>
</li>
<li>
<section className="detail" id="event">
<h3>event</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">event</span></div>
<div className="block"><p>Traffic event data.</p></div>
</section>
</li>
<li>
<section className="detail" id="location">
<h3>location</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">location</span></div>
<div className="block"><p>Traffic event location.</p></div>
</section>
</li>
<li>
<section className="detail" id="additionalEvents">
<h3>additionalEvents</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">additionalEvents</span></div>
<div className="block"><p>Additional traffic events.</p></div>
</section>
</li>
<li>
<section className="detail" id="additionalLocations">
<h3>additionalLocations</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt;</span> <span className="element-name">additionalLocations</span></div>
<div className="block"><p>Additional traffic locations.</p></div>
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
<section className="detail" id="&lt;init&gt;(short,short,short,short,short,int,long,java.util.List,java.util.List)">
<h3>TMCData</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TMCData</span><wbr/><span className="parameters">(short numberOfGroups,
 short extent,
 short direction,
 short diversionAdvice,
 short durationPersistence,
 int event,
 long location,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; additionalEvents,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; additionalLocations)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
