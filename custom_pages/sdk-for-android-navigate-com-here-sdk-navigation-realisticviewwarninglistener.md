---
title: "RealisticViewWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RealisticViewWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">RealisticViewWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive realistic view warnings.
 A <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a> will not be given until the previous warning of that type has been passed.
 For example, a route with <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a> 120 meters and <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a> 160 meters ahead,
 the first <a href="sdk-for-android-navigate-realisticviewwarning#distanceToRealisticViewInMeters"><code>RealisticViewWarning.distanceToRealisticViewInMeters</code></a> is 120 meters
 and the next <a href="sdk-for-android-navigate-realisticviewwarning#distanceToRealisticViewInMeters"><code>RealisticViewWarning.distanceToRealisticViewInMeters</code></a> is then 40 meters,
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
<section className="detail" id="onRealisticViewWarningUpdated(com.here.sdk.navigation.RealisticViewWarning)">
<h3>onRealisticViewWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onRealisticViewWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a> realisticViewWarning)</span></div>
<div className="block"><p>Called whenever a new realistic view warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>realisticViewWarning</code> - <p>The object that contains details on the realistic view warning.</p></dd>
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
