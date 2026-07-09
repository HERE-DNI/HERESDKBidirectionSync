---
title: "EventTextListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EventTextListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">EventTextListener</span></div>
<div className="block"><p>This interface should be implemented in order to receive notifications
 when text notifications are available from <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>. Multiple notifications
 can be given for the same maneuver at different distances.</p></div>
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
<section className="detail" id="onEventTextUpdated(com.here.sdk.navigation.EventText)">
<h3>onEventTextUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onEventTextUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext" title="class in com.here.sdk.navigation">EventText</a> eventText)</span></div>
<div className="block"><p>Called whenever there is a new text notification for a maneuver (multiple notifications can be
 given for the same maneuver at different distances (for example: "After 500 meters turn
 right." or "Now turn right.") and in that case, this method will be called once for each
 distance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>eventText</code> - <p>Data related to next text announcement.</p></dd>
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
