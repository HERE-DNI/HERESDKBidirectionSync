---
title: "PickMapContentResult.VehicleRestrictionResult (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PickMapContentResult.VehicleRestrictionResult.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.PickMapContentResult.VehicleRestrictionResult</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult" title="class in com.here.sdk.mapview">PickMapContentResult</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">PickMapContentResult.VehicleRestrictionResult</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Carries the result of picking a vehicle restriction object.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#coordinates">coordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">The geographic coordinates of the vehicle restriction.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#countryCode">countryCode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Country code.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#vehicleRestriction">vehicleRestriction</a></code></div>
<div class="col-last even-row-color">
<div class="block">The vehicle restriction details.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.CountryCode,com.here.sdk.transport.VehicleRestriction)">VehicleRestrictionResult</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode,
 <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.transport.VehicleRestriction)">VehicleRestrictionResult</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</code></div>
<div class="col-last odd-row-color">
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
<section class="detail" id="coordinates">
<h3>coordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span></div>
<div class="block"><p>The geographic coordinates of the vehicle restriction.</p></div>
</section>
</li>
<li>
<section class="detail" id="countryCode">
<h3>countryCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span class="element-name">countryCode</span></div>
<div class="block"><p>Country code.</p></div>
</section>
</li>
<li>
<section class="detail" id="vehicleRestriction">
<h3>vehicleRestriction</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a></span> <span class="element-name">vehicleRestriction</span></div>
<div class="block"><p>The vehicle restriction details.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.transport.VehicleRestriction)">
<h3>VehicleRestrictionResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestrictionResult</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the vehicle restriction.</p></dd>
<dd><code>vehicleRestriction</code> - <p>The vehicle restriction details.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.CountryCode,com.here.sdk.transport.VehicleRestriction)">
<h3>VehicleRestrictionResult</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestrictionResult</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the vehicle restriction.</p></dd>
<dd><code>countryCode</code> - <p>Country code.</p></dd>
<dd><code>vehicleRestriction</code> - <p>The vehicle restriction details.</p></dd>
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
