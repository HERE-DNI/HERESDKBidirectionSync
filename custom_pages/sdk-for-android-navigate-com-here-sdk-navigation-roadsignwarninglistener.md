---
title: "RoadSignWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoadSignWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">RoadSignWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive road sign warnings.
 <strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <em>always</em> be
 2 warnings emitted, with the [RoadSignWarning.distance_type] set to <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a> and <a href="sdk-for-android-navigate-distancetype#PASSED"><code>DistanceType.PASSED</code></a>
 which is given when the location of the road sign is reached.
 A <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation"><code>RoadSignWarning</code></a> will not be given until the previous warning of that type has been passed.
 For example, a route with <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation"><code>RoadSignWarning</code></a> 120 meters and <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation"><code>RoadSignWarning</code></a> 160 meters ahead,
 the first [RoadSignWarning.distance_to_road_sign_in_meters] is 120 meters
 and the next [RoadSignWarning.distance_to_road_sign_in_meters] is then 40 meters,
 since that is the distance between the first and second warnings.</p></div>
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
<section className="detail" id="onRoadSignWarningUpdated(com.here.sdk.navigation.RoadSignWarning)">
<h3>onRoadSignWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onRoadSignWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation">RoadSignWarning</a> roadSignWarning)</span></div>
<div className="block"><p>Called whenever a new road sign warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>roadSignWarning</code> - <p>The object that contains details on the road sign warning.</p></dd>
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
