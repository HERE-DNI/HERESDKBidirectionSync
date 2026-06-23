---
title: "VehicleRestrictionIconProperties (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-vehiclerestrictioniconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VehicleRestrictionIconProperties.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.VehicleRestrictionIconProperties</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleRestrictionIconProperties</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Encapsulates properties for generating vehicle restriction icons
 using <code>IconProvider</code>.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#countryCode">countryCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies country specific version of the icon.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#restriction">restriction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicle restriction to generate icon for.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.transport.VehicleRestriction)">VehicleRestrictionIconProperties</a><wbr/>(<a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> restriction)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates icon properties for specified restriction.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.transport.VehicleRestriction,com.here.sdk.core.CountryCode)">VehicleRestrictionIconProperties</a><wbr/>(<a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> restriction,
 <a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates icon properties for specified restriction and country.</div>
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
<section class="detail" id="restriction">
<h3>restriction</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a></span> <span class="element-name">restriction</span></div>
<div class="block"><p>Vehicle restriction to generate icon for.</p></div>
</section>
</li>
<li>
<section class="detail" id="countryCode">
<h3>countryCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span class="element-name">countryCode</span></div>
<div class="block"><p>Specifies country specific version of the icon. Ignored
 if there is no country specific version of requested icon.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.transport.VehicleRestriction)">
<h3>VehicleRestrictionIconProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestrictionIconProperties</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> restriction)</span></div>
<div class="block"><p>Creates icon properties for specified restriction.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>restriction</code> - <p>Vehicle restriction to generate icon for.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.transport.VehicleRestriction,com.here.sdk.core.CountryCode)">
<h3>VehicleRestrictionIconProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestrictionIconProperties</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> restriction,
 @Nullable
 <a href="sdk-for-android-navigate-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode)</span></div>
<div class="block"><p>Creates icon properties for specified restriction and country.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>restriction</code> - <p>Vehicle restriction to generate icon for.</p></dd>
<dd><code>countryCode</code> - <p>Specifies country specific version of the icon. Ignored
 if there is no country specific version of requested icon.</p></dd>
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
