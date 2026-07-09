---
title: "ElectronicHorizonEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ElectronicHorizonEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Provides an electronic horizon engine that continuously predicts
 the road network ahead of the vehicle by using detailed map data, including road topography that is
 currently out of sight.
 You can subscribe to electronic horizon updates based on position updates by using <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a>.
 For more information about sub path levels, see <a href="sdk-for-android-navigate-electronichorizonoptions#lookAheadDistancesInMeters"><code>ElectronicHorizonOptions.lookAheadDistancesInMeters</code></a>.
 The electronic horizon engine uses map-matched locations and can optionally use a <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a>
 to improve the most-preferred path (MPP).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.electronichorizon.ElectronicHorizonOptions,com.here.sdk.transport.TransportMode,com.here.sdk.routing.Route)">ElectronicHorizonEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a> options,
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.electronichorizon.ElectronicHorizonOptions,com.here.sdk.transport.TransportMode,com.here.sdk.routing.Route)">
<h3>ElectronicHorizonEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ElectronicHorizonEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route)</span>
                        throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p></dd>
<dd><code>options</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonOptions</code></a> instance that configures how the electronic horizon is calculated, including look-ahead distances.</p></dd>
<dd><code>transportMode</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport"><code>TransportMode</code></a> that is used when building the electronic horizon paths.</p></dd>
<dd><code>route</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> that improves the calculation of the most-preferred path (MPP).
     If <code>null</code> is passed, the most-preferred path can deviate from the route.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> If the electronic horizon engine cannot be created.</p></dd>
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
<section className="detail" id="update(com.here.sdk.navigation.MapMatchedLocation)">
<h3>update</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">update</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation)</span></div>
<div className="block"><p>Updates the electronic horizon paths based on the provided map-matched location.
 This method returns immediately and does not block.
 When internal calculation is complete, callbacks are called on the main thread.
 When multiple updates are triggered while processing is still running,
 intermediate locations are skipped and only the last location is processed.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapMatchedLocation</code> - <p>The map-matched location that defines the current vehicle position on the road network.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">
<h3>addElectronicHorizonListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addElectronicHorizonListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span></div>
<div className="block"><p>Adds an <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> to the subscription list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that receives electronic horizon path updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeElectronicHorizonListener(com.here.sdk.electronichorizon.ElectronicHorizonListener)">
<h3>removeElectronicHorizonListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeElectronicHorizonListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span></div>
<div className="block"><p>Removes an <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> from the subscription list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that should no longer receive electronic horizon path updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoute()">
<h3>getRoute</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span className="element-name">getRoute</span>()</div>
<div className="block"><p>Gets the instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> or <code>null</code> if <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> is not set.
 You can override this property to rebuild the electronic horizon based on a different route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> that is being used by <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoute(com.here.sdk.routing.Route)">
<h3>setRoute</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoute</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span></div>
<div className="block"><p>Sets the instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> to be used by <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>
 or <code>null</code> if no route should be used.
 You can override this property to rebuild the electronic horizon based on a different route.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> that is being used by <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</p></dd>
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
