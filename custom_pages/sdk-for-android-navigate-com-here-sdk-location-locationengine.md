---
title: "LocationEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.location.LocationEngine</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.here.sdk.location.AppConfigListener</code>, <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">LocationEngine</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a>, com.here.sdk.location.AppConfigListener</span></div>
<div className="block">This class handles location updates received according to the desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.
 Each instance of this class will be using internally the same client providing the actual
 location updates. For that reason, only one <a href="sdk-for-android-navigate-com-here-sdk-location-locationengine" title="class in com.here.sdk.location"><code>LocationEngine</code></a>
 can be started at a time. Multiple listeners can be attached, either to receive
 location updates, see <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a>, status updates, see
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> or location issue has occurred, see
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a>. When a different <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a> is
 desired, the LocationEngine needs to be stopped and started again.</div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationengine#%3Cinit%3E()">LocationEngine</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Constructor of the LocationEngine</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">LocationEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructor of the LocationEngine</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>LocationEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationEngine</span>()
               throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block">Constructor of the LocationEngine</div>
<dl className="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if engine was not initialized properly</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>LocationEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LocationEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine)</span>
               throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block">Constructor of the LocationEngine</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - of the SDK holding internal services and SDK configuration</dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if engine was not initialized properly</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="start(com.here.sdk.location.LocationAccuracy)">
<h3>start</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div className="block">Starts the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>.
 Make sure to call either confirmHEREPrivacyNoticeInclusion()
 or confirmHEREPrivacyNoticeException() beforehand.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationAccuracy)">start</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - Desired location accuracy</dd>
<dt>Returns:</dt>
<dd>the status of the LocationEngine</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="start(com.here.sdk.location.LocationOptions)">
<h3>start</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div className="block">Starts the location engine with desired <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.
 Make sure to call either confirmHEREPrivacyNoticeInclusion()
 or confirmHEREPrivacyNoticeException() beforehand.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)">start</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - Desired location options.</dd>
<dt>Returns:</dt>
<dd>the status of the LocationEngine</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">
<h3>updateLocationAccuracy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">updateLocationAccuracy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div className="block"><p>Reconfigures the location engine with desired LocationAccuracy. This method is a faster
 way to change location accuracy for already started location engine, than calling <a href="sdk-for-android-navigate-locationenginebase#stop()"><code>LocationEngineBase.stop()</code></a> and <a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>LocationEngineBase.start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>, if called for unstarted location
 engine.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">updateLocationAccuracy</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not
 guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="updateLocationOptions(com.here.sdk.location.LocationOptions)">
<h3>updateLocationOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">updateLocationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div className="block"><p>Reconfigures the location engine with desired LocationOptions. This method is a faster way
 to change location options for already started location engine, than calling <a href="sdk-for-android-navigate-locationenginebase#stop()"><code>LocationEngineBase.stop()</code></a> and <a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>LocationEngineBase.start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>, if called for unstarted location
 engine.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#updateLocationOptions(com.here.sdk.location.LocationOptions)">updateLocationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="stop()">
<h3>stop</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">stop</span>()</div>
<div className="block">Stops the location engine.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#stop()">stop</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isStarted()">
<h3>isStarted</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isStarted</span>()</div>
<div className="block">Checks if the engine is in started state.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#isStarted()">isStarted</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>true if started, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="confirmHEREPrivacyNoticeInclusion()">
<h3>confirmHEREPrivacyNoticeInclusion</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span className="element-name">confirmHEREPrivacyNoticeInclusion</span>()</div>
<div className="block"><p>It is the responsibility of the application developer to ensure that
 the application user is informed about the collection of characteristic information
 regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related
 <a href="https://legal.here.com/here-network-positioning-via-sdk">HERE Privacy Notice</a>
 must be made available to the user.
 This information can be included in the application's Terms &amp; Conditions,
 Privacy Policy, or otherwise made accessible to the user.
 An example text for informing users about the data collection:
 "This application uses location services provided by HERE Technologies.
 To maintain, improve, and provide these services, HERE Technologies occasionally collects
 characteristic information about nearby mobile and Wi-Fi network signals.
 For more information, please refer to the HERE Privacy Notice at:
 https://legal.here.com/here-network-positioning-via-sdk"

 By calling this method, the application developer confirms that
 this information is made available to the end user.

 For example, it is sufficient to inform users once that using the app requires
 acceptance of its terms (if any). Then, in the terms include the
 above mentioned data collection information and a link to the related HERE Privacy Notice.
 The user is not required to open the terms to acknowledge the data collection details.
 The "Positioning" example app on
 <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a>
 provides an example of this.

 When the above criteria are met, it is recommended to silently execute this
 method each time before starting the <code>LocationEngine</code>, as failure to do so
 will result in the engine being non-functional.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#confirmHEREPrivacyNoticeInclusion()">confirmHEREPrivacyNoticeInclusion</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>Immediately returns with <a href="sdk-for-android-navigate-confirmationstatus#OK"><code>ConfirmationStatus.OK</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="confirmHEREPrivacyNoticeException()">
<h3>confirmHEREPrivacyNoticeException</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span className="element-name">confirmHEREPrivacyNoticeException</span>()</div>
<div className="block"><p>By calling this method, the application developer confirms that they have received an
 exceptional permission from HERE in written form to **not** include a reference to the HERE
 Privacy Notice. As a result, the <code>LocationEngine</code> will not collect characteristic
 information about the nearby mobile and Wi-Fi network signals. However, the engine will still
 be fully functional and it will deliver location updates when the exception can be confirmed.
 Note that this call should not involve user interaction and it should be executed silently
 by the application before starting the <code>LocationEngine</code>.
 The permission for exceptional use will be verified asynchronously using your HERE SDK
 credentials. A missing permission will lead to stopping of the <code>LocationEngine</code>
 and
 <a href="sdk-for-android-navigate-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED"><code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code></a> is delivered to
 <code>LocationStatusListener</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#confirmHEREPrivacyNoticeException()">confirmHEREPrivacyNoticeException</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location"><code>ConfirmationStatus</code></a>.
         A first-time call may result in <a href="sdk-for-android-navigate-confirmationstatus#PENDING"><code>ConfirmationStatus.PENDING</code></a>, make sure to use the
         <code>LocationStatusListener</code> to get notified on an unconfirmed permission.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">
<h3>enableVehicleSensors</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">enableVehicleSensors</span><wbr/><span className="parameters">(@NonNull
 androidx.car.app.hardware.CarHardwareManager manager)</span></div>
<div className="block">This feature enables the utilization of the vehicle's GNSS and movement sensor information.
 It is recommended to always enable this feature by default when the application supports
 Android Auto. This allows the phone's positioning sensor information to be augmented with the
 vehicle's sensor data, resulting in the best possible positioning estimates. However, given
 the varying quality of car sensor implementations, it is also advisable to provide
 application users with the option to disable the usage of vehicle sensor information - this
 would be helpful in case the vehicle reports information that is clearly misleading or
 contradictory. Furthermore, users should be able to re-enable this feature if the vehicle's
 capability improves.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">enableVehicleSensors</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>manager</code> - Android Auto car hardware manager.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="disableVehicleSensors()">
<h3>disableVehicleSensors</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">disableVehicleSensors</span>()</div>
<div className="block">Disables access to vehicle's sensor information.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#disableVehicleSensors()">disableVehicleSensors</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLastKnownLocation()">
<h3>getLastKnownLocation</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a></span> <span className="element-name">getLastKnownLocation</span>()</div>
<div className="block">Gets the last known location obtained by the engine.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#getLastKnownLocation()">getLastKnownLocation</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>last known <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a> if available, null if never
         obtained.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationListener(com.here.sdk.core.LocationListener)">
<h3>addLocationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div className="block">Adds a <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> to the engine to get notified when there is a new
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a>.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationListener(com.here.sdk.core.LocationListener)">addLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationListener(com.here.sdk.core.LocationListener)">
<h3>removeLocationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeLocationListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div className="block">Removes a <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> from the engine</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationListener(com.here.sdk.core.LocationListener)">removeLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>addLocationStatusListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addLocationStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div className="block">Adds a <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> to the engine to get notified when there is an
 important status change.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">addLocationStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>removeLocationStatusListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeLocationStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div className="block">Removes a <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> from the engine</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">removeLocationStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>addLocationIssueListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addLocationIssueListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div className="block">Adds a <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue
 has occurred</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">addLocationIssueListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>removeLocationIssueListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeLocationIssueListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div className="block">Removes a <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">removeLocationIssueListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLastKnownLocationPersistent(boolean)">
<h3>setLastKnownLocationPersistent</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">setLastKnownLocationPersistent</span><wbr/><span className="parameters">(boolean persistent)</span></div>
<div className="block">Enables or disables saving of last known location so it persists between application
 sessions. Defaults to enabled.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#setLastKnownLocationPersistent(boolean)">setLastKnownLocationPersistent</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>persistent</code> - If true enables last known location to be saved persistently, or if false
         disables it.</dd>
<dt>Returns:</dt>
<dd>LocationEngineStatus.OK always.</dd>
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
