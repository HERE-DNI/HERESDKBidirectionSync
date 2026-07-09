---
title: "AvoidanceOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AvoidanceOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.AvoidanceOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AvoidanceOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The options to specify restrictions for route calculations.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidboundingboxareaoptions" title="class in com.here.sdk.routing">AvoidBoundingBoxAreaOptions</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#avoidBoundingBoxAreasOptions">avoidBoundingBoxAreasOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of rectangular shapes which routes must not cross and additional options for this area.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions" title="class in com.here.sdk.routing">AvoidCorridorAreaOptions</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#avoidCorridorAreasOptions">avoidCorridorAreasOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of corridor shapes which routes must not cross and additional options for this area.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#avoidedTruckRoadTypes">avoidedTruckRoadTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies a list of avoided truck road types for vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidpolygonareaoptions" title="class in com.here.sdk.routing">AvoidPolygonAreaOptions</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#avoidPolygonAreasOptions">avoidPolygonAreasOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of polygon shapes which routes must not cross and additional options for this area.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#countries">countries</a></code></div>
<div className="col-last even-row-color">
<div className="block">Countries that the route must avoid.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#exceptZoneIds">exceptZoneIds</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-roadfeatures" title="enum class in com.here.sdk.routing">RoadFeatures</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#roadFeatures">roadFeatures</a></code></div>
<div className="col-last even-row-color">
<div className="block">Features which routes should avoid.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#segments">segments</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Segments that routes will avoid going through.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-zonecategory" title="enum class in com.here.sdk.routing">ZoneCategory</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#zoneCategories">zoneCategories</a></code></div>
<div className="col-last even-row-color">
<div className="block">Zone categories which routes must not cross.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#zoneIds">zoneIds</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List containing identifiers of zones that routes should avoid going through.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions#%3Cinit%3E()">AvoidanceOptions</a>()</code></div>
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
<section className="detail" id="roadFeatures">
<h3>roadFeatures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-roadfeatures" title="enum class in com.here.sdk.routing">RoadFeatures</a>&gt;</span> <span className="element-name">roadFeatures</span></div>
<div className="block"><p>Features which routes should avoid. Best effort only (not enforced).</p></div>
</section>
</li>
<li>
<section className="detail" id="countries">
<h3>countries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</span> <span className="element-name">countries</span></div>
<div className="block"><p>Countries that the route must avoid. Strictly enforced.
 Violations are reported as <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 <strong>Note:</strong> This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidBoundingBoxAreasOptions">
<h3>avoidBoundingBoxAreasOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidboundingboxareaoptions" title="class in com.here.sdk.routing">AvoidBoundingBoxAreaOptions</a>&gt;</span> <span className="element-name">avoidBoundingBoxAreasOptions</span></div>
<div className="block"><p>List of rectangular shapes which routes must not cross and additional options for this area.</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidPolygonAreasOptions">
<h3>avoidPolygonAreasOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidpolygonareaoptions" title="class in com.here.sdk.routing">AvoidPolygonAreaOptions</a>&gt;</span> <span className="element-name">avoidPolygonAreasOptions</span></div>
<div className="block"><p>List of polygon shapes which routes must not cross and additional options for this area.
 <strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidCorridorAreasOptions">
<h3>avoidCorridorAreasOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-avoidcorridorareaoptions" title="class in com.here.sdk.routing">AvoidCorridorAreaOptions</a>&gt;</span> <span className="element-name">avoidCorridorAreasOptions</span></div>
<div className="block"><p>List of corridor shapes which routes must not cross and additional options for this area.
 <strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.</p></div>
</section>
</li>
<li>
<section className="detail" id="zoneCategories">
<h3>zoneCategories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-zonecategory" title="enum class in com.here.sdk.routing">ZoneCategory</a>&gt;</span> <span className="element-name">zoneCategories</span></div>
<div className="block"><p>Zone categories which routes must not cross. Strictly enforced.
 Violations are reported as <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_ZONE_RESTRICTION"><code>SectionNoticeCode.VIOLATED_ZONE_RESTRICTION</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="segments">
<h3>segments</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a>&gt;</span> <span className="element-name">segments</span></div>
<div className="block"><p>Segments that routes will avoid going through.
 Violations are reported as <a href="sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 <strong>Notes:</strong>
<ul>
<li>This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.</li>
<li>The engine does not support an unlimited number of segments to avoid.
 The limit is defined by the HERE backend services and may change. For now,
 the maximum number of segments to avoid should be below 250. This value may change
 on the backend and it is therefore not guaranteed to be stable.</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="exceptZoneIds">
<h3>exceptZoneIds</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">exceptZoneIds</span></div>
<div className="block"><p>Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.
 e.g. the format of ID is like <code>here:cm:envzone:2</code>.
 Information about the various routing zones originates from the respective catalogs of platform.here.com.
 For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".</p></div>
</section>
</li>
<li>
<section className="detail" id="zoneIds">
<h3>zoneIds</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">zoneIds</span></div>
<div className="block"><p>List containing identifiers of zones that routes should avoid going through.
 e.g. the format of ID is like <code>here:cm:envzone:2</code>.
 Information about the various routing zones originates from the respective catalogs of platform.here.com.
 For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidedTruckRoadTypes">
<h3>avoidedTruckRoadTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</span> <span className="element-name">avoidedTruckRoadTypes</span></div>
<div className="block"><p>Specifies a list of avoided truck road types for vehicle.
 Refer to <a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport"><code>TruckRoadType</code></a> for the available options.</p></div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>AvoidanceOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AvoidanceOptions</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
