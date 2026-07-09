---
title: "SpeedLimit (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedlimit"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SpeedLimit.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.SpeedLimit</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SpeedLimit</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents the speed limit of the current road.
 Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits,
 the HERE SDK internally reads the current device time and notifies only on speed limits
 that are currently active.
 It is recommended to use <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#effectiveSpeedLimitInMetersPerSecond()"><code>effectiveSpeedLimitInMetersPerSecond()</code></a> when
 an application does not offer dedicated speed limit indicators for other cases, such as
 weather-dependent speed limits.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#advisorySpeedLimitInMetersPerSecond">advisorySpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">A recommended speed limit that may not be indicated on the local road signs,
 but that serves to warn a driver that the road conditions may indicate a lower speed.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#fogSpeedLimitInMetersPerSecond">fogSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#optimalWeatherSpeedLimitInMetersPerSecond">optimalWeatherSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#rainSpeedLimitInMetersPerSecond">rainSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#schoolZoneSpeedLimitInMetersPerSecond">schoolZoneSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#snowSpeedLimitInMetersPerSecond">snowSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Regular speed limit if available.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#timeDependentSpeedLimitInMetersPerSecond">timeDependentSpeedLimitInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A conditional speed limit as indicated on the local road signs.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#%3Cinit%3E()">SpeedLimit</a>()</code></div>
<div className="col-last even-row-color">
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
<section className="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">speedLimitInMetersPerSecond</span></div>
<div className="block"><p>Regular speed limit if available. In case of unbounded speed limit, the value is zero.
 <strong>Note:</strong>
 When following a route, then this value will depend on the selected transport mode.
 For other speed limits, like weather-dependent speed limits only the value as shown
 on the local road sign is provided. It may not be applicable to all transport modes.
 For tracking mode (without following a route), the VehicleProfile is ignored and only
 the speed limit from the local road sign is provided or the regular speed limit
 for a particular type of road or area like regular inner-city speed limits.</p></div>
</section>
</li>
<li>
<section className="detail" id="advisorySpeedLimitInMetersPerSecond">
<h3>advisorySpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">advisorySpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A recommended speed limit that may not be indicated on the local road signs,
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
A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="snowSpeedLimitInMetersPerSecond">
<h3>snowSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">snowSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when there is snow on the road.
 A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="rainSpeedLimitInMetersPerSecond">
<h3>rainSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">rainSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when it is raining or there is water on the road.
 A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="fogSpeedLimitInMetersPerSecond">
<h3>fogSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">fogSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when the visibility decreases due to fog.
 A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="optimalWeatherSpeedLimitInMetersPerSecond">
<h3>optimalWeatherSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">optimalWeatherSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 The road speed limit that is in effect only when the visibility is optimal due to weather
 conditions.
 A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.
 <strong>Note:</strong>
 This speed limit is conditioned by factors not expressed by the other ones.
 For example, it may be a time-related speed limit or a vehicle-related one.</p></div>
</section>
</li>
<li>
<section className="detail" id="schoolZoneSpeedLimitInMetersPerSecond">
<h3>schoolZoneSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">schoolZoneSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 School zone signs are often placed to slow drivers before reaching an intersection where
 children are crossing.
 A possible usage example can be to show an icon on the device's screen containing both
 special speed limit value and a visual cue in order to warn the user about the conditional
 speed limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="timeDependentSpeedLimitInMetersPerSecond">
<h3>timeDependentSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">timeDependentSpeedLimitInMetersPerSecond</span></div>
<div className="block"><p>A conditional speed limit as indicated on the local road signs.
 Speed limit that is in effect considering the current local time provided by the device's
 clock.</p></div>
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
<h3>SpeedLimit</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SpeedLimit</span>()</div>
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
<li>
<section className="detail" id="effectiveSpeedLimitInMetersPerSecond()">
<h3>effectiveSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">effectiveSpeedLimitInMetersPerSecond</span>()</div>
<div className="block"><p>Returns the effective (lowest) speed limit between <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#speedLimitInMetersPerSecond"><code>speedLimitInMetersPerSecond</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#schoolZoneSpeedLimitInMetersPerSecond"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#timeDependentSpeedLimitInMetersPerSecond"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#optimalWeatherSpeedLimitInMetersPerSecond"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Returns the lowest value between: <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#speedLimitInMetersPerSecond"><code>speedLimitInMetersPerSecond</code></a>,
     <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#schoolZoneSpeedLimitInMetersPerSecond"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#timeDependentSpeedLimitInMetersPerSecond"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>
     and <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#optimalWeatherSpeedLimitInMetersPerSecond"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>.</p></dd>
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
