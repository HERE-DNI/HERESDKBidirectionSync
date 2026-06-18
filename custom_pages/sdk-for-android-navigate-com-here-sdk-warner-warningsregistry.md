---
title: "WarningsRegistry (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warningsregistry"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- WarningsRegistry.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-warner-package-summary">com.here.sdk.warner</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.warner.WarningsRegistry</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">WarningsRegistry</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A class that store warning metadata for different warning types.
 Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.).
 Provided by <code>WarnerEngine</code> so callers can lookup detailed information about specific warnings.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBorderCrossingWarning(com.here.sdk.warner.Warning)">getBorderCrossingWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a border crossing warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-customwarning" title="class in com.here.sdk.warner">CustomWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getCustomWarning(com.here.sdk.warner.Warning)">getCustomWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns additional data associated with the given custom warning.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-dangerzonewarning" title="class in com.here.sdk.navigation">DangerZoneWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDangerZoneWarning(com.here.sdk.warner.Warning)">getDangerZoneWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a danger zone warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-environmentalzonewarning" title="class in com.here.sdk.navigation">EnvironmentalZoneWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getEnvironmentalZoneWarning(com.here.sdk.warner.Warning)">getEnvironmentalZoneWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns environmental zone warning corresponding to the given identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-lanedecreasewarning" title="class in com.here.sdk.warner">LaneDecreaseWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLaneDecreaseWarning(com.here.sdk.warner.Warning)">getLaneDecreaseWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a lane decrease warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLowSpeedZoneWarning(com.here.sdk.warner.Warning)">getLowSpeedZoneWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a low speed zone warning corresponding to the given identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRailwayCrossingWarning(com.here.sdk.warner.Warning)">getRailwayCrossingWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a railway crossing warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRealisticViewWarning(com.here.sdk.warner.Warning)">getRealisticViewWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a realistic-view warning corresponding to the given identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadsignwarning" title="class in com.here.sdk.navigation">RoadSignWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadSignWarning(com.here.sdk.warner.Warning)">getRoadSignWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a road-sign warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSafetyCameraWarning(com.here.sdk.warner.Warning)">getSafetyCameraWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a safety-camera warning corresponding to the given identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-schoolzonewarning" title="class in com.here.sdk.navigation">SchoolZoneWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSchoolZoneWarning(com.here.sdk.warner.Warning)">getSchoolZoneWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a school zone warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-tollstop" title="class in com.here.sdk.navigation">TollStop</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTollStopWarning(com.here.sdk.warner.Warning)">getTollStopWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a toll stop warning corresponding to the given identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficMergeWarning(com.here.sdk.warner.Warning)">getTrafficMergeWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a traffic merge warning corresponding to the given identifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTruckRestrictionWarning(com.here.sdk.warner.Warning)">getTruckRestrictionWarning</a><wbr/>(<a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a truck restrictions warning corresponding to the given identifier.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getSafetyCameraWarning(com.here.sdk.warner.Warning)">
<h3>getSafetyCameraWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a></span> <span class="element-name">getSafetyCameraWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a safety-camera warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single safety-camera warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-safetycamerawarning" title="class in com.here.sdk.navigation"><code>SafetyCameraWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictionWarning(com.here.sdk.warner.Warning)">
<h3>getTruckRestrictionWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a></span> <span class="element-name">getTruckRestrictionWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a truck restrictions warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single truck restrictions warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-truckrestrictionwarning" title="class in com.here.sdk.navigation"><code>TruckRestrictionWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSignWarning(com.here.sdk.warner.Warning)">
<h3>getRoadSignWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsignwarning" title="class in com.here.sdk.navigation">RoadSignWarning</a></span> <span class="element-name">getRoadSignWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a road-sign warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single road sign warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>sdk.navigation.RoadSignWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealisticViewWarning(com.here.sdk.warner.Warning)">
<h3>getRealisticViewWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a></span> <span class="element-name">getRealisticViewWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a realistic-view warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single realistic-view warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnvironmentalZoneWarning(com.here.sdk.warner.Warning)">
<h3>getEnvironmentalZoneWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-environmentalzonewarning" title="class in com.here.sdk.navigation">EnvironmentalZoneWarning</a></span> <span class="element-name">getEnvironmentalZoneWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns environmental zone warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single environmental zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-environmentalzonewarning" title="class in com.here.sdk.navigation"><code>EnvironmentalZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchoolZoneWarning(com.here.sdk.warner.Warning)">
<h3>getSchoolZoneWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarning" title="class in com.here.sdk.navigation">SchoolZoneWarning</a></span> <span class="element-name">getSchoolZoneWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a school zone warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single school zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-schoolzonewarning" title="class in com.here.sdk.navigation"><code>SchoolZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTollStopWarning(com.here.sdk.warner.Warning)">
<h3>getTollStopWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tollstop" title="class in com.here.sdk.navigation">TollStop</a></span> <span class="element-name">getTollStopWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a toll stop warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single toll stop warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-tollstop" title="class in com.here.sdk.navigation"><code>TollStop</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDangerZoneWarning(com.here.sdk.warner.Warning)">
<h3>getDangerZoneWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-dangerzonewarning" title="class in com.here.sdk.navigation">DangerZoneWarning</a></span> <span class="element-name">getDangerZoneWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a danger zone warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single danger zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-dangerzonewarning" title="class in com.here.sdk.navigation"><code>DangerZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBorderCrossingWarning(com.here.sdk.warner.Warning)">
<h3>getBorderCrossingWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a></span> <span class="element-name">getBorderCrossingWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a border crossing warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single border crossing warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRailwayCrossingWarning(com.here.sdk.warner.Warning)">
<h3>getRailwayCrossingWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a></span> <span class="element-name">getRailwayCrossingWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a railway crossing warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single railway crossing warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-railwaycrossingwarning" title="class in com.here.sdk.navigation"><code>RailwayCrossingWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLowSpeedZoneWarning(com.here.sdk.warner.Warning)">
<h3>getLowSpeedZoneWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a></span> <span class="element-name">getLowSpeedZoneWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a low speed zone warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single low speed zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-lowspeedzonewarning" title="class in com.here.sdk.navigation"><code>LowSpeedZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficMergeWarning(com.here.sdk.warner.Warning)">
<h3>getTrafficMergeWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a></span> <span class="element-name">getTrafficMergeWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a traffic merge warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single traffic merge warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>sdk.navigation.TrafficMergeWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLaneDecreaseWarning(com.here.sdk.warner.Warning)">
<h3>getLaneDecreaseWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lanedecreasewarning" title="class in com.here.sdk.warner">LaneDecreaseWarning</a></span> <span class="element-name">getLaneDecreaseWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns a lane decrease warning corresponding to the given identifier.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single lane decrease warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>LaneDecreaseWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.
     </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomWarning(com.here.sdk.warner.Warning)">
<h3>getCustomWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-customwarning" title="class in com.here.sdk.warner">CustomWarning</a></span> <span class="element-name">getCustomWarning</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div class="block"><p>Returns additional data associated with the given custom warning.
 </p><p>The provided <code>warning</code> identifies a specific custom warning instance by its
 base warning information and custom warning type. This information is used
 to resolve the corresponding entry in the warning registry and retrieve
 any additional, type-specific data associated with the warning.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The <a href="sdk-for-android-navigate-warning" title="class in com.here.sdk.warner"><code>Warning</code></a> instance identifying the custom warning for which
     additional data should be retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>CustomWarning</code> associated with the given <code>warning</code>, or <code>null</code>
     if no additional data exists for this warning.
     The returned object contains the payload with type-specific
     details and attributes of the corresponding warning.
     </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
