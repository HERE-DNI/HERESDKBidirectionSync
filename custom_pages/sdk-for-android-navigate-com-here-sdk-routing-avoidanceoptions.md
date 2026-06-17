---
title: "AvoidanceOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AvoidanceOptions.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.AvoidanceOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AvoidanceOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The options to specify restrictions for route calculations.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidboundingboxareaoptions" title="class in com.here.sdk.routing">AvoidBoundingBoxAreaOptions</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#avoidBoundingBoxAreasOptions">avoidBoundingBoxAreasOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of rectangular shapes which routes must not cross and additional options for this area.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidcorridorareaoptions" title="class in com.here.sdk.routing">AvoidCorridorAreaOptions</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#avoidCorridorAreasOptions">avoidCorridorAreasOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of corridor shapes which routes must not cross and additional options for this area.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#avoidedTruckRoadTypes">avoidedTruckRoadTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies a list of avoided truck road types for vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidpolygonareaoptions" title="class in com.here.sdk.routing">AvoidPolygonAreaOptions</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#avoidPolygonAreasOptions">avoidPolygonAreasOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of polygon shapes which routes must not cross and additional options for this area.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#countries">countries</a></code></div>
<div class="col-last even-row-color">
<div class="block">Countries that the route must avoid.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#exceptZoneIds">exceptZoneIds</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-roadfeatures" title="enum class in com.here.sdk.routing">RoadFeatures</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#roadFeatures">roadFeatures</a></code></div>
<div class="col-last even-row-color">
<div class="block">Features which routes should avoid.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#segments">segments</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Segments that routes will avoid going through.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-zonecategory" title="enum class in com.here.sdk.routing">ZoneCategory</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#zoneCategories">zoneCategories</a></code></div>
<div class="col-last even-row-color">
<div class="block">Zone categories which routes must not cross.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#zoneIds">zoneIds</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List containing identifiers of zones that routes should avoid going through.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">AvoidanceOptions</a>()</code></div>
<div class="col-last even-row-color">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="roadFeatures">
<h3>roadFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-roadfeatures" title="enum class in com.here.sdk.routing">RoadFeatures</a>&gt;</span> <span class="element-name">roadFeatures</span></div>
<div class="block"><p>Features which routes should avoid. Best effort only (not enforced).</p></div>
</section>
</li>
<li>
<section class="detail" id="countries">
<h3>countries</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>&gt;</span> <span class="element-name">countries</span></div>
<div class="block"><p>Countries that the route must avoid. Strictly enforced.
 Violations are reported as <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 <strong>Note:</strong> This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidBoundingBoxAreasOptions">
<h3>avoidBoundingBoxAreasOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidboundingboxareaoptions" title="class in com.here.sdk.routing">AvoidBoundingBoxAreaOptions</a>&gt;</span> <span class="element-name">avoidBoundingBoxAreasOptions</span></div>
<div class="block"><p>List of rectangular shapes which routes must not cross and additional options for this area.</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidPolygonAreasOptions">
<h3>avoidPolygonAreasOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidpolygonareaoptions" title="class in com.here.sdk.routing">AvoidPolygonAreaOptions</a>&gt;</span> <span class="element-name">avoidPolygonAreasOptions</span></div>
<div class="block"><p>List of polygon shapes which routes must not cross and additional options for this area.
 <strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidCorridorAreasOptions">
<h3>avoidCorridorAreasOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-avoidcorridorareaoptions" title="class in com.here.sdk.routing">AvoidCorridorAreaOptions</a>&gt;</span> <span class="element-name">avoidCorridorAreasOptions</span></div>
<div class="block"><p>List of corridor shapes which routes must not cross and additional options for this area.
 <strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.</p></div>
</section>
</li>
<li>
<section class="detail" id="zoneCategories">
<h3>zoneCategories</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-zonecategory" title="enum class in com.here.sdk.routing">ZoneCategory</a>&gt;</span> <span class="element-name">zoneCategories</span></div>
<div class="block"><p>Zone categories which routes must not cross. Strictly enforced.
 Violations are reported as <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sectionnoticecode#VIOLATED_ZONE_RESTRICTION"><code>SectionNoticeCode.VIOLATED_ZONE_RESTRICTION</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="segments">
<h3>segments</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a>&gt;</span> <span class="element-name">segments</span></div>
<div class="block"><p>Segments that routes will avoid going through.
 Violations are reported as <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sectionnoticecode#VIOLATED_BLOCKED_ROAD"><code>SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code></a>.
 </p><p><strong>Notes:</strong>
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
<section class="detail" id="exceptZoneIds">
<h3>exceptZoneIds</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">exceptZoneIds</span></div>
<div class="block"><p>Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.
 e.g. the format of ID is like <code>here:cm:envzone:2</code>.
 Information about the various routing zones originates from the respective catalogs of platform.here.com.
 For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".</p></div>
</section>
</li>
<li>
<section class="detail" id="zoneIds">
<h3>zoneIds</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">zoneIds</span></div>
<div class="block"><p>List containing identifiers of zones that routes should avoid going through.
 e.g. the format of ID is like <code>here:cm:envzone:2</code>.
 Information about the various routing zones originates from the respective catalogs of platform.here.com.
 For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidedTruckRoadTypes">
<h3>avoidedTruckRoadTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a>&gt;</span> <span class="element-name">avoidedTruckRoadTypes</span></div>
<div class="block"><p>Specifies a list of avoided truck road types for vehicle.
 Refer to <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport"><code>TruckRoadType</code></a> for the available options.</p></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>AvoidanceOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AvoidanceOptions</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
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
</main>





</div>
`
}</HTMLBlock>
