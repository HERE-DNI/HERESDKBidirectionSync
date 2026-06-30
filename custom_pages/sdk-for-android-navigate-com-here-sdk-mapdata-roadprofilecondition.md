---
title: "RoadProfileCondition (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadProfileCondition.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapdata.RoadProfileCondition</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoadProfileCondition</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Road profile conditions that must be met for a regulation to apply.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isControlledAccess">isControlledAccess</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, applies only to controlled access roads.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isLimitedAccessRoad">isLimitedAccessRoad</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, applies only to limited access roads.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isMotorisedVehiclesOnly">isMotorisedVehiclesOnly</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, applies only to motorised vehicles only roads.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isMultiplyDigitilized">isMultiplyDigitilized</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, applies only to multiply digitized roads.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isPriorityRoad">isPriorityRoad</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, applies only to priority roads.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isRoadLegallyDivided">isRoadLegallyDivided</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, applies only to legally divided roads.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isRoadPhysicallyDivided">isRoadPhysicallyDivided</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, applies only to physically divided roads.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isRural">isRural</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, applies only to rural roads.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isUnpaved">isUnpaved</a></code></div>
<div class="col-last even-row-color">
<div class="block">If true, applies only to unpaved roads.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#isUrban">isUrban</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If true, applies only to urban roads.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#requiredFunctionalClasses">requiredFunctionalClasses</a></code></div>
<div class="col-last even-row-color">
<div class="block">Functional road classes on which the regulation applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#requiredNumberOfLanes">requiredNumberOfLanes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Range of lane counts for which the regulation applies.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#requiredRouteLevels">requiredRouteLevels</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route levels on which the regulation applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-commercialvehicleroadtype" title="enum class in com.here.sdk.mapdata">CommercialVehicleRoadType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#roadType">roadType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Required road type for the regulation to apply.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#%3Cinit%3E(com.here.sdk.mapdata.CommercialVehicleRoadType,com.here.sdk.core.IntegerRange)">RoadProfileCondition</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapdata-commercialvehicleroadtype" title="enum class in com.here.sdk.mapdata">CommercialVehicleRoadType</a> roadType,
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredNumberOfLanes)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance with specified parameters.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-roadprofilecondition#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="roadType">
<h3>roadType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-commercialvehicleroadtype" title="enum class in com.here.sdk.mapdata">CommercialVehicleRoadType</a></span> <span class="element-name">roadType</span></div>
<div class="block"><p>Required road type for the regulation to apply.</p></div>
</section>
</li>
<li>
<section class="detail" id="requiredFunctionalClasses">
<h3>requiredFunctionalClasses</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a>&gt;</span> <span class="element-name">requiredFunctionalClasses</span></div>
<div class="block"><p>Functional road classes on which the regulation applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="requiredRouteLevels">
<h3>requiredRouteLevels</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a>&gt;</span> <span class="element-name">requiredRouteLevels</span></div>
<div class="block"><p>Route levels on which the regulation applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="requiredNumberOfLanes">
<h3>requiredNumberOfLanes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">requiredNumberOfLanes</span></div>
<div class="block"><p>Range of lane counts for which the regulation applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="isControlledAccess">
<h3>isControlledAccess</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isControlledAccess</span></div>
<div class="block"><p>If true, applies only to controlled access roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isLimitedAccessRoad">
<h3>isLimitedAccessRoad</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isLimitedAccessRoad</span></div>
<div class="block"><p>If true, applies only to limited access roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isMultiplyDigitilized">
<h3>isMultiplyDigitilized</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isMultiplyDigitilized</span></div>
<div class="block"><p>If true, applies only to multiply digitized roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRoadLegallyDivided">
<h3>isRoadLegallyDivided</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isRoadLegallyDivided</span></div>
<div class="block"><p>If true, applies only to legally divided roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRoadPhysicallyDivided">
<h3>isRoadPhysicallyDivided</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isRoadPhysicallyDivided</span></div>
<div class="block"><p>If true, applies only to physically divided roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPriorityRoad">
<h3>isPriorityRoad</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isPriorityRoad</span></div>
<div class="block"><p>If true, applies only to priority roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isUnpaved">
<h3>isUnpaved</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isUnpaved</span></div>
<div class="block"><p>If true, applies only to unpaved roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isMotorisedVehiclesOnly">
<h3>isMotorisedVehiclesOnly</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isMotorisedVehiclesOnly</span></div>
<div class="block"><p>If true, applies only to motorised vehicles only roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isUrban">
<h3>isUrban</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isUrban</span></div>
<div class="block"><p>If true, applies only to urban roads.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRural">
<h3>isRural</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isRural</span></div>
<div class="block"><p>If true, applies only to rural roads.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapdata.CommercialVehicleRoadType,com.here.sdk.core.IntegerRange)">
<h3>RoadProfileCondition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoadProfileCondition</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-commercialvehicleroadtype" title="enum class in com.here.sdk.mapdata">CommercialVehicleRoadType</a> roadType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredNumberOfLanes)</span></div>
<div class="block"><p>Creates a new instance with specified parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roadType</code> - <p>Required road type for the regulation to apply.</p></dd>
<dd><code>requiredNumberOfLanes</code> - <p>Range of lane counts for which the regulation applies.</p></dd>
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
