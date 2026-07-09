---
title: "EVChargingPool (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evchargingpool"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVChargingPool.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.EVChargingPool</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">EVChargingPool</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A charging pool for electric vehicles is an area equipped with one or more charging stations.
 Use <a href="sdk-for-android-navigate-placecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION"><code>PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION</code></a> to find stations.
 In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
 if any.
 For offline EV rich attributes, also enable <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-evaccesstype" title="enum class in com.here.sdk.search">EVAccessType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#access">access</a></code></div>
<div className="col-last even-row-color">
<div className="block">The accessibility level of the charging pool, or <code>null</code> if unknown.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#accessRestrictionReasons">accessRestrictionReasons</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Contains the list of reasons for restriction.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation" title="class in com.here.sdk.search">EVChargingStation</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#chargingStations">chargingStations</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of charging stations.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#cpoId">cpoId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">CPO (Charge Point Operator) id for charging pool.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpooldetails" title="class in com.here.sdk.search">EVChargingPoolDetails</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#details">details</a></code></div>
<div className="col-last even-row-color">
<div className="block">EV charging station attributes details.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-emobilityserviceprovider" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#eMobilityServiceProviders">eMobilityServiceProviders</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of e-Mobility Service Providers.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evse" title="class in com.here.sdk.search">Evse</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#evseInfo">evseInfo</a></code></div>
<div className="col-last even-row-color">
<div className="block">Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#id">id</a></code></div>
<div className="col-last odd-row-color">
<div className="block">HERE ID of the charging pool.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool#%3Cinit%3E(java.util.List,java.util.List,java.util.List)">EVChargingPool</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation" title="class in com.here.sdk.search">EVChargingStation</a>&gt; chargingStations,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-emobilityserviceprovider" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt; eMobilityServiceProviders,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt; accessRestrictionReasons)</code></div>
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
<section className="detail" id="chargingStations">
<h3>chargingStations</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation" title="class in com.here.sdk.search">EVChargingStation</a>&gt;</span> <span className="element-name">chargingStations</span></div>
<div className="block"><p>List of charging stations.</p></div>
</section>
</li>
<li>
<section className="detail" id="eMobilityServiceProviders">
<h3>eMobilityServiceProviders</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-emobilityserviceprovider" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt;</span> <span className="element-name">eMobilityServiceProviders</span></div>
<div className="block"><p>List of e-Mobility Service Providers.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section className="detail" id="access">
<h3>access</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evaccesstype" title="enum class in com.here.sdk.search">EVAccessType</a></span> <span className="element-name">access</span></div>
<div className="block"><p>The accessibility level of the charging pool, or <code>null</code> if unknown.</p></div>
</section>
</li>
<li>
<section className="detail" id="accessRestrictionReasons">
<h3>accessRestrictionReasons</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</span> <span className="element-name">accessRestrictionReasons</span></div>
<div className="block"><p>Contains the list of reasons for restriction.
 Populated only for offline search and when access is <a href="sdk-for-android-navigate-evaccesstype#RESTRICTED_ACCESS"><code>EVAccessType.RESTRICTED_ACCESS</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="details">
<h3>details</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpooldetails" title="class in com.here.sdk.search">EVChargingPoolDetails</a></span> <span className="element-name">details</span></div>
<div className="block"><p>EV charging station attributes details. It is available only for a place that has charging station
 for electric vehicles. Only offline search fills this field.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">id</span></div>
<div className="block"><p>HERE ID of the charging pool.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section className="detail" id="cpoId">
<h3>cpoId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">cpoId</span></div>
<div className="block"><p>CPO (Charge Point Operator) id for charging pool.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section className="detail" id="evseInfo">
<h3>evseInfo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evse" title="class in com.here.sdk.search">Evse</a>&gt;</span> <span className="element-name">evseInfo</span></div>
<div className="block"><p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
 Only online search fills this field.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List)">
<h3>EVChargingPool</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">EVChargingPool</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation" title="class in com.here.sdk.search">EVChargingStation</a>&gt; chargingStations,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-emobilityserviceprovider" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt; eMobilityServiceProviders,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt; accessRestrictionReasons)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>chargingStations</code> - <p>List of charging stations.</p></dd>
<dd><code>eMobilityServiceProviders</code> - <p>List of e-Mobility Service Providers.
 Only online search fills this field.</p></dd>
<dd><code>accessRestrictionReasons</code> - <p>Contains the list of reasons for restriction.
 Populated only for offline search and when access is <a href="sdk-for-android-navigate-evaccesstype#RESTRICTED_ACCESS"><code>EVAccessType.RESTRICTED_ACCESS</code></a>.</p></dd>
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
