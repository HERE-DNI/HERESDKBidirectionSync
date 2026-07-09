---
title: "EVChargingLocationFeature (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVChargingLocationFeature.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a>&gt;
<div className="inheritance">com.here.sdk.search.EVChargingLocationFeature</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">EVChargingLocationFeature</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a>&gt;</span></div>
<div className="block"><p>Optional features that can be requested for EV charging locations.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#CONNECTOR_GROUPS">CONNECTOR_GROUPS</a></code></div>
<div className="col-last even-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getConnectorGroups()"><code>EVChargingLocation.getConnectorGroups()</code></a> will be returned.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#EMSPS">EMSPS</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getEMobilityServiceProviders()"><code>EVChargingLocation.getEMobilityServiceProviders()</code></a> will be returned.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#EVSES">EVSES</a></code></div>
<div className="col-last even-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getEvses()"><code>EVChargingLocation.getEvses()</code></a> will be returned.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#LOCATION_INFO">LOCATION_INFO</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getCpoID()"><code>EVChargingLocation.getCpoID()</code></a>, <a href="sdk-for-android-navigate-evcharginglocation#getFacilityTypes()"><code>EVChargingLocation.getFacilityTypes()</code></a>,
 <a href="sdk-for-android-navigate-evcharginglocation#getParkingType()"><code>EVChargingLocation.getParkingType()</code></a>, <a href="sdk-for-android-navigate-evcharginglocation#getEnergyMix()"><code>EVChargingLocation.getEnergyMix()</code></a>,
 and <a href="sdk-for-android-navigate-evcharginglocation#getOpeningHours()"><code>EVChargingLocation.getOpeningHours()</code></a> will be returned.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#NEARBY">NEARBY</a></code></div>
<div className="col-last even-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getFacilityTypes()"><code>EVChargingLocation.getFacilityTypes()</code></a> will be returned.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#TARIFFS">TARIFFS</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><a href="sdk-for-android-navigate-evchargingconnectorgroup#tariffIndexes"><code>EVChargingConnectorGroup.tariffIndexes</code></a> will be returned.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#TRUCK_RESTRICTIONS">TRUCK_RESTRICTIONS</a></code></div>
<div className="col-last even-row-color">
<div className="block"><a href="sdk-for-android-navigate-evcharginglocation#getTruckRestrictions()"><code>EVChargingLocation.getTruckRestrictions()</code></a> will be returned.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="EVSES">
<h3>EVSES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">EVSES</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getEvses()"><code>EVChargingLocation.getEvses()</code></a> will be returned.
 If <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#CONNECTOR_GROUPS"><code>CONNECTOR_GROUPS</code></a> is also included, then
 <a href="sdk-for-android-navigate-evchargingconnectorgroup#connectors"><code>EVChargingConnectorGroup.connectors</code></a> will also be returned.</p></div>
</section>
</li>
<li>
<section className="detail" id="TRUCK_RESTRICTIONS">
<h3>TRUCK_RESTRICTIONS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">TRUCK_RESTRICTIONS</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getTruckRestrictions()"><code>EVChargingLocation.getTruckRestrictions()</code></a> will be returned.</p></div>
</section>
</li>
<li>
<section className="detail" id="LOCATION_INFO">
<h3>LOCATION_INFO</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">LOCATION_INFO</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getCpoID()"><code>EVChargingLocation.getCpoID()</code></a>, <a href="sdk-for-android-navigate-evcharginglocation#getFacilityTypes()"><code>EVChargingLocation.getFacilityTypes()</code></a>,
 <a href="sdk-for-android-navigate-evcharginglocation#getParkingType()"><code>EVChargingLocation.getParkingType()</code></a>, <a href="sdk-for-android-navigate-evcharginglocation#getEnergyMix()"><code>EVChargingLocation.getEnergyMix()</code></a>,
 and <a href="sdk-for-android-navigate-evcharginglocation#getOpeningHours()"><code>EVChargingLocation.getOpeningHours()</code></a> will be returned.</p></div>
</section>
</li>
<li>
<section className="detail" id="EMSPS">
<h3>EMSPS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">EMSPS</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getEMobilityServiceProviders()"><code>EVChargingLocation.getEMobilityServiceProviders()</code></a> will be returned.</p></div>
</section>
</li>
<li>
<section className="detail" id="CONNECTOR_GROUPS">
<h3>CONNECTOR_GROUPS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">CONNECTOR_GROUPS</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getConnectorGroups()"><code>EVChargingLocation.getConnectorGroups()</code></a> will be returned.
 To ensure <a href="sdk-for-android-navigate-evchargingconnectorgroup#connectors"><code>EVChargingConnectorGroup.connectors</code></a> is available, also include
 <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#EVSES"><code>EVSES</code></a>.
 To ensure <a href="sdk-for-android-navigate-evchargingconnectorgroup#tariffIndexes"><code>EVChargingConnectorGroup.tariffIndexes</code></a> is available, also include
 <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#TARIFFS"><code>TARIFFS</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="TARIFFS">
<h3>TARIFFS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">TARIFFS</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evchargingconnectorgroup#tariffIndexes"><code>EVChargingConnectorGroup.tariffIndexes</code></a> will be returned.
 Ignored if neither <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#EVSES"><code>EVSES</code></a> nor
 <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature#CONNECTOR_GROUPS"><code>CONNECTOR_GROUPS</code></a> are included.</p></div>
</section>
</li>
<li>
<section className="detail" id="NEARBY">
<h3>NEARBY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">NEARBY</span></div>
<div className="block"><p><a href="sdk-for-android-navigate-evcharginglocation#getFacilityTypes()"><code>EVChargingLocation.getFacilityTypes()</code></a> will be returned.</p></div>
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
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocationfeature" title="enum class in com.here.sdk.search">EVChargingLocationFeature</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
