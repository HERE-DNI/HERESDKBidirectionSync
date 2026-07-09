---
title: "RoadSign (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsign"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoadSign.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RoadSign</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoadSign</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Describes a road sign.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#generalWarningType">generalWarningType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the general warning to which the road sign belongs.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#isPrioritySign">isPrioritySign</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Flag indicating if the road sign is a priority sign.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedDuration">localizedDuration</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional length information during which the warning is applicable.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedPreWarning">localizedPreWarning</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional pre-warning in terms of distance, of the upcoming warning or regulation.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedSignValue">localizedSignValue</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedValidityTime">localizedValidityTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#offsetInMeters">offsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#roadSignCategory">roadSignCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The main category to which the road sign belongs.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#roadSignType">roadSignType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Type of the road sign.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#travelDirection">travelDirection</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Segment direction which the road sign is applied.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#vehicleTypes">vehicleTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies a list of vehicle types for which the road sign is applicable.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#weatherType">weatherType</a></code></div>
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#%3Cinit%3E(int,com.here.sdk.routing.TravelDirection,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,boolean,com.here.sdk.navigation.GeneralWarningRoadSignType,java.util.List,com.here.sdk.navigation.WeatherType)">RoadSign</a><wbr/>(int offsetInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> roadSignType,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> roadSignCategory,
 boolean isPrioritySign,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance with default values.</div>
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
<section className="detail" id="offsetInMeters">
<h3>offsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">offsetInMeters</span></div>
<div className="block"><p>The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</p></div>
</section>
</li>
<li>
<section className="detail" id="travelDirection">
<h3>travelDirection</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span className="element-name">travelDirection</span></div>
<div className="block"><p>Segment direction which the road sign is applied.</p></div>
</section>
</li>
<li>
<section className="detail" id="roadSignType">
<h3>roadSignType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span className="element-name">roadSignType</span></div>
<div className="block"><p>Type of the road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="roadSignCategory">
<h3>roadSignCategory</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span className="element-name">roadSignCategory</span></div>
<div className="block"><p>The main category to which the road sign belongs.</p></div>
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
<section className="detail" id="generalWarningType">
<h3>generalWarningType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span className="element-name">generalWarningType</span></div>
<div className="block"><p>Specifies the general warning to which the road sign belongs.</p></div>
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
<section className="detail" id="localizedSignValue">
<h3>localizedSignValue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">localizedSignValue</span></div>
<div className="block"><p>Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="localizedPreWarning">
<h3>localizedPreWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">localizedPreWarning</span></div>
<div className="block"><p>Optional pre-warning in terms of distance, of the upcoming warning or regulation.
 The pre-warning information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="localizedDuration">
<h3>localizedDuration</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">localizedDuration</span></div>
<div className="block"><p>Optional length information during which the warning is applicable.
 Usually, this information is shown on a separate shield below the main shield.
 For example, a sign may warn on playing children for a length of 100 m, starting from
 the location of the warning sign.
 The length information (most likely with units) is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section className="detail" id="localizedValidityTime">
<h3>localizedValidityTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span className="element-name">localizedValidityTime</span></div>
<div className="block"><p>Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.
 The time information is given as printed on the local road sign.</p></div>
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
<section className="detail" id="&lt;init&gt;(int,com.here.sdk.routing.TravelDirection,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,boolean,com.here.sdk.navigation.GeneralWarningRoadSignType,java.util.List,com.here.sdk.navigation.WeatherType)">
<h3>RoadSign</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoadSign</span><wbr/><span className="parameters">(int offsetInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> roadSignType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> roadSignCategory,
 boolean isPrioritySign,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType)</span></div>
<div className="block"><p>Creates a new instance with default values.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>offsetInMeters</code> - <p>The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</p></dd>
<dd><code>travelDirection</code> - <p>Segment direction which the road sign is applied.</p></dd>
<dd><code>roadSignType</code> - <p>Type of the road sign.</p></dd>
<dd><code>roadSignCategory</code> - <p>The main category to which the road sign belongs.</p></dd>
<dd><code>isPrioritySign</code> - <p>Flag indicating if the road sign is a priority sign.</p></dd>
<dd><code>generalWarningType</code> - <p>Specifies the general warning to which the road sign belongs.</p></dd>
<dd><code>vehicleTypes</code> - <p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></dd>
<dd><code>weatherType</code> - <p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></dd>
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
