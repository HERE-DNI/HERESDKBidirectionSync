---
title: "BorderCrossingWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- BorderCrossingWarning.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.BorderCrossingWarning</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">BorderCrossingWarning</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A border crossing. The main field describing the border crossing is <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#type"><code>type</code></a> specifying whether the border crossing
 is given for a country border or a state border. The <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#type"><code>type</code></a> must be known.
 The country and state codes are contained in <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#administrativeRules"><code>administrativeRules</code></a> along with other information such as speed
 limits, u-turn regulations or pre-trip planning information contained by the <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a>.
 </p><p>Use <code>BorderCrossingWarningListener</code> to get notifications about upcoming country or state border crossings.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#administrativeRules">administrativeRules</a></code></div>
<div class="col-last even-row-color">
<div class="block">The administrative rules for the country or state after the border crossing.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-administrativecommercialvehiclerules" title="class in com.here.sdk.mapdata">AdministrativeCommercialVehicleRules</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#commercialVehicleRegulations">commercialVehicleRegulations</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Commercial vehicle regulations for the administrative region after the border crossing.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#distanceToBorderCrossingInMeters">distanceToBorderCrossingInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance to the border crossing in meters.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#distanceType">distanceType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The distance type for the warning, e.g.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#id">id</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unique identifier for this specific border crossing warning instance.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-bordercrossingtype" title="enum class in com.here.sdk.navigation">BorderCrossingType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#type">type</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type of border crossing.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#%3Cinit%3E(double,com.here.sdk.navigation.BorderCrossingType,com.here.sdk.mapdata.AdministrativeRules,com.here.sdk.navigation.DistanceType)">BorderCrossingWarning</a><wbr/>(double distanceToBorderCrossingInMeters,
 <a href="sdk-for-android-navigate-bordercrossingtype" title="enum class in com.here.sdk.navigation">BorderCrossingType</a> type,
 <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a> administrativeRules,
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning#hashCode()">hashCode</a>()</code></div>

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
<div class="block"><p>Unique identifier for this specific border crossing warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToBorderCrossingInMeters">
<h3>distanceToBorderCrossingInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToBorderCrossingInMeters</span></div>
<div class="block"><p>Distance to the border crossing in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bordercrossingtype" title="enum class in com.here.sdk.navigation">BorderCrossingType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Type of border crossing.</p></div>
</section>
</li>
<li>
<section class="detail" id="administrativeRules">
<h3>administrativeRules</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span class="element-name">administrativeRules</span></div>
<div class="block"><p>The administrative rules for the country or state after the border crossing. It contains information regarding
 rules such as driving side, speed limits, various sticker requirements, toll costs and others.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceType">
<h3>distanceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span></div>
<div class="block"><p>The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for
 passing a border crossing. Since the border crossing warning is given relative to a single position on
 the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></div>
</section>
</li>
<li>
<section class="detail" id="commercialVehicleRegulations">
<h3>commercialVehicleRegulations</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-administrativecommercialvehiclerules" title="class in com.here.sdk.mapdata">AdministrativeCommercialVehicleRules</a></span> <span class="element-name">commercialVehicleRegulations</span></div>
<div class="block"><p>Commercial vehicle regulations for the administrative region after the border crossing.
 Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles.
 This field is only populated when crossing into a region with specific commercial vehicle regulations.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.BorderCrossingType,com.here.sdk.mapdata.AdministrativeRules,com.here.sdk.navigation.DistanceType)">
<h3>BorderCrossingWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BorderCrossingWarning</span><wbr/><span class="parameters">(double distanceToBorderCrossingInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-bordercrossingtype" title="enum class in com.here.sdk.navigation">BorderCrossingType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a> administrativeRules,
 @NonNull
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>distanceToBorderCrossingInMeters</code> - <p>Distance to the border crossing in meters.</p></dd>
<dd><code>type</code> - <p>Type of border crossing.</p></dd>
<dd><code>administrativeRules</code> - <p>The administrative rules for the country or state after the border crossing. It contains information regarding
 rules such as driving side, speed limits, various sticker requirements, toll costs and others.</p></dd>
<dd><code>distanceType</code> - <p>The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for
 passing a border crossing. Since the border crossing warning is given relative to a single position on
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
