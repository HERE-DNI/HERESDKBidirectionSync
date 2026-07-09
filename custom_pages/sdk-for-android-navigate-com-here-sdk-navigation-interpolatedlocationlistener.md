---
title: "InterpolatedLocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- InterpolatedLocationListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">InterpolatedLocationListener</span></div>
<div className="block"><p>This interface should be implemented
 in order to receive interpolated locations. The interpolated locations are only provided between
 <a href="sdk-for-android-navigate-visualnavigator#startRendering(com.here.sdk.mapview.MapViewBase)"><code>VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase)</code></a> and <a href="sdk-for-android-navigate-visualnavigator#stopRendering()"><code>VisualNavigator.stopRendering()</code></a> calls and the application
 is not running in the background.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="onInterpolatedLocationUpdated(com.here.sdk.core.Location)">
<h3>onInterpolatedLocationUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onInterpolatedLocationUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>Called whenever a new interpolated location is calculated, usually several times per second.
 The interpolated locations are only provided between <a href="sdk-for-android-navigate-visualnavigator#startRendering(com.here.sdk.mapview.MapViewBase)"><code>VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase)</code></a> and
 <a href="sdk-for-android-navigate-visualnavigator#stopRendering()"><code>VisualNavigator.stopRendering()</code></a> calls and the application is not running in the background.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>The interpolated location.</p></dd>
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
