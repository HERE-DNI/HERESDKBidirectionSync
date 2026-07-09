---
title: "SpeedWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SpeedWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">SpeedWarningListener</span></div>
<div className="block"><p>This interface should be implemented in order to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 <strong>Note:</strong>
 The warnings issued by this interface
 don't take into account any temporary special speed limits. See <code>SpeedLimitListener</code>.</p></div>
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
<section className="detail" id="onSpeedWarningStatusChanged(com.here.sdk.navigation.SpeedWarningStatus)">
<h3>onSpeedWarningStatusChanged</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onSpeedWarningStatusChanged</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningstatus" title="enum class in com.here.sdk.navigation">SpeedWarningStatus</a> status)</span></div>
<div className="block"><p>Called whenever a new <code>SpeedWarningStatus</code> is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - <p>The new status of the speed warning.</p></dd>
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
