---
title: "CurrentSituationLaneAssistanceViewListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CurrentSituationLaneAssistanceViewListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">CurrentSituationLaneAssistanceViewListener</span></div>
<div className="block"><p>This interface should be
 implemented in order to receive notifications on <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation"><code>CurrentSituationLaneAssistanceView</code></a>.
 The current situation lane assistance view notifications describe the lane information at the current location.
 A new notification is evaluated with each location update. A notification is only sent when there is a change
 in lane data, such as a new upcoming lane.
 This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
 During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
 to reach the destination.
 However, the event does not indicate which exact lane the user is currently driving in.
 The listener works for offline mode as well.
 <strong>Note:</strong>
<ul>
<li>Lane information is not available for all roads. It's mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul></p></div>
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
<section className="detail" id="onCurrentSituationLaneAssistanceViewUpdate(com.here.sdk.navigation.CurrentSituationLaneAssistanceView)">
<h3>onCurrentSituationLaneAssistanceViewUpdate</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onCurrentSituationLaneAssistanceViewUpdate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation">CurrentSituationLaneAssistanceView</a> lanes)</span></div>
<div className="block"><p>The callback to be called.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lanes</code> - <p>Lane information on the road the user is currently driving on.</p></dd>
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
