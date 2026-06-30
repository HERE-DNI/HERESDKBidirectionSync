---
title: "LocationEngineBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationenginebase"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationEngineBase.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-locationengine" title="class in com.here.sdk.location">LocationEngine</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LocationEngineBase</span></div>
<div class="block"><p>Public interface that describes the behaviour of <code>LocationEngine</code>.
 Implementation is platform-specific.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">addLocationIssueListener</a><wbr/>(<a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue has occurred.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationListener(com.here.sdk.core.LocationListener)">addLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a <code>LocationListener</code> to the engine to get notified when there is a new location
 update available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">addLocationStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a <code>LocationStatusListener</code> to the engine to get notified when there is an important
 status change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException()">confirmHEREPrivacyNoticeException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">By calling this method, the application developer confirms that they have received an exceptional permission
 from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion()">confirmHEREPrivacyNoticeInclusion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">It is the responsibility of the application developer to ensure that
 the application user is informed about the collection of characteristic information
 regarding nearby mobile and Wi-Fi network signals.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#disableVehicleSensors()">disableVehicleSensors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Disables access to vehicle's sensor information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">enableVehicleSensors</a><wbr/>(androidx.car.app.hardware.CarHardwareManager manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This feature enables the utilization of the vehicle's GNSS and movement sensor information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#getLastKnownLocation()">getLastKnownLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the last known location obtained by the <code>LocationEngine</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#isStarted()">isStarted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if the engine is in started state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">removeLocationIssueListener</a><wbr/>(<a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationListener(com.here.sdk.core.LocationListener)">removeLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a <code>LocationListener</code> from the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">removeLocationStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a <code>LocationStatusListener</code> from the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#setLastKnownLocationPersistent(boolean)">setLastKnownLocationPersistent</a><wbr/>(boolean persistent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Enables or disables saving of last known location so that it persists between application sessions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationAccuracy)">start</a><wbr/>(<a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)">start</a><wbr/>(<a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()">stop</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Stops the location engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">updateLocationAccuracy</a><wbr/>(<a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reconfigures the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#updateLocationOptions(com.here.sdk.location.LocationOptions)">updateLocationOptions</a><wbr/>(<a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reconfigures the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="start(com.here.sdk.location.LocationAccuracy)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div class="block"><p>Starts the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>. Returns
 <a href="sdk-for-android-navigate-locationenginestatus#ALREADY_STARTED"><code>LocationEngineStatus.ALREADY_STARTED</code></a>, if <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> is called again without <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> in between.
 Make sure to call either <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion()"><code>confirmHEREPrivacyNoticeInclusion()</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException()"><code>confirmHEREPrivacyNoticeException()</code></a> beforehand.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(com.here.sdk.location.LocationOptions)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div class="block"><p>Starts the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>. Returns
 <a href="sdk-for-android-navigate-locationenginestatus#ALREADY_STARTED"><code>LocationEngineStatus.ALREADY_STARTED</code></a>, if <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> is called again without <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> in between.
 Make sure to call either <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion()"><code>confirmHEREPrivacyNoticeInclusion()</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException()"><code>confirmHEREPrivacyNoticeException()</code></a> beforehand.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">
<h3>updateLocationAccuracy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationAccuracy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div class="block"><p>Reconfigures the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>. This method is a faster way to change location accuracy for already started
 location engine, than calling <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>,
 if called for unstarted location engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocationOptions(com.here.sdk.location.LocationOptions)">
<h3>updateLocationOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div class="block"><p>Reconfigures the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>. This method is a faster way to change location options for already started
 location engine, than calling <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop()"><code>stop()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>,
 if called for unstarted location engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stop()">
<h3>stop</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">stop</span>()</div>
<div class="block"><p>Stops the location engine.</p></div>
</section>
</li>
<li>
<section class="detail" id="confirmHEREPrivacyNoticeInclusion()">
<h3>confirmHEREPrivacyNoticeInclusion</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeInclusion</span>()</div>
<div class="block"><p>It is the responsibility of the application developer to ensure that
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
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Immediately returns with <a href="sdk-for-android-navigate-confirmationstatus#OK"><code>ConfirmationStatus.OK</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="confirmHEREPrivacyNoticeException()">
<h3>confirmHEREPrivacyNoticeException</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeException</span>()</div>
<div class="block"><p>By calling this method, the application developer confirms that they have received an exceptional permission
 from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice. As a result,
 the <code>LocationEngine</code> will not collect characteristic information about the nearby mobile and Wi-Fi network signals.
 However, the engine will still be fully functional and it will deliver location updates when the exception
 can be confirmed.
 Note that this call should not involve user interaction and it should be executed silently
 by the application before starting the <code>LocationEngine</code>.
 The permission for exceptional use will be verified asynchronously using your HERE SDK credentials.
 A missing permission will lead to stopping of the <code>LocationEngine</code> and <a href="sdk-for-android-navigate-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED"><code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code></a>
 is delivered to <code>LocationStatusListener</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location"><code>ConfirmationStatus</code></a>.
     A first-time call may result in <a href="sdk-for-android-navigate-confirmationstatus#PENDING"><code>ConfirmationStatus.PENDING</code></a>, make sure to use the
     <code>LocationStatusListener</code> to get notified on an unconfirmed permission.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationListener(com.here.sdk.core.LocationListener)">
<h3>addLocationListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div class="block"><p>Adds a <code>LocationListener</code> to the engine to get notified when there is a new location
 update available. Supports more than one listener, instance is added only once.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationListener(com.here.sdk.core.LocationListener)">
<h3>removeLocationListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div class="block"><p>Removes a <code>LocationListener</code> from the engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>addLocationStatusListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addLocationStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div class="block"><p>Adds a <code>LocationStatusListener</code> to the engine to get notified when there is an important
 status change. Supports more than one listener, instance is added only once.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>removeLocationStatusListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeLocationStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div class="block"><p>Removes a <code>LocationStatusListener</code> from the engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>addLocationIssueListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addLocationIssueListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div class="block"><p>Adds a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue has occurred.
 Supports more than one listener, instance is added only once.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>removeLocationIssueListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeLocationIssueListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div class="block"><p>Removes a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastKnownLocationPersistent(boolean)">
<h3>setLastKnownLocationPersistent</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">setLastKnownLocationPersistent</span><wbr/><span class="parameters">(boolean persistent)</span></div>
<div class="block"><p>Enables or disables saving of last known location so that it persists between application sessions.
 Defaults to enabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>persistent</code> - <p>Set to <code>true</code> to enable last known location to be saved persistently, or <code>false</code> to disable it.</p></dd>
<dt>Returns:</dt>
<dd><p><a href="sdk-for-android-navigate-locationenginestatus#OK"><code>LocationEngineStatus.OK</code></a> if call succeeds.
     <a href="sdk-for-android-navigate-locationenginestatus#NOT_SUPPORTED"><code>LocationEngineStatus.NOT_SUPPORTED</code></a> on platforms which do not support controlling of last known location saving.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">
<h3>enableVehicleSensors</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">enableVehicleSensors</span><wbr/><span class="parameters">(@NonNull
 androidx.car.app.hardware.CarHardwareManager manager)</span></div>
<div class="block"><p>This feature enables the utilization of the vehicle's GNSS and movement sensor information.
 It is recommended to always enable this feature by default when the application supports Android Auto.
 This allows the phone's positioning sensor information to be augmented with the vehicle's sensor data,
 resulting in the best possible positioning estimates.
 However, given the varying quality of car sensor implementations, it is also advisable to provide application users
 with the option to disable the usage of vehicle sensor information - this would be helpful in case the vehicle
 reports information that is clearly misleading or contradictory.
 Furthermore, users should be able to re-enable this feature if the vehicle's capability improves.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - <p>Android Auto car hardware manager.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disableVehicleSensors()">
<h3>disableVehicleSensors</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">disableVehicleSensors</span>()</div>
<div class="block"><p>Disables access to vehicle's sensor information.</p></div>
</section>
</li>
<li>
<section class="detail" id="getLastKnownLocation()">
<h3>getLastKnownLocation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a></span> <span class="element-name">getLastKnownLocation</span>()</div>
<div class="block"><p>Gets the last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
 This property can be obtained without starting the <code>LocationEngine</code>. However, the initial value might be <code>null</code>
 if no location has ever been obtained by the <code>LocationEngine</code>.
 The time attribute of the <code>Location</code> object indicates when the last location was obtained.
 Note: In order to receive continuous location updates, add a <code>LocationListener</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStarted()">
<h3>isStarted</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isStarted</span>()</div>
<div class="block"><p>Checks if the engine is in started state.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
