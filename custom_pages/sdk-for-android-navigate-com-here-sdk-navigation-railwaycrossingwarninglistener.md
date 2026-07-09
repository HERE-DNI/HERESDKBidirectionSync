---
title: "RailwayCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RailwayCrossingWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">RailwayCrossingWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive railway crossing warnings.
 <strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
 on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
 means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
 crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
 <code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
 case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
 set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p></div>
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
<section className="detail" id="onRailwayCrossingWarningUpdated(com.here.sdk.navigation.RailwayCrossingWarning)">
<h3>onRailwayCrossingWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onRailwayCrossingWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a> railwayCrossingWarning)</span></div>
<div className="block"><p>Called whenever a new railway crossing warning is available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>railwayCrossingWarning</code> - <p>The object that contains details on the railway crossing warning.</p></dd>
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
