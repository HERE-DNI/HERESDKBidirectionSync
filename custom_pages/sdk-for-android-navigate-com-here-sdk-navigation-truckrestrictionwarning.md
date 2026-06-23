---
title: "TruckRestrictionWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TruckRestrictionWarning.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.TruckRestrictionWarning</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TruckRestrictionWarning</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck
 or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#axleCount">axleCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">The axle count for which the current restriction applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-dimensionrestriction" title="class in com.here.sdk.navigation">DimensionRestriction</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#dimensionRestriction">dimensionRestriction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicle dimension restrictions.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceInMeters">distanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The distance from the current location to the restriction.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceType">distanceType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates if the specified truck restriction is ahead of the vehicle or has just passed by.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hazardousMaterials">hazardousMaterials</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of hazardous materials which are restricted on the road section for which the warning applies.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#id">id</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unique identifier for this specific truck restriction warning instance.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timeRule">timeRule</a></code></div>
<div class="col-last even-row-color">
<div class="block">Time rule indicating the time periods for which the restriction applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#trailerCount">trailerCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The trailer count for which the current restriction applies.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#truckRoadType">truckRoadType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Truck road type restriction.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#tunnelCategory">tunnelCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tunnel category.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-weightrestriction" title="class in com.here.sdk.navigation">WeightRestriction</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#weightRestriction">weightRestriction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Weight restriction.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(double,com.here.sdk.navigation.DistanceType)">TruckRestrictionWarning</a><wbr/>(double distanceInMeters,
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isGeneral()">isGeneral</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this truck restriction warning is general.</div>
</div>
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
<div class="block"><p>Unique identifier for this specific truck restriction warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceInMeters">
<h3>distanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceInMeters</span></div>
<div class="block"><p>The distance from the current location to the restriction.</p></div>
</section>
</li>
<li>
<section class="detail" id="weightRestriction">
<h3>weightRestriction</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-weightrestriction" title="class in com.here.sdk.navigation">WeightRestriction</a></span> <span class="element-name">weightRestriction</span></div>
<div class="block"><p>Weight restriction.
 It is <code>null</code> when there is no known weight restriction ahead.</p></div>
</section>
</li>
<li>
<section class="detail" id="dimensionRestriction">
<h3>dimensionRestriction</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-dimensionrestriction" title="class in com.here.sdk.navigation">DimensionRestriction</a></span> <span class="element-name">dimensionRestriction</span></div>
<div class="block"><p>Vehicle dimension restrictions.
 It is <code>null</code> when there is no known dimension restriction ahead.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceType">
<h3>distanceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span></div>
<div class="block"><p>Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-android-navigate-index#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerCount">
<h3>trailerCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">trailerCount</span></div>
<div class="block"><p>The trailer count for which the current restriction applies.
 If the field is 'null' then the current restriction does not have a condition based on trailers count.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeRule">
<h3>timeRule</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span></div>
<div class="block"><p>Time rule indicating the time periods for which the restriction applies.
 If the field is 'null' then the restriction is applicable at anytime.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckRoadType">
<h3>truckRoadType</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a></span> <span class="element-name">truckRoadType</span></div>
<div class="block"><p>Truck road type restriction.</p></div>
</section>
</li>
<li>
<section class="detail" id="hazardousMaterials">
<h3>hazardousMaterials</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span class="element-name">hazardousMaterials</span></div>
<div class="block"><p>The list of hazardous materials which are restricted on the road section for which the warning applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="tunnelCategory">
<h3>tunnelCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span class="element-name">tunnelCategory</span></div>
<div class="block"><p>Tunnel category.</p></div>
</section>
</li>
<li>
<section class="detail" id="axleCount">
<h3>axleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCount</span></div>
<div class="block"><p>The axle count for which the current restriction applies.
 If this field is <code>null</code>, the restriction does not depend on axle count.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.DistanceType)">
<h3>TruckRestrictionWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TruckRestrictionWarning</span><wbr/><span class="parameters">(double distanceInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>distanceInMeters</code> - <p>The distance from the current location to the restriction.</p></dd>
<dd><code>distanceType</code> - <p>Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-android-navigate-index#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></dd>
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
<li>
<section class="detail" id="isGeneral()">
<h3>isGeneral</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isGeneral</span>()</div>
<div class="block"><p>Checks if this truck restriction warning is general.
 A general warning has no specific restriction conditions set.
 Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition.
 This method only checks that no specific conditions are set for the warning.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>true</code> if all restriction fields are null or empty, <code>false</code> otherwise.</p></dd>
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
