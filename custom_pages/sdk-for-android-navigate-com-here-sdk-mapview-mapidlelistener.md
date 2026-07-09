---
title: "MapIdleListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapidlelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapIdleListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">MapIdleListener</span></div>
<div className="block"><p>Used to detect when the map becomes idle or busy.
 Map is considered busy when its state changes (for example as a result of camera manipulation)
 and/or when it requires a redraw (for example, as a result of map data being downloaded).
 Map is considered idle when current state is fully rendered and no further
 redraws are necessary.</p></div>
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
<section className="detail" id="onMapBusy()">
<h3>onMapBusy</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onMapBusy</span>()</div>
<div className="block"><p>Called when map becomes invalidated and is about to be updated. One or more
 redraws will happen afterwards, until <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapidlelistener#onMapIdle()"><code>onMapIdle()</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="onMapIdle()">
<h3>onMapIdle</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onMapIdle</span>()</div>
<div className="block"><p>Called when map finishes all state updates. No state changes or redraws
 will happen aftrwards until <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapidlelistener#onMapBusy()"><code>onMapBusy()</code></a> is called.</p></div>
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
