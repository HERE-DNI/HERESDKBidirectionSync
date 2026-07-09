---
title: "LowSpeedZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LowSpeedZoneWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LowSpeedZoneWarningListener</span></div>
<div className="block"><p>This interface should be implemented in order to receive low speed zone warnings.
 <strong>Note:</strong> This is currently available <em>only</em> for Japan.
 The low speed zone warner is a zone warner, which means that for a low speed zone there will <em>always</em>
 be 3 warnings emitted, with the <code>LowSpeedZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
 and lastly <code>DistanceType.PASSED</code> when the end of the low speed zone is passed.</p></div>
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
<section className="detail" id="onLowSpeedZoneWarningUpdated(com.here.sdk.navigation.LowSpeedZoneWarning)">
<h3>onLowSpeedZoneWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onLowSpeedZoneWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a> lowSpeedZoneWarning)</span></div>
<div className="block"><p>Called whenever a new low speed zone warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lowSpeedZoneWarning</code> - <p>The object that contains details on the low speed zone warning.</p></dd>
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
