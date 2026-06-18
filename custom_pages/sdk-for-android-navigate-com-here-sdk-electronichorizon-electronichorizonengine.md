---
title: "ElectronicHorizonEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ElectronicHorizonEngine.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Provides an electronic horizon engine that continuously predicts
 the road network ahead of the vehicle by using detailed map data, including road topography that is
 currently out of sight.
 You can subscribe to electronic horizon updates based on position updates by using <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a>.
 For more information about sub path levels, see <a href="sdk-for-android-navigate-electronichorizonoptions#lookAheadDistancesInMeters"><code>ElectronicHorizonOptions.lookAheadDistancesInMeters</code></a>.
 </p><p>The electronic horizon engine uses map-matched locations and can optionally use a <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a>
 to improve the most-preferred path (MPP).
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.electronichorizon.ElectronicHorizonOptions,com.here.sdk.transport.TransportMode,com.here.sdk.routing.Route)">ElectronicHorizonEngine</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a> options,
 <a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#addElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">addElectronicHorizonListener</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds an <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> to the subscription list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoute()">getRoute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> or <code>null</code> if <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> is not set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#removeElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">removeElectronicHorizonListener</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes an <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> from the subscription list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoute(com.here.sdk.routing.Route)">setRoute</a><wbr/>(<a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> to be used by <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>
 or <code>null</code> if no route should be used.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#update(com.here.sdk.navigation.MapMatchedLocation)">update</a><wbr/>(<a href="sdk-for-android-navigate-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the electronic horizon paths based on the provided map-matched location.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.electronichorizon.ElectronicHorizonOptions,com.here.sdk.transport.TransportMode,com.here.sdk.routing.Route)">
<h3>ElectronicHorizonEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElectronicHorizonEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @Nullable
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route)</span>
                        throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>The <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p></dd>
<dd><code>options</code> - <p>The <a href="sdk-for-android-navigate-electronichorizonoptions" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonOptions</code></a> instance that configures how the electronic horizon is calculated, including look-ahead distances.</p></dd>
<dd><code>transportMode</code> - <p>The <a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport"><code>TransportMode</code></a> that is used when building the electronic horizon paths.</p></dd>
<dd><code>route</code> - <p>The <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> that improves the calculation of the most-preferred path (MPP).
     If <code>null</code> is passed, the most-preferred path can deviate from the route.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> If the electronic horizon engine cannot be created.</p></dd>
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
<section class="detail" id="update(com.here.sdk.navigation.MapMatchedLocation)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation)</span></div>
<div class="block"><p>Updates the electronic horizon paths based on the provided map-matched location.
 This method returns immediately and does not block.
 When internal calculation is complete, callbacks are called on the main thread.
 When multiple updates are triggered while processing is still running,
 intermediate locations are skipped and only the last location is processed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapMatchedLocation</code> - <p>The map-matched location that defines the current vehicle position on the road network.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">
<h3>addElectronicHorizonListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElectronicHorizonListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span></div>
<div class="block"><p>Adds an <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> to the subscription list.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that receives electronic horizon path updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">
<h3>removeElectronicHorizonListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElectronicHorizonListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span></div>
<div class="block"><p>Removes an <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> from the subscription list.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that should no longer receive electronic horizon path updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoute()">
<h3>getRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()</div>
<div class="block"><p>Gets the instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> or <code>null</code> if <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> is not set.
 </p><p>You can override this property to rebuild the electronic horizon based on a different route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> that is being used by <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoute(com.here.sdk.routing.Route)">
<h3>setRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoute</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> value)</span></div>
<div class="block"><p>Sets the instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> to be used by <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>
 or <code>null</code> if no route should be used.
 </p><p>You can override this property to rebuild the electronic horizon based on a different route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The instance of <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> that is being used by <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
