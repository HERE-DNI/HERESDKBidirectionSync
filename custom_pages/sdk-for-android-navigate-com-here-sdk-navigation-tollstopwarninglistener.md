---
title: "TollStopWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TollStopWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TollStopWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive information on the upcoming toll booth structure.
 The warner might also warn about gates/checkpoints for vignette, border checkpoints
 and similar structures on the street.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.
 A <code>TollStop</code> will not be given until the previous warning of that type has been passed.
 For example, a route with <code>TollStop</code> 120 meters and <code>TollStop</code> 160 meters ahead,
 the first <code>TollStop.distance_to_toll_stop_in_meters</code> is 120 meters
 and the next <code>TollStop.distance_to_toll_stop_in_meters</code> is then 40 meters,
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
<section className="detail" id="onTollStopWarning(com.here.sdk.navigation.TollStop)">
<h3>onTollStopWarning</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTollStopWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">TollStop</a> tollStop)</span></div>
<div className="block"><p>Called whenever a new <code>TollStop</code> is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tollStop</code> - <p>The upcoming toll stop.</p></dd>
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
