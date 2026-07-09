---
title: "LocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-locationlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
</dl>
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation">GPXTrackWriter</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">Navigator</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcast</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">VisualNavigator</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LocationListener</span></div>
<div className="block"><p>This interface should be implemented in order to receive notifications
 about location updates.</p></div>
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
<section className="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onLocationUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>Current location.</p></dd>
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
