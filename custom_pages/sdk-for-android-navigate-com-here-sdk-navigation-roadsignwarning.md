---
title: "RoadSignWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoadSignWarning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RoadSignWarning</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoadSignWarning</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A road sign. The main field describing the sign is <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type"><code>type</code></a>. Some road types are standardized, others can be country specific.
 A valid road sign contains known <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type"><code>type</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#category"><code>category</code></a>.
 Use <code>RoadSignWarningListener</code> to get notifications with current road signs.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#category">category</a></code></div>
<div className="col-last even-row-color">
<div className="block">The main category to which the road sign belongs.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceToRoadSignInMeters">distanceToRoadSignInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Distance to the road sign in meters.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#distanceType">distanceType</a></code></div>
<div className="col-last even-row-color">
<div className="block">The distance type for the warning, e.g.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#duration">duration</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional length information during which the warning is applicable.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#generalWarningType">generalWarningType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the general warning to which the road sign belongs.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#id">id</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unique identifier for this specific road sign warning instance.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#isPrioritySign">isPrioritySign</a></code></div>
<div className="col-last even-row-color">
<div className="block">Flag indicating if the road sign is a priority sign.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#preWarning">preWarning</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional pre-warning in terms of distance, of the upcoming warning or regulation.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#roadSignSegment">roadSignSegment</a></code></div>
<div className="col-last even-row-color">
<div className="block">The reference to the segment where the road sign is located.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#signValue">signValue</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#type">type</a></code></div>
<div className="col-last even-row-color">
<div className="block">Type of the road sign.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#validityTime">validityTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#vehicleTypes">vehicleTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies a list of vehicle types for which the road sign is applicable.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#weatherType">weatherType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Specifies the weather type for which the sign is applicable.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning#%3Cinit%3E(double,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,com.here.sdk.navigation.GeneralWarningRoadSignType,boolean,java.util.List,com.here.sdk.navigation.WeatherType,com.here.sdk.routing.SegmentReference,com.here.sdk.navigation.DistanceType)">RoadSignWarning</a><wbr/>(double distanceToRoadSignInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> category,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 boolean isPrioritySign,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> roadSignSegment,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
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
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">id</span></div>
<div className="block"><p>Unique identifier for this specific road sign warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceToRoadSignInMeters">
<h3>distanceToRoadSignInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceToRoadSignInMeters</span></div>
<div className="block"><p>Distance to the road sign in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Type of the road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="category">
<h3>category</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span className="element-name">category</span></div>
<div className="block"><p>The main category to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section className="detail" id="generalWarningType">
<h3>generalWarningType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span className="element-name">generalWarningType</span></div>
<div className="block"><p>Specifies the general warning to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section className="detail" id="isPrioritySign">
<h3>isPrioritySign</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isPrioritySign</span></div>
<div className="block"><p>Flag indicating if the road sign is a priority sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="vehicleTypes">
<h3>vehicleTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</span> <span className="element-name">vehicleTypes</span></div>
<div className="block"><p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></div>
</section>
</li>
<li>
<section className="detail" id="weatherType">
<h3>weatherType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span className="element-name">weatherType</span></div>
<div className="block"><p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></div>
</section>
</li>
<li>
<section className="detail" id="signValue">
<h3>signValue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">signValue</span></div>
<div className="block"><p>Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="preWarning">
<h3>preWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">preWarning</span></div>
<div className="block"><p>Optional pre-warning in terms of distance, of the upcoming warning or regulation.
 The pre-warning information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="duration">
<h3>duration</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">duration</span></div>
<div className="block"><p>Optional length information during which the warning is applicable.
 Usually, this information is shown on a separate shield below the main shield.
 For example, a sign may warn on playing children for a length of 100 m, starting from
 the location of the warning sign.
 The length information (most likely with units) is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="validityTime">
<h3>validityTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">validityTime</span></div>
<div className="block"><p>Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.
 The time information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="roadSignSegment">
<h3>roadSignSegment</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">roadSignSegment</span></div>
<div className="block"><p>The reference to the segment where the road sign is located. It can be used to identify the
 location of the road sign.
 It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
 provided by the <code>NavigableLocationListener</code> or with the <a href="sdk-for-android-navigate-span#getSegmentReference()"><code>Span.getSegmentReference()</code></a>
 available in the Route's Span.
 By combining it with the geometry of the segment, that can be loaded using
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader" title="class in com.here.sdk.mapdata"><code>SegmentDataLoader</code></a>, it is possible to identify the road sign's coordinates.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceType">
<h3>distanceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span className="element-name">distanceType</span></div>
<div className="block"><p>The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for
 passing a road sign. Since the road sign warning is given relative to a single position on
 the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,com.here.sdk.navigation.GeneralWarningRoadSignType,boolean,java.util.List,com.here.sdk.navigation.WeatherType,com.here.sdk.routing.SegmentReference,com.here.sdk.navigation.DistanceType)">
<h3>RoadSignWarning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoadSignWarning</span><wbr/><span className="parameters">(double distanceToRoadSignInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 boolean isPrioritySign,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> roadSignSegment,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
