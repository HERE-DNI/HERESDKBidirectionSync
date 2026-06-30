---
title: "TrafficBroadcast (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficBroadcast.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.trafficbroadcast.TrafficBroadcast</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficBroadcast</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div class="block"><p>A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
 format and it can be used when there is no internet connection, so that the <code>OfflineRoutingEngine</code>
 can utilize traffic data coming over a radio channel. The <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#activate()"><code>activate()</code></a> method needs to be called to
 receive traffic data events.
 <strong>Note:</strong> In order to adopt the <code>TrafficDataProvider</code> interface special hardware is required. Talk
 to your HERE representative for more details. Only by adopting the <code>TrafficDataProvider</code> interface
 you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant
 to be used <em>independently</em> from the already included traffic on routes, on the map and from the
 HERE backends (when using the <code>TrafficEngine</code>).
 This class continuously reacts to new locations provided from a location source and acts as a
 <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a>. The location must be updated regardless of calling <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#activate()"><code>activate()</code></a>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.trafficbroadcast.TrafficBroadcastParameters)">TrafficBroadcast</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#%3Cinit%3E(com.here.sdk.trafficbroadcast.TrafficBroadcastParameters)">TrafficBroadcast</a><wbr/>(<a href="sdk-for-android-navigate-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#activate()">activate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activates the reception of traffic data over the radio channel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#deactivate()">deactivate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deactivates the reception of traffic data over the radio channel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#getTrafficDataProvider()">getTrafficDataProvider</a>()</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called each time a new location is available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#onTMCDataUpdated(com.here.sdk.trafficbroadcast.TMCData)">onTMCDataUpdated</a><wbr/>(<a href="sdk-for-android-navigate-tmcdata" title="class in com.here.sdk.trafficbroadcast">TMCData</a> tmcData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Must be called on every TMC data update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast#onTMCServiceProviderInfoUpdated(com.here.sdk.trafficbroadcast.TMCServiceProviderInfo)">onTMCServiceProviderInfoUpdated</a><wbr/>(<a href="sdk-for-android-navigate-tmcserviceproviderinfo" title="class in com.here.sdk.trafficbroadcast">TMCServiceProviderInfo</a> tmcServiceProdiverInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Must be called on every TMC service prodiver info update.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.trafficbroadcast.TrafficBroadcastParameters)">
<h3>TrafficBroadcast</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TrafficBroadcast</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</span>
                 throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters</code> - <p>The necessary parameters to start traffic broadcast.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>when the object was not initialized properly.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.trafficbroadcast.TrafficBroadcastParameters)">
<h3>TrafficBroadcast</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TrafficBroadcast</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</span>
                 throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of an existing SDKEngine.</p></dd>
<dd><code>parameters</code> - <p>The necessary parameters to start traffic broadcast.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>when the object was not initialized properly.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="activate()">
<h3>activate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activate</span>()</div>
<div class="block"><p>Activates the reception of traffic data over the radio channel.
 This method is supposed to be called when the system loses internet connection,
 so that traffic data can be switched from the online source to the radio channel.
 When activation is done, requestTMCService is called from TMCServiceInterface</p></div>
</section>
</li>
<li>
<section class="detail" id="deactivate()">
<h3>deactivate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivate</span>()</div>
<div class="block"><p>Deactivates the reception of traffic data over the radio channel.
 When deactivation is done, requestTMCService is called from TMCServiceInterface
 With special case of countryCode parameter = 0</p></div>
</section>
</li>
<li>
<section class="detail" id="onTMCServiceProviderInfoUpdated(com.here.sdk.trafficbroadcast.TMCServiceProviderInfo)">
<h3>onTMCServiceProviderInfoUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onTMCServiceProviderInfoUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-tmcserviceproviderinfo" title="class in com.here.sdk.trafficbroadcast">TMCServiceProviderInfo</a> tmcServiceProdiverInfo)</span></div>
<div class="block"><p>Must be called on every TMC service prodiver info update.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmcServiceProdiverInfo</code> - <p>Contains service prodiver info in RDS-TMC format.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onTMCDataUpdated(com.here.sdk.trafficbroadcast.TMCData)">
<h3>onTMCDataUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onTMCDataUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-tmcdata" title="class in com.here.sdk.trafficbroadcast">TMCData</a> tmcData)</span></div>
<div class="block"><p>Must be called on every TMC data update.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmcData</code> - <p>Contains the traffic events in RDS-TMC format.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficDataProvider()">
<h3>getTrafficDataProvider</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></span> <span class="element-name">getTrafficDataProvider</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The traffic data provider that provides the traffic information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
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
`
}</HTMLBlock>
