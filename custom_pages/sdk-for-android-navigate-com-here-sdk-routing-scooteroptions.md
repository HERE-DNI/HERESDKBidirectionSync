---
title: "ScooterOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-scooteroptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ScooterOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.ScooterOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public final class </span><span className="element-name type-name-label">ScooterOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>RoutingOptions</code> class instead.</p></div>
</div>
<div className="block"><p>All the options to specify how a scooter route should be calculated.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#allowHighway">allowHighway</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies whether scooter is allowed on highway or not.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#avoidanceOptions">avoidanceOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Options to specify restrictions for route calculations.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#engineSizeInCubicCentimeters">engineSizeInCubicCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Engine size of the scooter in cubic centimeters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#lastCharacterOfLicensePlate">lastCharacterOfLicensePlate</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies the last character of a vehicle's license plate, typically used to
 evaluate traffic restrictions in certain environmental or low-emission zones.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#maxSpeedOnSegments">maxSpeedOnSegments</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#occupantsNumber">occupantsNumber</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies the number of occupants in the vehicle, including driver.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#routeOptions">routeOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies the common route calculation options.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#textOptions">textOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#tollOptions">tollOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions#%3Cinit%3E()">ScooterOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
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
<section className="detail" id="routeOptions">
<h3>routeOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></span> <span className="element-name">routeOptions</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies the common route calculation options.</p></div>
</section>
</li>
<li>
<section className="detail" id="textOptions">
<h3>textOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span className="element-name">textOptions</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidanceOptions">
<h3>avoidanceOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></span> <span className="element-name">avoidanceOptions</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Options to specify restrictions for route calculations. By default
 no restrictions are applied.</p></div>
</section>
</li>
<li>
<section className="detail" id="tollOptions">
<h3>tollOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></span> <span className="element-name">tollOptions</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</p></div>
</section>
</li>
<li>
<section className="detail" id="occupantsNumber">
<h3>occupantsNumber</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">occupantsNumber</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies the number of occupants in the vehicle, including driver.
 Shouldn't be less than 1 or greater than 255. Defaults to 1.
 This option is only relevant for Japan and will be ignored for other countries.</p></div>
</section>
</li>
<li>
<section className="detail" id="lastCharacterOfLicensePlate">
<h3>lastCharacterOfLicensePlate</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">lastCharacterOfLicensePlate</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies the last character of a vehicle's license plate, typically used to
 evaluate traffic restrictions in certain environmental or low-emission zones.
 In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
 be restricted on certain days or in certain areas to reduce congestion and emissions.
 When this value is provided, the HERE SDK considers it during route calculation to
 avoid roads or areas where your vehicle may be restricted based on local regulations.
 Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".
 If this value is not set, such license plate-based restrictions are ignored, and
 routing is performed without considering them.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxSpeedOnSegments">
<h3>maxSpeedOnSegments</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</span> <span className="element-name">maxSpeedOnSegments</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="allowHighway">
<h3>allowHighway</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">allowHighway</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
 allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
 Note that there is a similar parameter in <a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a>, to
 disallow highway usage, see <a href="sdk-for-android-navigate-roadfeatures#CONTROLLED_ACCESS_HIGHWAY"><code>RoadFeatures.CONTROLLED_ACCESS_HIGHWAY</code></a>.
 As the avoidance options takes precedence, if this parameter is also used, then
 scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
 However, if no alternative route is possible, the calculated route may use highways.
 In such a case, a <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a> will be provided in the related <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>
 to indicate that the highway usage restriction is violated on this route.
 A few examples:
 1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
 highway usage, a notice is received.
 2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
 highway usage, no notice is received.
 3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
 highway usage, a notice is received.
 4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
 when no route is found without highway usage, a notice is received.</p></div>
</section>
</li>
<li>
<section className="detail" id="engineSizeInCubicCentimeters">
<h3>engineSizeInCubicCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">engineSizeInCubicCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value
 is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the road.
 <strong>Note:</strong> For now, this option is only relevant in Japan and will be ignored
 for other countries. Currently, map data for this option is only available
 for Japan.</p></div>
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
<h3>ScooterOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ScooterOptions</span>()</div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
