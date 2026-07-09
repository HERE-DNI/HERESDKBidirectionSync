---
title: "SafetyCameraWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SafetyCameraWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">SafetyCameraWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive notifications on safety cameras.
 A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
 For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
 the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
 and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
 since that is the distance between the first and second warnings.
 When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
 The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
 That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p></div>
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
<section className="detail" id="onSafetyCameraWarningUpdated(com.here.sdk.navigation.SafetyCameraWarning)">
<h3>onSafetyCameraWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onSafetyCameraWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a> safetyCameraWarning)</span></div>
<div className="block"><p>Called whenever a new <code>SafetyCameraWarning</code> is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>safetyCameraWarning</code> - <p>The object that contains details on the safety camera warning.</p></dd>
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
