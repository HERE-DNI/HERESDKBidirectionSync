---
title: "BorderCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- BorderCrossingWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">BorderCrossingWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive border crossing warnings for country and state borders.
 <strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <em>always</em> be
 2 warnings emitted, with the [BorderCrossingWarning.distance_type] set to <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a> and <a href="sdk-for-android-navigate-distancetype#PASSED"><code>DistanceType.PASSED</code></a>
 which is given when the location of the border crossing is reached.
 A <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> will not be given until the previous warning of that type has been passed.
 For example, a route with <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> 120 meters and <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> 160 meters ahead,
 the first [BorderCrossingWarning.distance_to_border_crossing_in_meters] is 120 meters
 and the next [BorderCrossingWarning.distance_to_border_crossing_in_meters] is then 40 meters,
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
<section className="detail" id="onBorderCrossingWarningUpdated(com.here.sdk.navigation.BorderCrossingWarning)">
<h3>onBorderCrossingWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onBorderCrossingWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a> borderCrossingWarning)</span></div>
<div className="block"><p>Called whenever a new border crossing warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>borderCrossingWarning</code> - <p>The object that contains details on the border crossing warning.</p></dd>
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
