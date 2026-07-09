---
title: "VenueEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-venueengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.VenueEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>VenueEngine is an add-on to the base map functionality with its
 own content loading and cache.
 VenueEngine gives access to the venue functionality, which allows you
 to load and visualize venues on the map, search content inside venues etc.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-venueengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.venue.VenueEngineInitCallback)">VenueEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-venueengine#%3Cinit%3E(com.here.sdk.venue.VenueEngineInitCallback)">VenueEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.venue.VenueEngineInitCallback)">
<h3>VenueEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VenueEngine</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span>
            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>The optional callback that will be triggered when a venue engine initialization
     will be completed. After the initialization, the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> should
     be started using one of its methods or using <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengine#start(java.lang.String)"><code>start(String)</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.venue.VenueEngineInitCallback)">
<h3>VenueEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VenueEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span>
            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of existing SDKEngine.</p></dd>
<dd><code>callback</code> - <p>The optional callback that will be triggered when a venue engine initialization
     will be completed. After the initialization, the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> should
     be started using one of its methods or using <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengine#start(java.lang.String)"><code>start(String)</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section className="detail" id="start(com.here.sdk.core.AuthenticationCallback)">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</span></div>
<div className="block"><p>Authenticates asynchronously using HERE SDK credentials and uses a result token to start
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. An initialization status of the venue service is
 returned to objects registered as <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service"><code>VenueServiceListener</code></a>. If the
 authentication will fail, the venue service will not be started.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>The optional callback that will be triggered when the authentication will be completed.
     If the authentication fails, the venue service will not be started.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="start(java.lang.String)">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</span></div>
<div className="block"><p>Authenticates asynchronously using HERE SDK credentials using a token to start
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. An initialization status of the venue service is
 returned to objects registered as <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service"><code>VenueServiceListener</code></a>. If the
 authentication will fail, the venue service will not be started.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>token</code> - <p>SDK project scope token to be used for authentication</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroy()">
<h3>destroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroy</span>()</div>
<div className="block"><p>Releases all internally used resources. The instance can't be used anymore after calling
 this method.</p></div>
</section>
</li>
<li>
<section className="detail" id="getVenueService()">
<h3>getVenueService</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span className="element-name">getVenueService</span>()</div>
<div className="block"><p>Gets the venue service. This service can be used to load the venue model objects.
 Gets the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>. This service
 can be used to load the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> objects.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The venue service.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueMap()">
<h3>getVenueMap</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a></span> <span className="element-name">getVenueMap</span>()</div>
<div className="block"><p>Gets a venue map to visualize venues.
 Gets a venue map to visualize venues and control the
 state of the venues on the map. You need to start the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a> to
 be able to load venues.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The venue map.</p></dd>
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
