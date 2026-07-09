---
title: "CameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CameraBehavior.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-areacamerabehavior" title="class in com.here.sdk.navigation">AreaCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior" title="class in com.here.sdk.navigation">AutomotiveCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-dynamiccamerabehavior" title="class in com.here.sdk.navigation">DynamicCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior" title="class in com.here.sdk.navigation">FixedCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedbasedcamerabehavior" title="class in com.here.sdk.navigation">SpeedBasedCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">CameraBehavior</span></div>
<div className="block"><p>Interface used to change implement different
 camera behaviors.</p></div>
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
<section className="detail" id="getNormalizedPrincipalPoint()">
<h3>getNormalizedPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span className="element-name">getNormalizedPrincipalPoint</span>()</div>
<div className="block"><p>Gets the currently set normalized principal point to be used during navigation.
 Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The normalized principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">setNormalizedPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div className="block"><p>Sets a normalized principal point to be used during navigation.
 Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The normalized principal point.</p></dd>
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
