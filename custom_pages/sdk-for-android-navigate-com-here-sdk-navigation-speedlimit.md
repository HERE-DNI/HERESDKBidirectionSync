---
title: "SpeedLimit (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedlimit"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SpeedLimit.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.SpeedLimit</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SpeedLimit</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents the speed limit of the current road.
 Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits,
 the HERE SDK internally reads the current device time and notifies only on speed limits
 that are currently active.
 </p><p>It is recommended to use <a href="sdk-for-android-navigate-index#effectiveSpeedLimitInMetersPerSecond()"><code>effectiveSpeedLimitInMetersPerSecond()</code></a> when
 an application does not offer dedicated speed limit indicators for other cases, such as
 weather-dependent speed limits.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#advisorySpeedLimitInMetersPerSecond">advisorySpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">A recommended speed limit that may not be indicated on the local road signs,
 but that serves to warn a driver that the road conditions may indicate a lower speed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#fogSpeedLimitInMetersPerSecond">fogSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#optimalWeatherSpeedLimitInMetersPerSecond">optimalWeatherSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#rainSpeedLimitInMetersPerSecond">rainSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#schoolZoneSpeedLimitInMetersPerSecond">schoolZoneSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#snowSpeedLimitInMetersPerSecond">snowSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">Regular speed limit if available.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timeDependentSpeedLimitInMetersPerSecond">timeDependentSpeedLimitInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A conditional speed limit as indicated on the local road signs.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">SpeedLimit</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#effectiveSpeedLimitInMetersPerSecond()">effectiveSpeedLimitInMetersPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the effective (lowest) speed limit between <a href="sdk-for-android-navigate-index#speedLimitInMetersPerSecond"><code>speedLimitInMetersPerSecond</code></a>,
 <a href="sdk-for-android-navigate-index#schoolZoneSpeedLimitInMetersPerSecond"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>, <a href="sdk-for-android-navigate-index#timeDependentSpeedLimitInMetersPerSecond"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>
 and <a href="sdk-for-android-navigate-index#optimalWeatherSpeedLimitInMetersPerSecond"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedLimitInMetersPerSecond</span></div>
<div class="block"><p>Regular speed limit if available. In case of unbounded speed limit, the value is zero.
 </p><p><strong>Note:</strong>
 When following a route, then this value will depend on the selected transport mode.
 For other speed limits, like weather-dependent speed limits only the value as shown
 on the local road sign is provided. It may not be applicable to all transport modes.
 For tracking mode (without following a route), the VehicleProfile is ignored and only
 the speed limit from the local road sign is provided or the regular speed limit
 for a particular type of road or area like regular inner-city speed limits.</p></div>
</section>
</li>
<li>
<section class="detail" id="advisorySpeedLimitInMetersPerSecond">
<h3>advisorySpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">advisorySpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A recommended speed limit that may not be indicated on the local road signs,
 but that serves to warn a driver that the road conditions may indicate a lower speed.
 Typically, the road condition is a curved road or a ramp but it may be due to a narrow road,
 narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a
 different road than the one for which it applies (this can happen with ramps). In this case,
 the advisory speed is indicated for the road for which it is intended, even if the sign is
 further than 50 meters from the particular road.
 <ul>
<li>Advisory speed signs due to construction are not included.</li>
<li>A speed value is published for advisory signs.</li>
</ul>
</p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="snowSpeedLimitInMetersPerSecond">
<h3>snowSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">snowSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when there is snow on the road.
 </p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="rainSpeedLimitInMetersPerSecond">
<h3>rainSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">rainSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when it is raining or there is water on the road.
 </p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="fogSpeedLimitInMetersPerSecond">
<h3>fogSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">fogSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when the visibility decreases due to fog.
 </p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="optimalWeatherSpeedLimitInMetersPerSecond">
<h3>optimalWeatherSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">optimalWeatherSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when the visibility is optimal due to weather
 conditions.
 </p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.
 </p><p><strong>Note:</strong>
 This speed limit is conditioned by factors not expressed by the other ones.
 For example, it may be a time-related speed limit or a vehicle-related one.</p></div>
</section>
</li>
<li>
<section class="detail" id="schoolZoneSpeedLimitInMetersPerSecond">
<h3>schoolZoneSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">schoolZoneSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 School zone signs are often placed to slow drivers before reaching an intersection where
 children are crossing.
 </p><p>A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeDependentSpeedLimitInMetersPerSecond">
<h3>timeDependentSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">timeDependentSpeedLimitInMetersPerSecond</span></div>
<div class="block"><p>A conditional speed limit as indicated on the local road signs.
 Speed limit that is in effect considering the current local time provided by the device's
 clock.</p></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>SpeedLimit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SpeedLimit</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
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
<section class="detail" id="effectiveSpeedLimitInMetersPerSecond()">
<h3>effectiveSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">effectiveSpeedLimitInMetersPerSecond</span>()</div>
<div class="block"><p>Returns the effective (lowest) speed limit between <a href="sdk-for-android-navigate-index#speedLimitInMetersPerSecond"><code>speedLimitInMetersPerSecond</code></a>,
 <a href="sdk-for-android-navigate-index#schoolZoneSpeedLimitInMetersPerSecond"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>, <a href="sdk-for-android-navigate-index#timeDependentSpeedLimitInMetersPerSecond"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>
 and <a href="sdk-for-android-navigate-index#optimalWeatherSpeedLimitInMetersPerSecond"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Returns the lowest value between: <a href="sdk-for-android-navigate-index#speedLimitInMetersPerSecond"><code>speedLimitInMetersPerSecond</code></a>,
     <a href="sdk-for-android-navigate-index#schoolZoneSpeedLimitInMetersPerSecond"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>, <a href="sdk-for-android-navigate-index#timeDependentSpeedLimitInMetersPerSecond"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>
     and <a href="sdk-for-android-navigate-index#optimalWeatherSpeedLimitInMetersPerSecond"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>.</p></dd>
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
