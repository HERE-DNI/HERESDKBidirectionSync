---
title: "WarningOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warningoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- WarningOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.warner.WarningOptions</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">WarningOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class with options to configure <a href="sdk-for-android-navigate-warnerengine#getWarningOptions()"><code>WarnerEngine.getWarningOptions()</code></a>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#borderCrossingWarningOptions">borderCrossingWarningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Border crossing warning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-lanedecreasewarningoptions" title="class in com.here.sdk.warner">LaneDecreaseWarningOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#laneDecreaseWarningOptions">laneDecreaseWarningOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A struct that provides lane decrease warning options.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#realisticViewWarningOptions">realisticViewWarningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Realistic view warning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#roadSignWarningOptions">roadSignWarningOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A struct that provides road sign warning options.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#safetyCameraWarningOptions">safetyCameraWarningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Safety camera warning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#schoolZoneWarningOptions">schoolZoneWarningOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">School zone warning options.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#trafficMergeWarningOptions">trafficMergeWarningOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">A struct that provides traffic merge warning options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#truckRestrictionsWarningOptions">truckRestrictionsWarningOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Truck restrictions warning options.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#%3Cinit%3E(com.here.sdk.navigation.SafetyCameraWarningOptions,com.here.sdk.navigation.TruckRestrictionsWarningOptions,com.here.sdk.navigation.RoadSignWarningOptions,com.here.sdk.navigation.RealisticViewWarningOptions,com.here.sdk.navigation.SchoolZoneWarningOptions,com.here.sdk.navigation.BorderCrossingWarningOptions,com.here.sdk.navigation.TrafficMergeWarningOptions,com.here.sdk.warner.LaneDecreaseWarningOptions)">WarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> safetyCameraWarningOptions,
 <a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> truckRestrictionsWarningOptions,
 <a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> roadSignWarningOptions,
 <a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> realisticViewWarningOptions,
 <a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> schoolZoneWarningOptions,
 <a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> borderCrossingWarningOptions,
 <a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> trafficMergeWarningOptions,
 <a href="sdk-for-android-navigate-lanedecreasewarningoptions" title="class in com.here.sdk.warner">LaneDecreaseWarningOptions</a> laneDecreaseWarningOptions)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-warner-warningoptions#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="safetyCameraWarningOptions">
<h3>safetyCameraWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span class="element-name">safetyCameraWarningOptions</span></div>
<div class="block"><p>Safety camera warning options. Set the options in order to enable them.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckRestrictionsWarningOptions">
<h3>truckRestrictionsWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span class="element-name">truckRestrictionsWarningOptions</span></div>
<div class="block"><p>Truck restrictions warning options.</p></div>
</section>
</li>
<li>
<section class="detail" id="roadSignWarningOptions">
<h3>roadSignWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span class="element-name">roadSignWarningOptions</span></div>
<div class="block"><p>A struct that provides road sign warning options.
 Set the options for filtering of road sign notifications.</p></div>
</section>
</li>
<li>
<section class="detail" id="realisticViewWarningOptions">
<h3>realisticViewWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span class="element-name">realisticViewWarningOptions</span></div>
<div class="block"><p>Realistic view warning options.
 Set the options for filtering the realistic view notifications and
 setting the realistic view notification distances based on the road type.</p></div>
</section>
</li>
<li>
<section class="detail" id="schoolZoneWarningOptions">
<h3>schoolZoneWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span class="element-name">schoolZoneWarningOptions</span></div>
<div class="block"><p>School zone warning options.
 Set the options for configuring of school zone notifications.</p></div>
</section>
</li>
<li>
<section class="detail" id="borderCrossingWarningOptions">
<h3>borderCrossingWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span class="element-name">borderCrossingWarningOptions</span></div>
<div class="block"><p>Border crossing warning options.</p></div>
</section>
</li>
<li>
<section class="detail" id="trafficMergeWarningOptions">
<h3>trafficMergeWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span class="element-name">trafficMergeWarningOptions</span></div>
<div class="block"><p>A struct that provides traffic merge warning options.
 Set the options for filtering the traffic merge notifications.</p></div>
</section>
</li>
<li>
<section class="detail" id="laneDecreaseWarningOptions">
<h3>laneDecreaseWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lanedecreasewarningoptions" title="class in com.here.sdk.warner">LaneDecreaseWarningOptions</a></span> <span class="element-name">laneDecreaseWarningOptions</span></div>
<div class="block"><p>A struct that provides lane decrease warning options.
 Set the options for filtering the lane decrease notifications.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.SafetyCameraWarningOptions,com.here.sdk.navigation.TruckRestrictionsWarningOptions,com.here.sdk.navigation.RoadSignWarningOptions,com.here.sdk.navigation.RealisticViewWarningOptions,com.here.sdk.navigation.SchoolZoneWarningOptions,com.here.sdk.navigation.BorderCrossingWarningOptions,com.here.sdk.navigation.TrafficMergeWarningOptions,com.here.sdk.warner.LaneDecreaseWarningOptions)">
<h3>WarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> safetyCameraWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> truckRestrictionsWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> roadSignWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> realisticViewWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> schoolZoneWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> borderCrossingWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> trafficMergeWarningOptions,
 @NonNull
 <a href="sdk-for-android-navigate-lanedecreasewarningoptions" title="class in com.here.sdk.warner">LaneDecreaseWarningOptions</a> laneDecreaseWarningOptions)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>safetyCameraWarningOptions</code> - <p>Safety camera warning options. Set the options in order to enable them.</p></dd>
<dd><code>truckRestrictionsWarningOptions</code> - <p>Truck restrictions warning options.</p></dd>
<dd><code>roadSignWarningOptions</code> - <p>A struct that provides road sign warning options.
 Set the options for filtering of road sign notifications.</p></dd>
<dd><code>realisticViewWarningOptions</code> - <p>Realistic view warning options.
 Set the options for filtering the realistic view notifications and
 setting the realistic view notification distances based on the road type.</p></dd>
<dd><code>schoolZoneWarningOptions</code> - <p>School zone warning options.
 Set the options for configuring of school zone notifications.</p></dd>
<dd><code>borderCrossingWarningOptions</code> - <p>Border crossing warning options.</p></dd>
<dd><code>trafficMergeWarningOptions</code> - <p>A struct that provides traffic merge warning options.
 Set the options for filtering the traffic merge notifications.</p></dd>
<dd><code>laneDecreaseWarningOptions</code> - <p>A struct that provides lane decrease warning options.
 Set the options for filtering the lane decrease notifications.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
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
