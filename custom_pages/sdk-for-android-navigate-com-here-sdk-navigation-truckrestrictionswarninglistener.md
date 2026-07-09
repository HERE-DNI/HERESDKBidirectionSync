---
title: "TruckRestrictionsWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TruckRestrictionsWarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TruckRestrictionsWarningListener</span></div>
<div className="block"><p>This interface
 should be implemented in order to receive truck restriction warnings.</p></div>
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
<section className="detail" id="onTruckRestrictionsWarningUpdated(java.util.List)">
<h3>onTruckRestrictionsWarningUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTruckRestrictionsWarningUpdated</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a>&gt; restrictions)</span></div>
<div className="block"><p>Called whenever the distance type (<a href="sdk-for-android-navigate-truckrestrictionwarning#distanceType"><code>TruckRestrictionWarning.distanceType</code></a>) of a truck
 restriction changes. If needed, it is up to the application to maintain a list of active
 warnings like the ones with <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a> or <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> based on the
 updates provided by this method.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>restrictions</code> - <p>A list containing truck restriction warnings that have their distance
     type (<a href="sdk-for-android-navigate-truckrestrictionwarning#distanceType"><code>TruckRestrictionWarning.distanceType</code></a>) updated.</p></dd>
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
