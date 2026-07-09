---
title: "TrafficMergeWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficMergeWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TrafficMergeWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive traffic merge warnings.
 <strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
 2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
 which is given when the location of the traffic merge is reached.
 A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
 For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
 the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
 and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
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
<section className="detail" id="onTrafficMergeWarningUpdated(com.here.sdk.navigation.TrafficMergeWarning)">
<h3>onTrafficMergeWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTrafficMergeWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a> trafficMergeWarning)</span></div>
<div className="block"><p>Called whenever a new traffic merge warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>trafficMergeWarning</code> - <p>The object that contains details on the traffic merge warning.</p></dd>
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
