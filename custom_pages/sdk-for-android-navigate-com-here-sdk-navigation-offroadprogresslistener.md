---
title: "OffRoadProgressListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- OffRoadProgressListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">OffRoadProgressListener</span></div>
<div className="block"><p>This interface should be implemented in order to
 receive notifications about the current off-road location from <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>.</p></div>
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
<section className="detail" id="onOffRoadProgressUpdated(com.here.sdk.navigation.OffRoadProgress)">
<h3>onOffRoadProgressUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onOffRoadProgressUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogress" title="class in com.here.sdk.navigation">OffRoadProgress</a> offRoadProgress)</span></div>
<div className="block"><p>Called whenever the current location has been updated and the user is off-road. Off-road
 progress events starts after the user has reached the map-matched destination and the current
 location is not map-matched.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>offRoadProgress</code> - <p>The current off-road progress update.</p></dd>
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
