---
title: "RoadSignWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadSignWarning.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.RoadSignWarning</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoadSignWarning</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A road sign. The main field describing the sign is <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type"><code>type</code></a>. Some road types are standardized, others can be country specific.
 A valid road sign contains known <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type"><code>type</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#category"><code>category</code></a>.
 Use <code>RoadSignWarningListener</code> to get notifications with current road signs.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#category">category</a></code></div>
<div class="col-last even-row-color">
<div class="block">The main category to which the road sign belongs.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceToRoadSignInMeters">distanceToRoadSignInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Distance to the road sign in meters.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceType">distanceType</a></code></div>
<div class="col-last even-row-color">
<div class="block">The distance type for the warning, e.g.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#duration">duration</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional length information during which the warning is applicable.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#generalWarningType">generalWarningType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the general warning to which the road sign belongs.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#id">id</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unique identifier for this specific road sign warning instance.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#isPrioritySign">isPrioritySign</a></code></div>
<div class="col-last even-row-color">
<div class="block">Flag indicating if the road sign is a priority sign.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#preWarning">preWarning</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional pre-warning in terms of distance, of the upcoming warning or regulation.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#roadSignSegment">roadSignSegment</a></code></div>
<div class="col-last even-row-color">
<div class="block">The reference to the segment where the road sign is located.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#signValue">signValue</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type">type</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type of the road sign.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#validityTime">validityTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#vehicleTypes">vehicleTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies a list of vehicle types for which the road sign is applicable.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#weatherType">weatherType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the weather type for which the sign is applicable.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#%3Cinit%3E(double,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,com.here.sdk.navigation.GeneralWarningRoadSignType,boolean,java.util.List,com.here.sdk.navigation.WeatherType,com.here.sdk.routing.SegmentReference,com.here.sdk.navigation.DistanceType)">RoadSignWarning</a><wbr/>(double distanceToRoadSignInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> category,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 boolean isPrioritySign,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> roadSignSegment,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span></div>
<div class="block"><p>Unique identifier for this specific road sign warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToRoadSignInMeters">
<h3>distanceToRoadSignInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToRoadSignInMeters</span></div>
<div class="block"><p>Distance to the road sign in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Type of the road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="category">
<h3>category</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span class="element-name">category</span></div>
<div class="block"><p>The main category to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section class="detail" id="generalWarningType">
<h3>generalWarningType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span class="element-name">generalWarningType</span></div>
<div class="block"><p>Specifies the general warning to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPrioritySign">
<h3>isPrioritySign</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrioritySign</span></div>
<div class="block"><p>Flag indicating if the road sign is a priority sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="vehicleTypes">
<h3>vehicleTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</span> <span class="element-name">vehicleTypes</span></div>
<div class="block"><p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></div>
</section>
</li>
<li>
<section class="detail" id="weatherType">
<h3>weatherType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weatherType</span></div>
<div class="block"><p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></div>
</section>
</li>
<li>
<section class="detail" id="signValue">
<h3>signValue</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">signValue</span></div>
<div class="block"><p>Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="preWarning">
<h3>preWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">preWarning</span></div>
<div class="block"><p>Optional pre-warning in terms of distance, of the upcoming warning or regulation.
 The pre-warning information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="duration">
<h3>duration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">duration</span></div>
<div class="block"><p>Optional length information during which the warning is applicable.
 Usually, this information is shown on a separate shield below the main shield.
 For example, a sign may warn on playing children for a length of 100 m, starting from
 the location of the warning sign.
 The length information (most likely with units) is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="validityTime">
<h3>validityTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">validityTime</span></div>
<div class="block"><p>Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.
 The time information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="roadSignSegment">
<h3>roadSignSegment</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">roadSignSegment</span></div>
<div class="block"><p>The reference to the segment where the road sign is located. It can be used to identify the
 location of the road sign.
 It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
 provided by the <code>NavigableLocationListener</code> or with the <a href="sdk-for-android-navigate-span#getSegmentReference()"><code>Span.getSegmentReference()</code></a>
 available in the Route's Span.
 By combining it with the geometry of the segment, that can be loaded using
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader" title="class in com.here.sdk.mapdata"><code>SegmentDataLoader</code></a>, it is possible to identify the road sign's coordinates.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceType">
<h3>distanceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span></div>
<div class="block"><p>The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for
 passing a road sign. Since the road sign warning is given relative to a single position on
 the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,com.here.sdk.navigation.GeneralWarningRoadSignType,boolean,java.util.List,com.here.sdk.navigation.WeatherType,com.here.sdk.routing.SegmentReference,com.here.sdk.navigation.DistanceType)">
<h3>RoadSignWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoadSignWarning</span><wbr/><span class="parameters">(double distanceToRoadSignInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 boolean isPrioritySign,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> roadSignSegment,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>distanceToRoadSignInMeters</code> - <p>Distance to the road sign in meters.</p></dd>
<dd><code>type</code> - <p>Type of the road sign.</p></dd>
<dd><code>category</code> - <p>The main category to which the road sign belongs.</p></dd>
<dd><code>generalWarningType</code> - <p>Specifies the general warning to which the road sign belongs.</p></dd>
<dd><code>isPrioritySign</code> - <p>Flag indicating if the road sign is a priority sign.</p></dd>
<dd><code>vehicleTypes</code> - <p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></dd>
<dd><code>weatherType</code> - <p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></dd>
<dd><code>roadSignSegment</code> - <p>The reference to the segment where the road sign is located. It can be used to identify the
 location of the road sign.
 It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
 provided by the <code>NavigableLocationListener</code> or with the <a href="sdk-for-android-navigate-span#getSegmentReference()"><code>Span.getSegmentReference()</code></a>
 available in the Route's Span.
 By combining it with the geometry of the segment, that can be loaded using
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader" title="class in com.here.sdk.mapdata"><code>SegmentDataLoader</code></a>, it is possible to identify the road sign's coordinates.</p></dd>
<dd><code>distanceType</code> - <p>The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for
 passing a road sign. Since the road sign warning is given relative to a single position on
 the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></dd>
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
