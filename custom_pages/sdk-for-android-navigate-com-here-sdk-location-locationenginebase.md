---
title: "LocationEngineBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationenginebase"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationEngineBase.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-location-locationengine" title="class in com.here.sdk.location">LocationEngine</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LocationEngineBase</span></div>
<div className="block"><p>Public interface that describes the behaviour of <code>LocationEngine</code>.
 Implementation is platform-specific.</p></div>
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
<section className="detail" id="start(com.here.sdk.location.LocationAccuracy)">
<h3>start</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div className="block"><p>Starts the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>. Returns
 <a href="sdk-for-android-navigate-locationenginestatus#ALREADY_STARTED"><code>LocationEngineStatus.ALREADY_STARTED</code></a>, if <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> is called again without <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> in between.
 Make sure to call either <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion()"><code>confirmHEREPrivacyNoticeInclusion()</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException()"><code>confirmHEREPrivacyNoticeException()</code></a> beforehand.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="start(com.here.sdk.location.LocationOptions)">
<h3>start</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div className="block"><p>Starts the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>. Returns
 <a href="sdk-for-android-navigate-locationenginestatus#ALREADY_STARTED"><code>LocationEngineStatus.ALREADY_STARTED</code></a>, if <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> is called again without <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> in between.
 Make sure to call either <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion()"><code>confirmHEREPrivacyNoticeInclusion()</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException()"><code>confirmHEREPrivacyNoticeException()</code></a> beforehand.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">
<h3>updateLocationAccuracy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">updateLocationAccuracy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div className="block"><p>Reconfigures the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>. This method is a faster way to change location accuracy for already started
 location engine, than calling <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>,
 if called for unstarted location engine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="updateLocationOptions(com.here.sdk.location.LocationOptions)">
<h3>updateLocationOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">updateLocationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div className="block"><p>Reconfigures the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>. This method is a faster way to change location options for already started
 location engine, than calling <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>,
 if called for unstarted location engine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="stop()">
<h3>stop</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">stop</span>()</div>
<div className="block"><p>Stops the location engine.</p></div>
</section>
</li>
<li>
<section className="detail" id="confirmHEREPrivacyNoticeInclusion()">
<h3>confirmHEREPrivacyNoticeInclusion</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span className="element-name">confirmHEREPrivacyNoticeInclusion</span>()</div>
<div className="block"><p>It is the responsibility of the application developer to ensure that
 the application user is informed about the collection of characteristic information
 regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related
 <a href="https://legal.here.com/en-gb/here-network-positioning-via-sdk">HERE Privacy Notice</a>
 must be made available to the user.
 This information can be included in the application's Terms &amp; Conditions,
 Privacy Policy, or otherwise made accessible to the user.
 An example text for informing users about the data collection:
 "This application uses location services provided by HERE Technologies.
 To maintain, improve, and provide these services, HERE Technologies occasionally collects
 characteristic information about nearby mobile and Wi-Fi network signals.
 For more information, please refer to the HERE Privacy Notice at:
 https://legal.here.com/en-gb/here-network-positioning-via-sdk"
 <strong>Note:</strong> By calling this method, the application developer confirms that
 this information is made available to the end user.
 For example, it is sufficient to inform users once that using the app requires
 acceptance of its terms (if any). Then, in the terms include the
 above mentioned data collection information and a link to the related HERE Privacy Notice.
 The user is not required to open the terms to acknowledge the data collection details.
 The "Positioning" example app on <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a>
 provides an example of this.
 When the above criteria are met, it is recommended to silently execute this
 method each time before starting the <code>LocationEngine</code>, as failure to do so
 will result in the engine being non-functional.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Immediately returns with <a href="sdk-for-android-navigate-confirmationstatus#OK"><code>ConfirmationStatus.OK</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="confirmHEREPrivacyNoticeException()">
<h3>confirmHEREPrivacyNoticeException</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span className="element-name">confirmHEREPrivacyNoticeException</span>()</div>
<div className="block"><p>By calling this method, the application developer confirms that they have received an exceptional permission
 from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice. As a result,
 the <code>LocationEngine</code> will not collect characteristic information about the nearby mobile and Wi-Fi network signals.
 However, the engine will still be fully functional and it will deliver location updates when the exception
 can be confirmed.
 Note that this call should not involve user interaction and it should be executed silently
 by the application before starting the <code>LocationEngine</code>.
 The permission for exceptional use will be verified asynchronously using your HERE SDK credentials.
 A missing permission will lead to stopping of the <code>LocationEngine</code> and <a href="sdk-for-android-navigate-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED"><code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code></a>
 is delivered to <code>LocationStatusListener</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location"><code>ConfirmationStatus</code></a>.
     A first-time call may result in <a href="sdk-for-android-navigate-confirmationstatus#PENDING"><code>ConfirmationStatus.PENDING</code></a>, make sure to use the
     <code>LocationStatusListener</code> to get notified on an unconfirmed permission.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationListener(com.here.sdk.core.LocationListener)">
<h3>addLocationListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">addLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div className="block"><p>Adds a <code>LocationListener</code> to the engine to get notified when there is a new location
 update available. Supports more than one listener, instance is added only once.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationListener(com.here.sdk.core.LocationListener)">
<h3>removeLocationListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">removeLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div className="block"><p>Removes a <code>LocationListener</code> from the engine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>addLocationStatusListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">addLocationStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div className="block"><p>Adds a <code>LocationStatusListener</code> to the engine to get notified when there is an important
 status change. Supports more than one listener, instance is added only once.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>removeLocationStatusListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">removeLocationStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div className="block"><p>Removes a <code>LocationStatusListener</code> from the engine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>addLocationIssueListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">addLocationIssueListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div className="block"><p>Adds a <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue has occurred.
 Supports more than one listener, instance is added only once.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>removeLocationIssueListener</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">removeLocationIssueListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div className="block"><p>Removes a <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLastKnownLocationPersistent(boolean)">
<h3>setLastKnownLocationPersistent</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">setLastKnownLocationPersistent</span><wbr/><span className="parameters">(boolean persistent)</span></div>
<div className="block"><p>Enables or disables saving of last known location so that it persists between application sessions.
 Defaults to enabled.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>persistent</code> - <p>Set to <code>true</code> to enable last known location to be saved persistently, or <code>false</code> to disable it.</p></dd>
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-locationenginestatus#OK"><code>LocationEngineStatus.OK</code></a> if call succeeds.
     <a href="sdk-for-android-navigate-locationenginestatus#NOT_SUPPORTED"><code>LocationEngineStatus.NOT_SUPPORTED</code></a> on platforms which do not support controlling of last known location saving.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">
<h3>enableVehicleSensors</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">enableVehicleSensors</span><wbr/><span className="parameters">(@NonNull
 androidx.car.app.hardware.CarHardwareManager manager)</span></div>
<div className="block"><p>This feature enables the utilization of the vehicle's GNSS and movement sensor information.
 It is recommended to always enable this feature by default when the application supports Android Auto.
 This allows the phone's positioning sensor information to be augmented with the vehicle's sensor data,
 resulting in the best possible positioning estimates.
 However, given the varying quality of car sensor implementations, it is also advisable to provide application users
 with the option to disable the usage of vehicle sensor information - this would be helpful in case the vehicle
 reports information that is clearly misleading or contradictory.
 Furthermore, users should be able to re-enable this feature if the vehicle's capability improves.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - <p>Android Auto car hardware manager.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="disableVehicleSensors()">
<h3>disableVehicleSensors</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">disableVehicleSensors</span>()</div>
<div className="block"><p>Disables access to vehicle's sensor information.</p></div>
</section>
</li>
<li>
<section className="detail" id="getLastKnownLocation()">
<h3>getLastKnownLocation</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a></span> <span className="element-name">getLastKnownLocation</span>()</div>
<div className="block"><p>Gets the last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
 This property can be obtained without starting the <code>LocationEngine</code>. However, the initial value might be <code>null</code>
 if no location has ever been obtained by the <code>LocationEngine</code>.
 The time attribute of the <code>Location</code> object indicates when the last location was obtained.
 Note: In order to receive continuous location updates, add a <code>LocationListener</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isStarted()">
<h3>isStarted</h3>
<div className="member-signature"><span className="return-type">boolean</span> <span className="element-name">isStarted</span>()</div>
<div className="block"><p>Checks if the engine is in started state.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Checks if the engine is in started state.</p></dd>
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
